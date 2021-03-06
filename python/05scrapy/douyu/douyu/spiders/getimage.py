# -*- coding: utf-8 -*-
import scrapy
import json
from douyu.items import DouyuItem

# 编写爬虫
class GetimageSpider(scrapy.Spider):
    name = 'getimage'
    allowed_domains = ['capi.douyucdn.cn']
    url = "http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset="
    offset = 0
    start_urls = [url + str(offset)]

    def parse(self, response):
        jsonDict = json.loads(response.text)
        infoDictList = jsonDict['data']
        for infoDict in infoDictList:
            item = DouyuItem()
            item['nickname'] = infoDict['nickname']
            item['imagelink'] = infoDict['vertical_src']
            
            yield item
        
        self.offset += 20
        yield scrapy.Request(self.url+str(self.offset),callback=self.parse)