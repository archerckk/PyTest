# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Test41104Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pic=scrapy.Field()
    title=scrapy.Field()
    price=scrapy.Field()
    url=scrapy.Field()
