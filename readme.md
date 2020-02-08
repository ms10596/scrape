# Scrapest
scraping engine that is contenraized and deployed in a kubernetes cluster. It scrapes and sends articles to an elasticsearch instance in the cloud.

## Main Blocks
1. __scraper__: a python program built on the SCRAPY framework. It consists of several spiders that are invoked using a post request.
2. __elasticsearch__: t3.micro instance of elastic search that presents in AWS cloud service.

