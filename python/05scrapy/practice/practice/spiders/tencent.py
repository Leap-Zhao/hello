# -*- coding: utf-8 -*-
import scrapy
from practice.items import PracticeItem


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']

    offset = 0
    url = 'https://hr.tencent.com/position.php?&start='

    start_urls = [url + str(offset)]

    def parse(self, response):
        # 解析url
        for each in response.xpath('//tr[@class="even"] | //tr[@class="odd"]'):
            # 初使化item对象
            item = PracticeItem()
            item['positionName'] = each.xpath('./td[1]/a/text()').extract()[0] 
            positionType = each.xpath('./td[2]/text()').extract()
            if positionType:
                item['positionType'] = positionType[0]
            else:
                item['positionType'] = ""
            item['positionPeople'] = each.xpath('./td[3]/text()').extract()[0]
            item['positionLocation'] = each.xpath('./td[4]/text()').extract()[0]
            item['positionDate'] = each.xpath('./td[5]/text()').extract()[0]
            # 将数据交给管道去处理
            yield item

        # 循环完一个url地址后,将setoff+10,再次发送请求
        if self.offset <= 3860:
            self.offset +=10
        
        yield scrapy.Request(self.url+str(self.offset),callback=self.parse)
