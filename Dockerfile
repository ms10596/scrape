FROM python:3
COPY . .
RUN pip install -r requirements.txt
CMD ["scrapy", "crawl", "youm7"]


