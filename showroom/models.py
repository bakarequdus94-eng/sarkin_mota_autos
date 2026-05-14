from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='cars/') 

    def __str__(self): # Fixed from __clstr__
        return f"{self.brand} {self.name}"

class CarImage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='cars/gallery/')

class CarVideo(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='videos')
    video = models.FileField(upload_to='cars/videos/')
    
    def __str__(self): # Fixed from __clstr_
        return f"Video for {self.car.name}"