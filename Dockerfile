FROM python:3c
COPY . .
RUN pip install -r requirements.txt
CMD ["scrapy", "crawl", "youm7"]


