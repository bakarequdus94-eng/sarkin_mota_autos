import os
from django.contrib import admin
from django.urls import path
from showroom import views
from django.conf import settings
from django.conf.urls.static import static # Fixed the .urls here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing_page, name='landing'),
    path('showroom/', views.car_list, name='car_list'),
    path('car/<int:pk>/', views.car_detail, name='car_detail'),
    path('car/<int:car_id>/review/', views.add_review, name='add_review'),
path('car/<int:car_id>/book-inspection/', views.book_inspection, name='book_inspection'),
]

# This ensures your car photos actually appear on the screen
# ONLY serve media locally if we aren't using Cloudinary
if settings.DEBUG and not os.environ.get('CLOUDINARY_STORAGE'):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)