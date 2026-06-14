import requests
from django.core.cache import cache
from django.shortcuts import render
from .models import Car # Assuming your model is named Car

def get_exchange_rates():
    """
    Fetches live exchange rates with NGN as base currency.
    Caches the results for 6 hours to prevent hitting API limits on every refresh.
    """
    rates = cache.get('sarkin_mota_rates')
    if not rates:
        try:
            # Free API endpoint (Replace 'YOUR-API-KEY' with a key from exchangerate-api.com)
            url = "https://open.er-api.com/v6/latest/NGN"
            response = requests.get(url, timeout=5)
            data = response.json()
            
            if data.get("result") == "success":
                rates = {
                    "USD": data["rates"].get("USD", 0.00065), # Fallbacks if API goes down
                    "EUR": data["rates"].get("EUR", 0.00060),
                    "NGN": 1.0
                }
                # Cache the rates for 6 hours (21600 seconds)
                cache.set('sarkin_mota_rates', rates, 21600)
        except Exception:
            # Secure fallback rates if the server has no internet or API fails
            rates = {"USD": 0.00065, "EUR": 0.00060, "NGN": 1.0}
            
    return rates

def car_list_view(request):
    """ Your main showroom view """
    cars = Car.objects.all()
    rates = get_exchange_rates()
    
    context = {
        'cars': cars,
        'rates_json': rates, # Pass this dictionary to JavaScript later
    }
    return render(request, 'showroom/car_list.html', context)