import scrapy
import csv
from django.conf import settings
import logging

logger = logging.getLogger(__name__)


# class OmaSpider(scrapy.Spider):
#     name = "oma.by"
#     allowed_domains = ["https://www.oma.by"]
#     start_urls = ["https://www.oma.by/elektroinstrument-c"]
#
#     def parse(self, response, **kwargs):
#         with open(settings.BASE_DIR / "posts1.csv", "w") as file:
#             writer = csv.writer(file)
#
#             for product in response.css(".catalog-grid .product-item"):
#                 data = {
#                     "title": product.css(".product-title-and-rate-block .wrapper::text").get().strip(),
#                     "price": product.css(".product-price-block .price__normal::text").get().strip(),
#                     "link": f"{self.allowed_domains[0]}{product.css('a.area-link::attr(href)').get()}",
#                 }
#                 yield data
#                 writer.writerow([data["title"], data["price"]])



class OmaSpider(scrapy.Spider):
    name = "oma.by"
    allowed_domains = ["https://www.oma.by"]
    start_urls = ["https://www.oma.by/elektroinstrument-c"]

    def parse(self, response, **kwargs):
        for product in response.css(".catalog-grid .product-item"):
            data = {
                "title": product.css(".product-title-and-rate-block .wrapper::text").get().strip(),
                "price": product.css(".product-price-block .price__normal::text").get().strip(),
                "link": f"{self.allowed_domains[0]}{product.css('a.area-link::attr(href)').get()}",
            }

            #logger.debug(data)
            yield data