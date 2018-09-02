# -*- coding: utf-8 -*-
import scrapy
from myFirstScrapy.items import ItcastItem

# import sys
# reload(sys)
# sys.setdefaultencoding("utf-8")

class ItcastSpider(scrapy.Spider):
	name = "itcast"
	allowed_domains = ['http://www.itcast.cn']
	start_urls = [
		"http://www.itcast.cn/channel/teacher.shtml"
	]

	def parse(self,response):
		# 测试: 将爬取的页面存到一个文件中
		# with open("teacher.html","w") as f:
		# 	f.write(response.body)

		# 所有老师的信息列表集合
		# teacherItems = []

		# xpath解析
		teacher_list = response.xpath('//div[@class="li_txt"]')
		for teacher in teacher_list:
			# 创建item对象,保存数据
			item = ItcastItem()
			# xpath返回的都是SelectorList对象
			name = teacher.xpath('./h3/text()').extract()
			level = teacher.xpath('./h4/text()').extract()
			info = teacher.xpath('./p/text()').extract()
			# print name[0]
			# print title[0]
			# print info[0]
			item['name'] = name[0]
			item['level'] = level[0]
			item['info'] = info[0]

			# teacherItems.append(item)
			yield item
		
		# return teacherItems

		# 将数据生成json文件或者csv文件
		# scrapy crawl itcast -o itcast.json
		# scrapy crawl itcast -o itcast.csv
