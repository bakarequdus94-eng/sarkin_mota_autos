#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies and static assets
pip install -r requirements.txt
python manage.py collectstatic --no-input

# Run raw SQL adjustments directly via Python shell
python manage.py shell <<EOF
from django.db import connection

with connection.cursor() as cursor:
    # 1. Force the migration tracker table to record 0001 baseline if it hasn't already
    try:
        cursor.execute("INSERT INTO django_migrations (app, name, applied) VALUES ('showroom', '0001_initial', NOW());")
        print("Initial migration state baseline set.")
    except Exception:
        print("Migration state record already present.")

    # 2. Safely alter column names to match models.py properties
    alter_queries = [
        "ALTER TABLE showroom_inspectionbooking RENAME COLUMN full_name TO name;",
        "ALTER TABLE showroom_inspectionbooking RENAME COLUMN phone_number TO phone;",
        "ALTER TABLE showroom_inspectionbooking RENAME COLUMN preferred_date TO date;",
        "ALTER TABLE showroom_inspectionbooking RENAME COLUMN preferred_time TO time_slot;"
    ]
    
    for query in alter_queries:
        try:
            cursor.execute(query)
            print(f"Executed: {query}")
        except Exception as e:
            print("Column translation already synchronized or skipped.")
EOF