# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from dongguan.items import DongguanItem


class DongguansunSpider(CrawlSpider):
    name = 'dongguansun'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=0']
    
    # 每一页的其它页面链接列表
    pageLinks = LinkExtractor(allow=r'type=4&page=\d+')
    # 每一页的贴子的链接列表
    postLinks = LinkExtractor(allow=r'/html/question/\d+/\d+.shtml')
    
    rules = (
        Rule(pageLinks, follow=True),
        Rule(postLinks, callback='parse_item',follow=False),
    )

    

    def parse_item(self, response):
#         print response.url
        item = DongguanItem()
        item['title'] = response.xpath("//div[@class='pagecenter p3']//strong/text()").extract()[0]
        item['titleId'] = item['title'].strip().split(" ")[-1].split(":")[-1]
        # 如果是有图片时,存在class为contentext的div
        contentext = response.xpath("//div[@class='contentext']/text()").extract()
        if len(contentext) == 0:
            # 没有图片
            contentext = response.xpath("//div[@class='c1 text14_2']/text()").extract()
            item['content'] = ''.join(contentext).strip()
        else:
            # 有图片
            item['content'] = ''.join(contentext).strip()
        item['url'] = response.url
        
        yield item
        
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
#         return i
