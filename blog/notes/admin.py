from django.contrib import admin

# Register your models here.

from notes.models import Notes


@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
   list_display = ("author", "title", "created_at")
   fields = ("author", "title")

