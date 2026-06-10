from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Car
from .models import Car, Review

# Add this to fix the terminal error
def landing_page(request):
    return render(request, 'showroom/landing.html')

def car_list(request):
    cars = Car.objects.all()

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
            pass # Ignore if the user type input isn't a valid number

    context = {
        'cars': cars,
        'query': query,
        'car_type': car_type,
        'max_price': max_price,
    }
    return render(request, 'showroom/car_list.html', context)

    paginator = Paginator(cars, 10) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
    'page_obj': page_obj, # This keeps your loop working perfectly!
    'query': query,
    'car_type': car_type,
    'max_price': max_price,
}
    return render(request, 'showroom/car_list.html', {'page_obj': page_obj, 'query': query})

# You will also likely need this for your car details
def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    return render(request, 'showroom/car_detail.html', {'car': car})

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