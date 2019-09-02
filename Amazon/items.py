# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    location = scrapy.Field()
    tag = scrapy.Field()
    # price = scrapy.Field()
    # getitby = scrapy.Field()
    # stars = scrapy.Field()
    # image = scrapy.Field()
