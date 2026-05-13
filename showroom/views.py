from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Car

# Add this to fix the terminal error
def landing_page(request):
    return render(request, 'showroom/landing.html')

def car_list(request):
    query = request.GET.get('q')
    if query:
        cars = Car.objects.filter(
            Q(name__icontains=query) | 
            Q(brand__icontains=query) | 
            Q(description__icontains=query)
        ).order_by('-id')
    else:
        cars = Car.objects.all().order_by('-id')

    paginator = Paginator(cars, 10) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'showroom/car_list.html', {'page_obj': page_obj, 'query': query})

# You will also likely need this for your car details
def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    return render(request, 'showroom/car_detail.html', {'car': car})