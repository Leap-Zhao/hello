# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class XinlangnewsPipeline(object):
    def process_item(self, item, spider):
        
        articleUrl = item['articleUrl']
        articleTitle = item['articleTitle']
        
        if articleTitle != '':
            filename = articleTitle+".txt"
        else:
            # 文件名为文章url中间部分
            filename = articleUrl[-16:-6].replace('/','_') + '.txt'
        
        fp = open(item['subTypeFilePath']+'\\'+filename,'w')
        fp.write(item['articleContent'].encode('utf-8'))
        fp.close()
        return item
    
