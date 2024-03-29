from django.core.management.base import BaseCommand

from shop.spiders_kufar import AvitoSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


class Command(BaseCommand):
   help = "Crawl onliner catalog"

   def handle(self, *args, **options):
       process = CrawlerProcess(get_project_settings())
       process.crawl(AvitoSpider)
       process.start()