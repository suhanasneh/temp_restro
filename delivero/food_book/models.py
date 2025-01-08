from django.db import models
from food_book.const_enums import FOOD_TYPE
from django.contrib.auth.models import AbstractUser


# Create your models here.


class Timestamp(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=20)

    def __str__(self):
        return self.email


class Product(Timestamp):
    name = models.CharField(max_length=255)
    food_type = models.CharField(choices=FOOD_TYPE,max_length=30)
    price = models.IntegerField()
    time_to_cook = models.IntegerField()


    def __str__(self):
        return self.name


class Order(Timestamp):
    products = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name='customer')
    time_to_cook = models.IntegerField()
    arrival_time = models.DateTimeField()

    def __str__(self):
        return f'{self.customer} arriving at {self.arrival_time}'
