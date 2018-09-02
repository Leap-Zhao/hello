# -*- coding: utf-8 -*-
import scrapy
from tencent.items import TencentItem

# 爬取腾讯的招聘网站
# https://hr.tencent.com/position.php?&start=0
# https://hr.tencent.com/position.php?&start=10
# 换一页 start 增长10 
class TencentpositionSpider(scrapy.Spider):
    name = 'tencentPosition'
    allowed_domains = ['tencent.com']
    url = "https://hr.tencent.com/position.php?&start="

    offset = 0
    start_urls = [url + str(offset)]

    def parse(self, response):
        for each in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
        	# 初使化item对象
        	item = TencentItem()
        	# 
			item['positionName'] = each.xpath("./td[1]/a/text()").extract()[0]
			item['positionLink'] = each.xpath("./td[1]/a/@href").extract()[0]
			item['positionType'] = each.xpath("./td[2]/text()").extract()[0]
			item['peopleNum'] = each.xpath("./td[3]/text()").extract()[0]
			item['workLocation'] = each.xpath("./td[4]/text()").extract()[0]
			item['publishTime']	 = each.xpath("./td[5]/text()").extract()[0]

			# 将数据交给管道去处理
			yield item


		if self.offset < 3940:
			# 进行下一页的欲处理
			self.offset += 10

		# 每次处理完一页的数据之后,重新发送下一页的请求
		# 将请求重新发给调度器入队列,出队列,交给下载器下载
		yield scrapy.Request(url,callback = self.parse)
