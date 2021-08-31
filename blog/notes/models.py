from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models


class Notes(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(
        auto_now_add=True, db_index=True
    )

#
# class Tags(models.Model):
#     title = models.CharField(max_length=100)
#     posts = models.ManyToManyField(Post, related_name="tags")
#
#     class Meta:
#         verbose_name = "Tag"
#         verbose_name_plural = "Tags"