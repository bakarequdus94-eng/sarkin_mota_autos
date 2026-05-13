from django.contrib import admin
from django.urls import path
from showroom import views
from django.conf import settings
from django.conf.urls.static import static # Fixed the .urls here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing_page, name='landing'),
    path('showroom/', views.car_list, name='car_list'),
    path('car/<int:car_id>/', views.car_detail, name='car_detail'),
]

# This ensures your car photos actually appear on the screen
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)