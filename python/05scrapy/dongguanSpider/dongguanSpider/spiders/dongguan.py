# -*- coding: utf-8 -*-
import scrapy

from dongguanSpider.items import DongguanspiderItem

class DongguanSpider(scrapy.Spider):
    name = 'dongguan'
    allowed_domains = ['wz.sun0769.com']
    url = "http://wz.sun0769.com/index.php/question/questionType?type=4&page="
    offset = 0
    start_urls = [url + str(offset)]

    def parse(self, response):
        linksList = response.xpath('//div[@class="greyframe"]/table//td/a[@class="news14"]/@href').extract()
        for link in linksList:
            yield scrapy.Request(link,callback = self.parse_item)
        
        if self.offset <= 88650:
            self.offset += 30
            yield scrapy.Request(self.url+str(self.offset),callback = self.parse)
            

    def parse_item(self,response):
        item = DongguanspiderItem()
        item['title'] = response.xpath("//div[@class='pagecenter p3']//strong/text()").extract()[0]
        item['titleId'] = item['title'].strip().split(" ")[-1].split(":")[-1]
        item['url'] = response.url
        contentext = response.xpath("//div[@class='contentext']/text()").extract()
        if len(contentext) != 0:
            item['content'] = "".join(contentext).strip()
        else:
            textList = response.xpath("//div[@class='c1 text14_2']/text()").extract()
            item['content'] = "".join(textList).strip()
             
        yield item

        
        