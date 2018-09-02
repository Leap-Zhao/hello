# -*- coding: utf-8 -*-
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.project import get_project_settings
import scrapy
import os

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# 处理管道图片的类ImagesPipeline
class DouyuPipeline(ImagesPipeline):
    # 获取settings.py文件里的图片保存路径
    image_store = get_project_settings().get("IMAGES_STORE")
    def get_media_requests(self, item, info):
        # 获得图片的url
        image_url = item['imagelink']
        # 向管道发送请求
        yield scrapy.Request(image_url)
    
    def item_completed(self, results, item, info):
        # 获取图片路径
        image_path = [x['path'] for ok,x in results if ok ]
        # 重命名图片
        os.rename(self.image_store + "\\" + image_path[0], self.image_store + "\\" + item['nickname'] + '.jpg')
        # 设置item的imagepath值
        item['imagepath']  = self.image_store + "\\" + item['nickname']
        
        return item
        
    
    
#     def process_item(self, item, spider):
#         return item
