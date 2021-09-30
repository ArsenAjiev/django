# management/commands/python_zen.py

from django.core.management.base import BaseCommand

from blog import settings
from post.models import Post
import csv

from django.core.management.base import BaseCommand

from blog import settings
from post.models import Post
import csv


# # # записывет данные из csv - post.csv в таблицу Post
# class Command(BaseCommand):
#     help = "Show all post"
#
#     def handle(self, *args, **options):
#         with open(settings.BASE_DIR / "posts.csv", "r") as file:
#             reader = csv.reader(file)
#             for row in reader:
#                 Post.objects.create(title=row[0], slug=row[1], text=row[2])




# записывет данные из таблицы Post  в csv - post.csv
class Command(BaseCommand):
    help = "Show all post"

    def handle(self, *args, **options):
        with open(settings.BASE_DIR / "posts.csv", "w") as file:
            writer = csv.writer(file)
            for post in Post.objects.all():
                writer.writerow([ post.title, post.slug, post.text])




# class Command(BaseCommand):
#    help = "Show all post"
#
#    def handle(self, *args, **options):
#        for post in Post.objects.all():
#            print(post.title)