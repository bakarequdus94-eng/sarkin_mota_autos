from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('showroom', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InspectionBooking',
            fields=[
                ('id', models.BigAutoField(auto_state=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_name=255)),
                ('phone_number', models.CharField(max_name=20)),
                ('email', models.EmailField(max_name=254)),
                ('preferred_date', models.DateField()),
                ('preferred_time', models.CharField(max_name=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='showroom.car')),
            ],
            options={
                'db_table': 'showroom_inspectionbooking',
            },
        ),
    ]