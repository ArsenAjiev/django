from django.contrib import admin
from shop.models import Product, Purchase, Iphone6

class PurchaseInline(admin.TabularInline):
   model = Purchase

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
   list_display = ( "title", "cost", "image", "status")
   search_fields = ("title",)
   inlines = [
      PurchaseInline,
   ]

@admin.register(Purchase)
class PurshaseAdmin(admin.ModelAdmin):
   list_display = ("user", "product", "count",)
   search_fields = ("product",)

@admin.register(Iphone6)
class Iphone6Admin(admin.ModelAdmin):
   list_display = ("title", "description", "price",)
   search_fields = ("title",)




# Register your models here.
