# -*- coding: utf-8 -*-
import scrapy
from __builtin__ import str

from doubanmovie.items import DoubanmovieItem


class DoubanmoviespiderSpider(scrapy.Spider):
    name = 'doubanmoviespider'
    allowed_domains = ['movie.douban.com']
    url = "https://movie.douban.com/top250?start="
    offset = 0
    start_urls = [url + str(offset)]

#     def parse(self, response):   
#         movieList = response.xpath("//div[@class='info']")
# #         print(movieList.extract())
#         for movie in movieList:    
#             item = DoubanmovieItem() 
#               
#             item['movieName'] = response.xpath(".//span[@class='title'][1]/text()").extract()[0]
#             item['movieInfo'] = response.xpath(".//div[@class='bd']/p/text()").extract()[0].strip()
#             item['movieScore'] = response.xpath(".//div[@class='star']/span[2]/text()").extract()[0]
#             item['movieMsg'] = response.xpath(".//p[@class='quote']/span/text()").extract()[0]
#             print(item)
#             yield item
#         
#         if self.offset < 225:
#             self.offset += 25
#             yield scrapy.Request(self.url+str(self.offset),callback = self.parse)
            
    def parse(self, response):
            item = DoubanmovieItem()
            movies = response.xpath("//div[@class='info']")
    
            for each in movies:
                # 标题
                item['movieName'] = each.xpath(".//span[@class='title'][1]/text()").extract()[0]
                # 信息
                item['movieInfo'] = each.xpath("./div[@class='bd']/p/text()").extract()[0].strip()
                # 评分
                item['movieScore'] = each.xpath(".//div[@class='star']/span[@class='rating_num']/text()").extract()[0]
                # 简介
                quote = each.xpath(".//p[@class='quote']/span/text()").extract()
                if len(quote) != 0:
                    item['movieMsg'] = quote[0]
                yield item
    
            if self.offset < 225:
                self.offset += 25
                yield scrapy.Request(self.url + str(self.offset), callback = self.parse)
