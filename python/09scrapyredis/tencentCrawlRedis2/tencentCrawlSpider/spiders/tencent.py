# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule

# 导入scrapy-redis相关的包
from scrapy_redis.spiders import RedisCrawlSpider


from tencentCrawlSpider.items import TencentcrawlspiderItem


class TencentSpider(RedisCrawlSpider):
    name = 'tencent'
    
    # allowed_domains = ['tencent.com']
    # start_urls = ['https://hr.tencent.com/position.php?&start=0#a']

    # scrapy-redis相关的配置
    # redis_key
    redis_key = 'tencentspider:start_urls'
    # 动态域范围获取
    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(TencentSpider, self).__init__(*args, **kwargs)

    rules = (
        Rule(LinkExtractor(allow=r'&start=\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        for each in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
            item = TencentcrawlspiderItem()
            #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
            #i['name'] = response.xpath('//div[@id="name"]').extract()
            #i['description'] = response.xpath('//div[@id="description"]').extract()
            item['positionName'] = each.xpath("./td[1]/a/text()").extract()[0]
            item['positionLink'] = each.xpath("./td[1]/a/@href").extract()[0]
            item['positionType'] = each.xpath("./td[2]/text()").extract()[0]
            item['peopleNum'] = each.xpath("./td[3]/text()").extract()[0]
            item['workLocation'] = each.xpath("./td[4]/text()").extract()[0]
            item['publishTime']     = each.xpath("./td[5]/text()").extract()[0]
            yield item
