#coding=utf-8

import urllib
import urllib2
from lxml import etree
import re
import sys



reload(sys)
sys.setdefaultencoding("utf-8")
# 数据分为: 结构性数据(json,xml) 与 非结构性数据(文本,html文件)


'''
正则表达式:re模块
# 1.通过正则表达式获得Pattern对象
pattern = re.compile('reStr')

# 2.1 通过Pattern对象去匹配出一个,返回Match对象
match = pattern.match(str)
match = pattern.search(str)
# 2.2 通过Pattern对象去匹配出多个
pattern.findall(str)  返回列表
pattern.finditer(str)	返回callable对象
# 2.3 通过Pattern对象去分割/替换
pattern.split()  返回列表
pattern.sub() 返回字符串

# 3 通过Match对象去执行进一步操作
match.group()
match.span()
'''

'''
案例1:爬取内涵段子某一页的段子内容
说明: 使用正则表达式 re模块
url:http://neihanshequ.com/
'''

'''
def loadUrl(url):
	headers = {
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
	}
	request = urllib2.Request(url,headers=headers)
	return urllib2.urlopen(request).read()

def parseHtml(html):
	pattern = re.compile(r'<h1.*?class="title">(.*?)</h1>',re.S)
	textList = pattern.findall(html)
	# print(textList)
	for text in textList:
		text = text.replace('<p>','').replace('</p>', '')
		loadToFile(text)
	print("文件写入完成")

def loadToFile(text):
	with open('./duanzi.txt','a') as f:
		f.write(text)

if __name__ == '__main__':
	url = "http://neihanshequ.com/"
	html = loadUrl(url)
	parseHtml(html)
'''






'''
xpath解析: 用lxml模块中的etree模块
# 1 读取html或xml的字符串或者文件
html = etree.HTML(text) 读取字符串
html = etree.parse('./hello.html') 读取外部文件
# 2 用xpath解析获取的文本,得到元素列表
result = html.xpath('//li')
# 3 解析得到的列表
如果得到的是Element元素列表 则result[0].text 或result[0].tag 得到标签名或文本内容
如果得到的是str列表,则直接result[0]即可
'''


def pracEtree():
	# 下面的text缺少了一个</li>标签
	text = '''
	<div>
	    <ul>
	         <li class="item-0"><a href="link1.html">first item</a></li>
	         <li class="item-1"><a href="link2.html">second item</a></li>
	         <li class="item-inactive"><a href="link3.html">third item</a></li>
	         <li class="item-1"><a href="link4.html">fourth item</a></li>
	         <li class="item-0"><a href="link5.html">fifth item</a>
	     </ul>
	 </div>
	'''

	# 用etree的HTML方法将字符串解析为HTML文档
	html = etree.HTML(text)
	# 按字符串序列化HTML文档,可以自动补全
	result = etree.tostring(html)
	result2 = html.xpath('//li')
	print(type(result)) # str
	print(type(result2)) # list
	print(result)
	print(result2) # 5个Element对象的列表


'''
案例2:用xpath爬取某贴吧帖子里的图片
url: 
说明: 对day1里的案例3进行修改即可,添加对图片的xpath解析
'''
def parseUrl(url):
	request_headers = {
		"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
	}
	request = urllib2.Request(url)
	return urllib2.urlopen(request).read()

def loadToFile(filename,imageHtml):
	with open('./tiebaImage/' + filename,"wb") as f:
		print("生成文件:" + filename)
		f.write(imageHtml)
	

def parseImage(url):
	print("正在解析%s" % url)
	html = parseUrl(url)
	tieziHtml = etree.HTML(html)
	imageUrlList = tieziHtml.xpath('//img[@class="BDE_Image"]/@src')
	for imageUrl in imageUrlList:
		imageHtml = parseUrl(imageUrl)
		imagefileName = imageUrl[imageUrl.rfind('/')+1:]
		# print(imagefileName,imageHtml)
		loadToFile(imagefileName,imageHtml)

def loadPage(url):
	print("正在解析%s" % url)
	html = parseUrl(url)
	# 获取html的文档对象
	content = etree.HTML(html)
	# print(content)
	link_list = content.xpath('//div[@class="t_con cleafix"]/div/div/div/a/@href')
	# 通过文档对象获取每个帖子的
	# tieziUrlList = content.xpath("//div[@id='content_wrap']")
	# print link_list
	for tieziUrl in link_list:
		tieziLink = "https://tieba.baidu.com" + tieziUrl
		# print(tieziLink)
		parseImage(tieziLink)

	# for imageSrc in imageSrcList:
	# 	loadToFile(imageSrc)

def parseTieBa(tiebaName):
	kw = urllib.urlencode({"kw":tiebaName})
	for page in range(1,2):
		pn = str((page-1)*50)
		url = "https://tieba.baidu.com/f?" + kw + "&pn=" + pn
		loadPage(url)
		# loadToFile(html,page)


if __name__ == '__main__':
	tiebaName = raw_input("输入你要获取的贴吧名:")
	parseTieBa(tiebaName)
	print("完成")






