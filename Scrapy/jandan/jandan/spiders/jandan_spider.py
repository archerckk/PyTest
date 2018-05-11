import scrapy
from ..items import JandanItem

class Jandan_spider(scrapy.Spider):
    name='jandan'
    allowed_domains=['imooc.com']
    start_urls=[
        'https://www.imooc.com/course/list?c=test'
    ]

    def parse(self, response):
        filename=response.url.split('/')[-1]
        with open(filename,'wb')as f:
            f.write(response.body)