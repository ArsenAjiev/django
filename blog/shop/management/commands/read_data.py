from django.core.management.base import BaseCommand

from blog import settings
from shop.models import Iphone6
import csv


# # # записывет данные из csv - posts_kufar.csv в таблицу iphone
class Command(BaseCommand):
    help = "Show all post"

    def handle(self, *args, **options):
        with open(settings.BASE_DIR / "posts_kufar.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                Iphone6.objects.create(title=row[0], description=row[1], price=row[2])