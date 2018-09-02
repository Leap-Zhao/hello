# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XinlangnewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    # 大类的名称和大类的url链接
    parentTypeName = scrapy.Field()
    parentTypeUrl = scrapy.Field()
    
    # 小类的名称和小类的url链接
    subTypeName = scrapy.Field()
    subTypeUrl = scrapy.Field()
    # 小类的目录存储路径
    subTypeFilePath = scrapy.Field()
    # 小类下文章的url链接
    articleUrl = scrapy.Field()
    # 文章的标题和内容
    articleTitle = scrapy.Field()
    articleContent = scrapy.Field()
    