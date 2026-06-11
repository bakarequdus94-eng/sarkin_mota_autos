from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect  # Added redirect here
from .models import Car, Review  # Cleaned up duplicate imports

# Fix for the terminal error landing page
def landing_page(request):
    return render(request, 'showroom/landing.html')

def car_list(request):
    cars = Car.objects.all().order_by('-id')  # Ordered by newest first

    # Capture GET parameters from the advanced search form
    query = request.GET.get('q', '').strip()
    car_type = request.GET.get('car_type', '').strip()
    max_price = request.GET.get('max_price', '').strip()

    # Apply filters dynamically if they exist
    if query:
        cars = cars.filter(
            Q(name__icontains=query) | 
            Q(brand__icontains=query) | 
            Q(description__icontains=query)
        )
    
    if car_type:
        cars = cars.filter(car_type__iexact=car_type)

    if max_price:
        try:
            cars = cars.filter(price__lte=float(max_price))
        except ValueError:
            pass  # Ignore if the user type input isn't a valid number

    # Pagination setup (6 cars per page)
    paginator = Paginator(cars, 6) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Combined single context dictionary
    context = {
        'page_obj': page_obj,  # Use page_obj in your template loop now!
        'query': query,
        'car_type': car_type,
        'max_price': max_price,
    }
    return render(request, 'showroom/car_list.html', context)

# View for car details page
def car_detail(request, pk):
    # Fetch the car using the primary key (pk)
    car = get_object_or_404(Car, id=pk)
    
    # Process review submissions when users click 'Submit Review'
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        
        # Save the new review straight into your PostgreSQL database
        if name and email and rating and comment:
            Review.objects.create(
                car=car,
                name=name,
                email=email,
                rating=int(rating),
                comment=comment
            )
            # Redirect straight back to the same page to prevent duplicate submissions on refresh
            return redirect('car_detail', pk=car.id)

    # Fetch all approved reviews for this specific vehicle to display them
    reviews = car.reviews.all()  # Uses the related_name='reviews' from your model

    context = {
        'car': car,
        'reviews': reviews,
    }
    return render(request, 'showroom/car_detail.html', context)

# View for submitting a customer review
def add_review(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')

        if name and rating:
            Review.objects.create(
                car=car,
                name=name,
                email=email,
                rating=int(rating),
                comment=comment
            )
    return redirect('car_detail', pk=car.id)