# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# 编写要抓取的目标
# http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset=
class DouyuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    nickname = scrapy.Field()
    imagelink = scrapy.Field()
    imagepath = scrapy.Field()
