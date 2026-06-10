from django.contrib import admin
from .models import Car, CarImage, CarVideo
from .models import Review

# This allows you to add photos directly inside the Car page
class CarImageInline(admin.TabularInline):
    model = CarImage
    extra = 7 # This gives you one empty slot to start with
    max_num = 7
# This allows you to add videos directly inside the Car page
class CarVideoInline(admin.TabularInline):
    model = CarVideo
    extra = 3
    max_num = 3
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'name', 'price') # Shows these columns in the main list
    inlines = [CarImageInline, CarVideoInline] # Hooks up the gallery and video slots
# list_display controls the columns you see when looking at the list of all cars
    list_display = ('name', 'brand', 'price', 'year', 'transmission', 'condition')
    
    # list_filter adds a clean filtering sidebar on the right side of the admin page
    list_filter = ('condition', 'transmission', 'year', 'brand')
    
    # search_fields lets you quickly find cars by typing in the admin search bar
    search_fields = ('name', 'brand', 'description')
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('car', 'name', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('name', 'comment', 'car__name')
class Media:
        js = ('showroom/js/admin_drag_drop.js',)
# Optionally register these if you want to edit them separately, 
# but the Inlines above are usually enough!
admin.site.register(CarImage)
admin.site.register(CarVideo)