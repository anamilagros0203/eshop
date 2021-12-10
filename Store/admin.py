from django.contrib import admin
from .models.category import Category
from .models.product import Products
from .models.customer import Customer
from .models.orders import Order

# Register your models here.

admin.site.register(Products)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)
