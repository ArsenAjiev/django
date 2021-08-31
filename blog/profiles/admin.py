from django.contrib import admin

# Register your models here.

from profiles.models import Profile 


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
   list_display = ("user", "first_name", "last_name", "created_at")
   fields = ("user", "first_name", "last_name", "image")


