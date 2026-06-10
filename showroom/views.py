from django.db import connection
from django.http import HttpResponse

def landing_page(request):
    """Placeholder view to keep urls.py happy during migration fixes."""
    return car_list(request)

def car_list(request):
    try:
        with connection.cursor() as cursor:
            # Force create the entire showroom_review table with all standard fields
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS showroom_review (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    email VARCHAR(254) NULL,
                    rating INTEGER NOT NULL,
                    comment TEXT NOT NULL,
                    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
                    car_id INTEGER NOT NULL REFERENCES showroom_car(id) ON DELETE CASCADE
                );
            ''')
            
            # Create index for review queries
            cursor.execute('''
                CREATE INDEX IF NOT EXISTS showroom_review_car_id_idx ON showroom_review(car_id);
            ''')

        return HttpResponse("✅ SUCCESS! The showroom_review table has been forced into PostgreSQL. You can safely restore your original views now!")
    except Exception as e:
        return HttpResponse(f"❌ SQL Execution Error: {e}")

def car_detail(request, *args, **kwargs):
    return car_list(request)

def add_review(request, *args, **kwargs):
    return car_list(request)