# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from elasticsearch import Elasticsearch, RequestsHttpConnection
import json
from boto3 import Session
from requests_aws4auth import AWS4Auth

host = "search-scrapest-brek4lku7p2upyxntfay6hctqi.us-east-1.es.amazonaws.com:443"


class ScrapePipeline(object):
    def __init__(self):
        # credentials = Session().get_credentials()
        # aws_auth = AWS4Auth(
        #     credentials.access_key,
        #     credentials.secret_key,
        #     "us-east-1",
        #     "es",
        #     session_token=credentials.token
        # )

        self.client = Elasticsearch(
            hosts=[host],
            use_ssl=True,
            verify_certs=True,
            # http_auth=aws_auth,
            connection_class=RequestsHttpConnection,
        )
        # self.client = Elasticsearch(
        #     ['https://search-scrapest-brek4lku7p2upyxntfay6hctqi.us-east-1.es.amazonaws.com:443'])

    def process_item(self, item, spider):
        self.client.index(index="articles", body=item.encode(), id=item['url'])
        return item
