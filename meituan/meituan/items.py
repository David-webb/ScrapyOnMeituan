# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MeituanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    pass


class MenuItem(scrapy.Item):
    title = scrapy.Field()
    murl = scrapy.Field()
    pass

class salersItem(scrapy.Item):
    name = scrapy.Field()
    position = scrapy.Field()
    lat_lons = scrapy.Field()
    telephone = scrapy.Field()
    CustomeJudge = scrapy.Field()
    pass