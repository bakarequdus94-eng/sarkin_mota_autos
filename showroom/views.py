from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect  # Added redirect here
from .models import Car, Review  # Cleaned up duplicate imports
from django.db import connection
from django.http import HttpResponse
 
 def landing_page(request):
    try:
        with connection.cursor() as cursor:
            # 1. Force inject the missing condition field (Text/CharField)
            cursor.execute('''
                ALTER TABLE showroom_car 
                ADD COLUMN IF NOT EXISTS condition VARCHAR(100) DEFAULT 'Foreign Used';
            ''')
            
            # 2. Force inject color (Just in case it's in your model)
            cursor.execute('''
                ALTER TABLE showroom_car 
                ADD COLUMN IF NOT EXISTS color VARCHAR(50) DEFAULT 'Black';
            ''')
            
            # 3. Force inject body_type (e.g., Sedan, SUV)
            cursor.execute('''
                ALTER TABLE showroom_car 
                ADD COLUMN IF NOT EXISTS body_type VARCHAR(50) DEFAULT 'SUV';
            ''')
            
            # 4. Force inject availability status (Boolean toggle)
            cursor.execute('''
                ALTER TABLE showroom_car 
                ADD COLUMN IF NOT EXISTS is_available BOOLEAN DEFAULT TRUE;
            ''')

        return HttpResponse("✅ SUCCESS! Condition, color, body type, and status columns have been injected. Let's load the car!")
    except Exception as e:
        return HttpResponse(f"❌ SQL Execution Error: {e}")

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
    car = get_object_or_404(Car, pk=pk)
    return render(request, 'showroom/car_detail.html', {'car': car})

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