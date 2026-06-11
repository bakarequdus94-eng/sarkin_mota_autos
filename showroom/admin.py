from django.contrib import admin
from .models import Car, CarImage, CarVideo, Review

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

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    # This makes the reviews pop up cleanly in a table view
    list_display = ('name', 'car', 'rating', 'email', 'created_at')
    
    # Allows you to instantly filter by rating (e.g., view all 1-star or 5-star reviews)
    list_filter = ('rating', 'created_at', 'car')
    
    # Let's you quickly search through comments or reviewer names
    search_fields = ('name', 'comment', 'email')
    
    # Sorts them so the newest inspection reviews appear at the very top
    ordering = ('-created_at',)


# Optional separate endpoints for single actions
admin.site.register(CarImage)
admin.site.register(CarVideo)