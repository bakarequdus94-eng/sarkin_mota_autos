from django.contrib import admin
from .models import Car, CarImage, CarVideo # Changed to CarImage

class ExtraPhotoInline(admin.TabularInline):
    model = CarImage # Changed to CarImage
    extra = 1

class CarVideoInline(admin.TabularInline):
    model = CarVideo
    extra = 1

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    inlines = [ExtraPhotoInline, CarVideoInline]
    list_display = ('name', 'brand', 'price')

admin.site.register(CarImage) # Changed to CarImage
admin.site.register(CarVideo)