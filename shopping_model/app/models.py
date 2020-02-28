from django.db import models
from django.conf import settings
# Create your models here.

class Products(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=300)


    def __str__(self):
        return self.title

class OrderProducts(models.Model):
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.quantity} of {self.product.title}"

    def get_total_item_price(self):
        return self.quantity*self.product.price

    def get_total_item_discount_price(self):
        return self.quantity*self.product.discount_price

    def get_amount_saved(self):
        return self.get_total_item_price() -  self.get_total_item_discount_price()

    def get_final_price(self):
        if self.product.discount_price:
            return self.get_total_item_discount_price()
        else:
            return self.get_total_item_price()



class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderProducts)
    start_date = models.DateTimeField(auto_now_add=True)
    odered_date = models.DateTimeField()

    def __str__(self):
        return self.user.username

    def get_total(self):
        total= 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total
