from django.shortcuts import render
from shop.models import Product, Purchase
from django.http import HttpResponse



def shop_index(request):
   product = Product.objects.all()
   return render(request, "shop_list.html", {"product": product})

# return HttpResponse("Shop index view- Hello world")
# Create your views here.
