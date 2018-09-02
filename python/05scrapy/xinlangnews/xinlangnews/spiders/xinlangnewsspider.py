# -*- coding: utf-8 -*-
import scrapy

from xinlangnews.items import XinlangnewsItem
import os

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class XinlangnewsspiderSpider(scrapy.Spider):
    name = 'xinlangnewsspider'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://news.sina.com.cn/guide/']

    def parse(self, response):
        allTypeItemsList = []
        # 获取所有大类名称和url,以列表形式呈现
        parentTypeNameList = response.xpath(r'//div[@id="tab01"]/div/h3/a/text()').extract()
        parentTypeUrlList = response.xpath(r'//div[@id="tab01"]/div/h3/a/@href').extract()
        # 获取所有小类名称和url,以列表形式呈现
        subTypeNameList = response.xpath(r'//div[@id="tab01"]/div/ul/li/a/text()').extract()
        subTypeUrlList = response.xpath(r'//div[@id="tab01"]/div/ul/li/a/@href').extract()
        
        # 按大类的个数循环处理
        for i in range(0,len(parentTypeNameList)):
            parentTypeName = parentTypeNameList[i]
            parentTypeUrl = parentTypeUrlList[i]
            # 指定大类目录的路径和目录名
            parentTypeFilePath = ".\\data\\" + parentTypeName
            # 如果不存在,则创建目录
            if( not os.path.exists(parentTypeFilePath)):
                os.makedirs(parentTypeFilePath)
            
            # 创建目录之后,处理小类
            for j in range(0,len(subTypeUrlList)):
                # 上面一句循环了所有的小类,要找出同一个大类下的小类
                if_belong = subTypeUrlList[j].startswith(parentTypeUrl)
                # 当小类属于此大类下时
                if(if_belong):
                    # 指定小类目录的路径和目录名
                    subTypeFilePath = parentTypeFilePath + "\\" + subTypeNameList[j]
                    # 如果不存在,则创建目录
                    if(not os.path.exists(subTypeFilePath)):
                        os.makedirs(subTypeFilePath)
                    
                    # 创建item并添加到allTypeItemsList列表中
                    item = XinlangnewsItem()     
                    item['parentTypeName'] = parentTypeName
                    item['parentTypeUrl'] = parentTypeUrl
                    item['subTypeName'] = subTypeNameList[j]
                    item['subTypeUrl'] = subTypeUrlList[j]    
                    item['subTypeFilePath'] = subTypeFilePath
                    allTypeItemsList.append(item)
                    
        # 发送每个小类url的Request请求,得到Response连同包含meta数据一同交给回调函数article_parse处理
        for typeItem in allTypeItemsList:
            yield scrapy.Request(url=typeItem['subTypeUrl'],meta={'meta_1':typeItem},callback=self.subtype_parse)
    
    def subtype_parse(self,response):
        # 提取每次Response的meta数据
        meta_1 = response.meta['meta_1']
        # 取出小类里所有的文章链接,生成文章链接列表
        articleUrlList = response.xpath(r'//a/@href').extract()
        
        articleItemsList = []
        for articleUrl in articleUrlList:
            # 检查每个链接是否以大类url开头,以.shtml结尾
            is_belong = articleUrl.endswith('.shtml') and articleUrl.startswith(meta_1['parentTypeUrl'])
            
            if(is_belong):
                item = XinlangnewsItem()
                item['parentTypeName'] = meta_1['parentTypeName']
                item['parentTypeUrl'] = meta_1['parentTypeUrl']
                item['subTypeName'] = meta_1['subTypeName']
                item['subTypeUrl'] = meta_1['subTypeUrl'] 
                item['subTypeFilePath'] = meta_1['subTypeFilePath']
                item['articleUrl'] = articleUrl
                articleItemsList.append(item)
        
        for articleItem in articleItemsList:
            yield scrapy.Request(url=articleItem['articleUrl'],meta={"meta_2":articleItem},callback=self.article_parse)
        
    def article_parse(self,response):       
        articleItem = response.meta['meta_2']
        articleTitle = ''
        articleTitleList = response.xpath(r"//h1[@class='main-title']/text()").extract()
        if articleTitleList != []:
            articleTitle = articleTitleList[0]
        else:
            articleTitleList = response.xpath(r"//h1[@id='artibodyTitle']/text()").extract()
            if articleTitleList != []:
                articleTitle = articleTitleList[0]
          
        articleContentList = response.xpath(r'//div[@id="artibody"]/p/text()').extract()
        
        articleContent = "标题: " + articleTitle + "\n"
        for articleContentPart in articleContentList:
            articleContent += articleContentPart
            
        articleItem['articleTitle'] = articleTitle
        articleItem['articleContent'] = articleContent
        
        yield articleItem
        
        
        
        
        
