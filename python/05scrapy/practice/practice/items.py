# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PracticeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	
	# 定义要爬取的目标
	positionName = scrapy.Field()
	positionType = scrapy.Field()
	positionPeople = scrapy.Field()
	positionLocation = scrapy.Field()
	positionDate = scrapy.Field()