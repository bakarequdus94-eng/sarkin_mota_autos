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
    # Combined single list_display config block
    list_display = ('brand', 'name', 'price', 'year', 'transmission', 'condition')
    
    # Hooks up the photo gallery and video slots inside the car creation page
    inlines = [CarImageInline, CarVideoInline] 
    
    # Adds a sidebar filtering layout on the right side of the admin screen
    list_filter = ('condition', 'transmission', 'year', 'brand')
    
    # Lets you search your vehicle inventory quickly
    search_fields = ('name', 'brand', 'description')

    # Fixed: Correctly indented inside CarAdmin class to register your custom JS script
    class Media:
        js = ('showroom/js/admin_drag_drop.js',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('car', 'name', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('name', 'comment', 'car__name')


# Optional separate endpoints for single actions
admin.site.register(CarImage)
admin.site.register(CarVideo)