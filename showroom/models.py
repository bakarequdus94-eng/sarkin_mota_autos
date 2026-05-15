from django.db import models
from cloudinary.models import CloudinaryField

class Car(models.Model):
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField()
    # Using your preferred CloudinaryField
    image = CloudinaryField('image') 

    def __str__(self):
        return f"{self.brand} {self.name}"

# Add this new class below your Car class
class CarImage(models.Model):
    car = models.ForeignKey(Car, default=None, on_delete=models.CASCADE, related_name='additional_images')
    image = CloudinaryField('image')

    def __str__(self):
        return self.car.name
        # Add this below your CarImage class
class CarVideo(models.Model):
    car = models.ForeignKey(Car, default=None, on_delete=models.CASCADE, related_name='additional_videos')
    video = CloudinaryField('video', resource_type='video') # Specifying video type

    def __str__(self):
        return f"Video for {self.car.name}"