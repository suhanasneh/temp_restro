
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from food_book import views

from django.urls import path
from . import views

urlpatterns = [
    path('customers/', views.CustomerViewSet.as_view({'get': 'list'}), name='cust'),
]