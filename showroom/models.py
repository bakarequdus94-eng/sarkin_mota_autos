from django.db import models
from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import User

class Car(models.Model):
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField()
    image = CloudinaryField('image') 
    created_at = models.DateTimeField(auto_now_add=True)
    
   # Made these safe for existing database records
    year = models.PositiveIntegerField(default=2020)
    mileage = models.PositiveIntegerField(default=0)

    TRANSMISSION_CHOICES = [
        ('Automatic', 'Automatic'),
        ('Manual', 'Manual'),
    ]
    transmission = models.CharField(max_length=20, choices=TRANSMISSION_CHOICES, default='Automatic')

    CONDITION_CHOICES = [
        ('Brand New', 'Brand New'),
        ('Foreign Used', 'Foreign Used'),
        ('Local Used', 'Local Used'),
    ]
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, default='Foreign Used')

    # THE MISSING FIELDS RENDER IS LOOKING FOR:
    body_type = models.CharField(max_length=50, default='SUV')
    is_available = models.BooleanField(default=True)
    
    # Other metadata fields
    fuel_type = models.CharField(max_length=50, default='Petrol')
    engine_size = models.CharField(max_length=50, default='V6')
    color = models.CharField(max_length=50, default='Black')
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def is_new(self):
        return timezone.now() - self.created_at < timedelta(days=7)

    @property
    def is_hot(self):
        return self.average_rating >= 4.5 and self.reviews.count() >= 3

    @property
    def average_rating(self):
        reviews = self.reviews.all()
        if reviews.exists():
            total = sum([r.rating for r in reviews])
            return round(total / reviews.count(), 1)
        return 0

    def __str__(self):
        return f"{self.brand} {self.name}"


class CarImage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='images')
    image = CloudinaryField('image')

    def __str__(self):
        return f"Image for {self.car.brand} {self.car.name}"


# Fixed indentation and layout for the video model
class CarVideo(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='additional_videos')
    video = CloudinaryField('video', resource_type='video')

    def __str__(self):
        return f"Video for {self.car.brand} {self.car.name}"


class Review(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Rating must be between 1 and 5 stars"
    )
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.rating} Stars by {self.name} for {self.car.name}"
        
class InspectionBooking(models.Model):
    TIME_SLOTS = [
        ('10:00', '10:00 AM'),
        ('12:00', '12:00 PM'),
        ('14:00', '02:00 PM'),
        ('16:00', '04:00 PM'),
    ]

    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='inspections')
    # If users aren't forced to log in, you can use name/phone instead of a User relation
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    date = models.DateField()
    time_slot = models.CharField(max_length=5, choices=TIME_SLOTS)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Prevents double booking the same car at the exact same time
        unique_together = ('car', 'date', 'time_slot')

    def __str__(self):
        return f"Inspection for {self.car.name} by {self.name} on {self.date}"