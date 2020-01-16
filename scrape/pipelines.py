# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from elasticsearch import Elasticsearch
import json


class ScrapePipeline(object):
    def __init__(self):
        self.client = Elasticsearch([{'host': 'localhost', 'port': 9200}])

    def process_item(self, item, spider):
        self.client.index(index="articles", body=item.encode(), id=item['url'])
        return item
