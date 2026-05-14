from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField()
    # Simplified for Cloudinary
    image = models.ImageField() 

    def __str__(self):
        return f"{self.brand} {self.name}"

class CarImage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='gallery')
    # Simplified for Cloudinary
    image = models.ImageField() 

class CarVideo(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='videos')
    # Simplified for Cloudinary
    video = models.FileField()

    def __str__(self):
        return f"Video for {self.car.name}"