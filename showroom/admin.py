from django.contrib import admin
from .models import Car, CarImage, CarVideo, Review, InspectionBooking

@admin.register(InspectionBooking)
class InspectionBookingAdmin(admin.ModelAdmin):
    list_display = ('car', 'name', 'date', 'time_slot', 'created_at')
    list_filter = ('date', 'time_slot', 'car')
    search_fields = ('name', 'email', 'phone', 'car__name')

# Add multiple photos directly inside the Car admin page
class CarImageInline(admin.TabularInline):
    model = CarImage
    extra = 7 
    max_num = 7

# Add videos directly inside the Car admin page
class CarVideoInline(admin.TabularInline):
    model = CarVideo
    extra = 3
    max_num = 3

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price', 'year', 'condition', 'is_available', 'created_at')
    list_filter = ('brand', 'condition', 'is_available', 'body_type')
    search_fields = ('name', 'brand', 'description')
    ordering = ('-created_at',)
    # THIS LINE WAS MISSING: This links your image and video slots directly into the car page!
    inlines = [CarImageInline, CarVideoInline]

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'car', 'rating', 'email', 'created_at')
    list_filter = ('rating', 'created_at', 'car')
    search_fields = ('name', 'comment', 'email')
    ordering = ('-created_at',)

# Optional separate endpoints for single actions
admin.site.register(CarImage)
admin.site.register(CarVideo)