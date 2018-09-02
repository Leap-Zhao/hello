# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    '''
        要爬取的目标如下:
    	职位名		positionName
    	详情链接	positionLink
    	职位类别	positionType
    	招聘人数	peopleNum
    	工作地点	workLocation
    	发布时间	publishTime
	'''
    positionName = scrapy.Field()
    positionLink = scrapy.Field()
    positionType = scrapy.Field()
    peopleNum = scrapy.Field()
    workLocation = scrapy.Field()
    publishTime = scrapy.Field()