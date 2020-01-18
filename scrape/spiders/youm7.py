import scrapy
from ..items import ScrapeItem
import datetime
import time


class Youm7(scrapy.Spider):
    name = "youm7"
    start_urls = ['http://www.youm7.com/'+str(i) for i in range(4589153, 4589153 - 1, -1)]

    def parse(self, response):
        new_item = ScrapeItem()
        new_item['title'] = self.get_title(response)
        new_item['url'] = response.request.url
        new_item['body'] = self.get_body(response)
        new_item['date'] = self.get_date(response)
        yield new_item

    @staticmethod
    def get_title(response):
        data = response.css("h1::text").extract()[0].strip()

        return data

    @staticmethod
    def get_body(response):
        dirty_body = " ".join([i.strip() for i in response.css("""div#articleBody>*::text""").extract()]).strip()
        return dirty_body

    @staticmethod
    def get_date(response):
        pieces = response.request.url.split("/")
        return datetime.datetime(int(pieces[4]), int(pieces[5]), int(pieces[6])).date()
