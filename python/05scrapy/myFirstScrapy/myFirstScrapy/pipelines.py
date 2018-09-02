# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class MyfirstscrapyPipeline(object):
#     def process_item(self, item, spider):
#         return item

import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class ItcastPipeline(object):
	def __init__(self):
		self.filename = open("itcast.json","w")

	def process_item(self,item,spider):
		jsontext = json.dumps(dict(item),ensure_ascii=False) + "\n"
		self.filename.write(jsontext)
		return item

	def close_spider(self,spider):
		self.filename.close()
