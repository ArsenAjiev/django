from django.db import models
from django.conf import settings



class Product(models.Model):
   title = models.CharField(max_length=200)
   cost = models.IntegerField()

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



# Create your models here.
