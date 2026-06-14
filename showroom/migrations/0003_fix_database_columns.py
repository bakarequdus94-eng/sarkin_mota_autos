from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('showroom', '0002_booking_table'), # This points to the file currently live on your DB
    ]

    operations = [
        # Rename full_name to name
        migrations.RenameField(
            model_name='inspectionbooking',
            old_name='full_name',
            new_name='name',
        ),
        # Rename phone_number to phone
        migrations.RenameField(
            model_name='inspectionbooking',
            old_name='phone_number',
            new_name='phone',
        ),
        # Rename preferred_date to date
        migrations.RenameField(
            model_name='inspectionbooking',
            old_name='preferred_date',
            new_name='date',
        ),
        # Rename preferred_time to time_slot
        migrations.RenameField(
            model_name='inspectionbooking',
            old_name='preferred_time',
            new_name='time_slot',
        ),
    ]