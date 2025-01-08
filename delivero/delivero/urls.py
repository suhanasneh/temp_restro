from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('food_book.urls')),
    path('admin/', admin.site.urls),
]