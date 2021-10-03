import scrapy
import csv
from django.conf import settings
import logging

logger = logging.getLogger(__name__)


class AvitoSpider(scrapy.Spider):
    name = "kufar.by"
    allowed_domains = ["https://www.kufar.by"]
    start_urls = ["https://www.kufar.by/l/r~minsk/mobilnye-telefony?pb=5&phm=v.or:200&size=42&sort=lst.d&cur=BYR"]

    def parse(self, response, **kwargs):
        with open(settings.BASE_DIR / "posts_kufar.csv", "w") as file:
            writer = csv.writer(file)

            for product in response.css(".kf-quup-f974c"):
                data = {
                    "title": product.css(".kf-quHG-32a15::text").get().strip(),
                    "description": product.css(".kf-quue-8b13b::text").get().strip(),
                    "price": product.css(".kf-yNuN-4d8cb .kf-yNuS-2063e::text").get().strip(),


                    # "link": f"{self.allowed_domains[0]}{product.css('a.area-link::attr(href)').get()}",
                }
                yield data
                writer.writerow([data["title"], data['description'], data["price"]])