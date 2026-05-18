from django.db import models
from cloudinary.models import CloudinaryField

class Car(models.Model):
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField()
    image = CloudinaryField('image') 

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