from django.db import models
from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from datetime import timedelta

class Car(models.Model):
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField()
    image = CloudinaryField('image') 
    created_at = models.DateTimeField(auto_now_add=True) # Automatically grabs the exact date/time it was created
    year = models.PositiveIntegerField(default=2026)
    mileage = models.PositiveIntegerField(help_text="Mileage in kilometers (km)", default=0)
    
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
    @property
    def is_new(self):
        # Returns True if the car was added less than 7 days ago
        return timezone.now() - self.created_at < timedelta(days=7)

    @property
    def is_hot(self):
        # A car is "Hot" if it has an average rating of 4.5 or higher and at least 3 reviews
        # (This ties perfectly into the rating system we just built!)
        return self.average_rating >= 4.5 and self.reviews.count() >= 3

    @property
    def average_rating(self):
        reviews = self.reviews.all()
        if reviews.exists():
            total = sum([r.rating for r in reviews])
            return round(total / reviews.count(), 1)
        return 0 # Returns 0 if there are no reviews yet

    def __str__(self):
        return f"{self.brand} {self.name}"

# Your multi-image model remains perfectly streamlined
class CarImage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='images')
    image = CloudinaryField('image')

    def __str__(self):
        return f"Image for {self.car.brand} {self.car.name}"
        # Add this below your CarImage class
class CarVideo(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='additional_videos')
    video = CloudinaryField('video', resource_type='video')

    def __str__(self):
        return f"Video for {self.car.name}"

# Keep your existing Car, CarImage, and CarVideo models here...

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