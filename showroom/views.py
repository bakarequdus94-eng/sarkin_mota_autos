from django.db import connection
from django.http import HttpResponse

def landing_page(request):
    try:
        with connection.cursor() as cursor:
            # 1. Force inject the condition column
            cursor.execute('''
                ALTER TABLE showroom_car 
                ADD COLUMN IF NOT EXISTS condition VARCHAR(100) DEFAULT 'Foreign Used';
            ''')
            
            # 2. Force inject color column
            cursor.execute('''
                ALTER TABLE showroom_car 
                ADD COLUMN IF NOT EXISTS color VARCHAR(50) DEFAULT 'Black';
            ''')
            
            # 3. Force inject body_type column
            cursor.execute('''
                ALTER TABLE showroom_car 
                ADD COLUMN IF NOT EXISTS body_type VARCHAR(50) DEFAULT 'SUV';
            ''')
            
            # 4. Force inject is_available column
            cursor.execute('''
                ALTER TABLE showroom_car 
                ADD COLUMN IF NOT EXISTS is_available BOOLEAN DEFAULT TRUE;
            ''')

        return HttpResponse("✅ SUCCESS! Database structural columns updated.")
    except Exception as e:
        return HttpResponse(f"❌ SQL Execution Error: {e}")