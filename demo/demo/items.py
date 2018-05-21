# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DemoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    course_name=scrapy.Field()
    course_desc=scrapy.Field()
    course_price=scrapy.Field()
    course_students = scrapy.Field()