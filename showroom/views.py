from django.db import connection
from django.http import HttpResponse

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
            
            # Create an index on car_id just to keep queries lightning fast
            cursor.execute('''
                CREATE INDEX IF NOT EXISTS showroom_review_car_id_idx ON showroom_review(car_id);
            ''')

        return HttpResponse("✅ SUCCESS! The showroom_review table has been created in PostgreSQL. Restoring your view now will fix the page!")
    except Exception as e:
        return HttpResponse(f"❌ SQL Execution Error: {e}")