# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

# 设计管道文件
# 添加__init__方法
# 添加close_spider方法
class PracticePipeline(object):
    def __init__(self):
        self.filename = open("practice.json","w")
    def process_item(self, item, spider):
        text = json.dumps(dict(item),ensure_ascii = False) + "\n"
        self.filename.write(text)
        return item

    def close_spider(self,spider):
        self.filename.close()
