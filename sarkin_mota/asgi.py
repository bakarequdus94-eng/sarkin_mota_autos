import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sarkin_mota.settings')

# Initialize the core application
application = get_wsgi_application()

# --- FORCE RENDER TO RUN MIGRATIONS ON STARTUP ---
try:
    from django.core.management import call_command
    print("Executing dynamic database migrations on startup...")
    call_command('migrate', interactive=False)
    print("Database migrations applied successfully!")
except Exception as e:
    print(f"Startup migration bypass logged an error: {e}")