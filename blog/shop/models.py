from django.db import models
from django.conf import settings

STATUS_CHOICES = (("IN_STOCK", "In Stock"), ("OUT_OF_STOCK", "Out Of Stock"))

ORDER_BY_CHOICES = (
    ("price_asc", "Price Asc"),
    ("price_desc", "Price Desc"),
    ("max_count", "Max Count"),
    ("max_price", "Max Price"),
)


class Product(models.Model):
   title = models.CharField(max_length=200)
   image = models.ImageField(null=True, blank=True)
   cost = models.IntegerField()
   status = models.CharField(
       max_length=100, choices=STATUS_CHOICES, default="IN_STOCK"
   )


   def __str__(self):
       return self.title


class Purchase(models.Model):
   user = models.ForeignKey(
       settings.AUTH_USER_MODEL, related_name="purchases",  on_delete=models.CASCADE
   )
   product = models.ForeignKey(
       Product, related_name="purchases", on_delete=models.CASCADE
   )
   count = models.IntegerField()


class Iphone6(models.Model):
   title = models.CharField(max_length=200)
   description = models.CharField(max_length=200)
   price = models.CharField(max_length=50)
   created_at = models.DateTimeField(
       auto_now_add=True, db_index=True
   )

   def __str__(self):
       return self.title



# Create your models here.
