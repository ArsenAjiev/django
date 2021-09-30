from django.contrib import admin
from shop.models import Product, Purchase

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




# Register your models here.
