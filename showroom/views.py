from django.db import connection
from django.http import HttpResponse

def landing_page(request):
    try:
        with connection.cursor() as cursor:
            # Force inject all missing database columns at once
            cursor.execute("ALTER TABLE showroom_car ADD COLUMN IF NOT EXISTS created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW();")
            cursor.execute("ALTER TABLE showroom_car ADD COLUMN IF NOT EXISTS year INTEGER DEFAULT 2020;")
            cursor.execute("ALTER TABLE showroom_car ADD COLUMN IF NOT EXISTS mileage INTEGER DEFAULT 0;")
            cursor.execute("ALTER TABLE showroom_car ADD COLUMN IF NOT EXISTS transmission VARCHAR(50) DEFAULT 'Automatic';")
            cursor.execute("ALTER TABLE showroom_car ADD COLUMN IF NOT EXISTS fuel_type VARCHAR(50) DEFAULT 'Petrol';")
            cursor.execute("ALTER TABLE showroom_car ADD COLUMN IF NOT EXISTS engine_size VARCHAR(50) DEFAULT 'V6';")
            cursor.execute("ALTER TABLE showroom_car ADD COLUMN IF NOT EXISTS condition VARCHAR(100) DEFAULT 'Foreign Used';")
            cursor.execute("ALTER TABLE showroom_car ADD COLUMN IF NOT EXISTS color VARCHAR(50) DEFAULT 'Black';")
            cursor.execute("ALTER TABLE showroom_car ADD COLUMN IF NOT EXISTS body_type VARCHAR(50) DEFAULT 'SUV';")
            cursor.execute("ALTER TABLE showroom_car ADD COLUMN IF NOT EXISTS is_available BOOLEAN DEFAULT TRUE;")

        return HttpResponse("✅ SUCCESS! All database structural columns have been successfully forced into PostgreSQL. You can safely restore your original views now!")
    except Exception as e:
        return HttpResponse(f"❌ SQL Execution Error: {e}")

# Placeholders to prevent 'AttributeError' in your urls.py during build
def car_list(request):
    return landing_page(request)

def car_detail(request, *args, **kwargs):
    return landing_page(request)

def add_review(request, *args, **kwargs):
    return landing_page(request)
    