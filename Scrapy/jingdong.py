# -*- coding: utf-8 -*-
import scrapy
# from .test4_11_04.test4_11_04.items  import Test41104Item

"""
作业4：

使用scrapy完成作业2的需求。

jd_search(keyword,page_skip=1,page_limit=10) #抓1后面10页（包括第10页）的内容。
jd_search(keyword,page_skip=4,page_limit=3) #抓4后面3页（包括第6页）的内容。
"""
class JingdongSpider(scrapy.Spider):
    name = 'jingdong'
    allowed_domains = ['jingdong.com']

    target='https://search.jd.com/Search?keyword=%E8%B7%AF%E7%94%B1%E5%99%A8&enc=utf-8&qrst=1&rt=1&stop=1&vt=1&page=7&s=298&click=0'


    start_urls = ['http://search.jd.com/Search?keyword=%E5%B9%BC%E7%8C%AB%E7%8C%AB%E7%B2%AE&enc=utf-8#filter']

    def parse(self, response):
        sel=scrapy.selector.Selector(response)
        site=sel.xpath('//div[@class="gl-i-wrap"]')
        for i in site:
            item=dict()
            item['pic']=i.xpath('div/a/img/@source-data-lazy-img').extract()
            item['price']=i.xpath('div/strong/i/text()').extract()
            item['title']=i.xpath('div/a/em/text()').extract()
            item['url']=i.xpath("div[@class='p-name p-name-type-2']/a/@href").extract()

            yield item


