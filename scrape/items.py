# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapeItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    url = scrapy.Field()
    body = scrapy.Field()
    date = scrapy.Field()

    def encode(self):
        return {
            "title": self['title'],
            "body": self['body'],
            "date": self['date']
        }
