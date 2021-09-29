# management/commands/python_zen.py

from django.core.management.base import BaseCommand

from blog import settings
from post.models import Post
import csv

class Command(BaseCommand):
    help = "Show all post"

    def handle(self, *args, **options):
        with open(settings.BASE_DIR / "posts.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                Post.objects.create(title=row[0], slug=row[1], text=row[2])





# class Command(BaseCommand):
#     help = "Show all post"
#
#     def handle(self, *args, **options):
#         with open(settings.BASE_DIR / "posts.csv", "w") as file:
#             writer = csv.writer(file)
#             for post in Post.objects.all():
#                 writer.writerow([post.id, post.title])




# class Command(BaseCommand):
#    help = "Show all post"
#
#    def handle(self, *args, **options):
#        for post in Post.objects.all():
#            print(post.title)