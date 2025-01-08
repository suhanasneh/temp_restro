from django.shortcuts import render
from rest_framework import viewsets
from food_book.models import Customer
from food_book.serializer import CustomerSerializer


# Create your views here.
class CustomerViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    # serializer_class = UserSerializer
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
