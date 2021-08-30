from django.contrib import admin

# Register your models here.

# admin.py
#from django.contrib import admin

from post.models import Post, Tags


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
   list_display = ("author", "title", "slug", "created_at", "test")
   fields = ("author", "title", "image", "slug", "text", "created_at", "test")
   readonly_fields = ("created_at",)
   search_fields = ("title", "slug", "text")

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
   list_display = ( "title",)
   fields = ("title",)
   search_fields = ("title",)