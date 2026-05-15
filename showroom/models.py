from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField()
    # Use standard ImageField; Cloudinary Storage handles the rest
    image = models.ImageField(upload_to='cars/') 

    def __str__(self):
        return f"{self.brand} {self.name}"

class CarImage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='gallery')
    image = models.ImageField(upload_to='cars/gallery/') 

class CarVideo(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='videos')
    # Use FileField for videos
    video = models.FileField(upload_to='cars/videos/')

    def __str__(self):
        return f"Video for {self.car.name}"