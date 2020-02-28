from django.contrib import admin
from . models import Products,OrderProducts,Order
# Register your models here.

admin.site.register(Products)
admin.site.register(OrderProducts)
admin.site.register(Order)
