# -*- coding: utf-8 -*-

import json

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

class TencentPipeline(object):
	def __init__(self):
		self.filename = open("tencent.json","w")
	def process_item(self, item, spider):
		text = json.dums(dict(item),ensure_ascii = False) + "\n"
    	self.filename.write(text)
        return item
    
    # 可选方法,关闭管道文件close_spider
	def close_spider(self,spider):
    	self.filename.close()
