import scrapy
# import os
from ..items  import DemoItem

class DemoSpider(scrapy.Spider):
    name='demo'
    allowed_domains='imooc.com'
    start_urls=[
        'https://www.imooc.com/course/list?c=linux',
        'https://www.imooc.com/course/list?c=test'
           ]

    def parse(self, response):
        sel=scrapy.selector.Selector(response)
        site=sel.xpath('//div[@class="course-card-content"]')
        item_list=[]
        for i in site:
            item=DemoItem()
            item['course_name']=i.xpath('h3/text()').extract()
            item['course_desc'] = i.xpath('div/p/text()').extract()
            item['course_students'] = i.xpath('div/div/span/text()').extract()
            item_list.append(item)

        return item_list
