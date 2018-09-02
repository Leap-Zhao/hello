# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
from scrapy.conf import settings
import pymongo

class DoubanmoviePipeline(object):
    
    # 保存到当地json时用下面的代码 
    def __init__(self):
        self.filename = open("doubantop250.json","w")
        
    def process_item(self, item, spider):
        text = json.dumps(dict(item),ensure_ascii=False) + "\n"
        self.filename.write(text.encode("utf-8"))
        return item
    
    def close_spider(self,spider):
        self.filename.close()
    
    
    '''
    # 保存到mongodb数据库时用下面的代码
    def __init__(self):    
        # 1.从settings文件中获取mongodb相关数据
        mongodb_host = settings['MONGODB_HOST']
        mongodb_port = settings['MONGODB_PORT']
        mongodb_dbname = settings['MONGODB_DBNAME']
        mongodb_sheetname = settings['MONGODB_SHEETNAME']
        
        # 2.创建mongodb数据库连接
        client = pymongo.MongoClient(mongodb_host,mongodb_port)
        # 3.指定所用数据库
        mydatabase = client[mongodb_dbname]
        # 4.指定存放的表名
        self.sheet = mydatabase[mongodb_sheetname]
    
    def process_item(self,item,spider):
        data = dict(item)
        self.sheet.insert(data)
        return item
    '''   