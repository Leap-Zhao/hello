#coding=utf-8

import urllib2
import urllib
import os 
import cookielib
import re
from lxml import etree

'''
案例1:获取环境变量(system environment variables)
'''
'''
variableValue = os.environ.get("variableName")
print(variableValue)
'''




'''
案例2:通过免费的代理ip来爬取html页面
'''
# 1.定义代理开关
# 2.构建一个指定ip的代理处理器与默认的代理处理器
# 3.通过if判断用哪个代理处理器
# 4.通过代理处理器构建一个opener
# 5.通过install_opener方法将opener构建为全局的opener,之后所有请求都可用urlopen()方法去发送
# 6.用urlopen()方法去发送请求
'''
proxyswitch = False
myProxyHandler = urllib2.ProxyHandler({"http":"192.168.0.1:80"})
defaultProxyHandler = urllib2.ProxyHandler({})

if proxyswitch:
	opener = urllib2.build_opener(myProxyHandler)
else:
	opener = urllib2.build_opener(defaultProxyHandler)
urllib2.install_opener(opener)
url = "http://www.baidu.com"
request = urllib2.Request(url)
response = opener.open(request)
print(response.read())
'''




'''
案例3.1:用自己的私有的ip做代理去爬取页面(不带封装版)
===================================================
了解即可
'''

# 1.定义一个有私有ip账号与密码的代理处理器
# 2.生成一个opener
# 3.生成请求对象request
# 4.发送请求

'''
proxyHandler = urllib2.ProxyHandler({"http":"username:pwd@192.168.1.1:8088"})

opener = urllib2.build_opener(proxyhandler)

request = urllib2.Reuqest("www.baidu.com")

response = opener.open(request)

print(response.read())
'''





'''
案例3.2:用自己的私有的ip做代理去爬取页面(带封装版)
'''
# 1.获取私有ip的账号与密码(定义在环境变量中)
# 2.定义一个带有账号密码的代理处理器
# 3.根据代理处理器生成一个opener
# 4.生成HTTPRequest
# 5.opener.open发送请求,返回http response

'''
proxyuserValue = os.environ.get("proxyuser")
proxypwdValue = os.environ.get("proxypwd")

authProxyHandler = urllib2.proxyHandler({"http" : proxyuserValue+":"+proxypwdValue+"@192.168.1.1:80"})
opener = urllib2.bulid_opener(authProxyHandler)
request = urllib2.Request("http://www.baidu.com")
response = opener.open(request)
print(response.read())
'''





'''
案例4:用CookieJar类保存Cookie,登陆进入人人网http://www.renren.com/PLogin.do
'''
# 1.通过Cookielib模块构建一个CookieJar()类对象,用来保存Cookie的值
# 2.通过HTTPCookieProcessor()处理器构建一个处理器对象,用来处理Cookie
# 3.根据Cookie处理器对象构建一个opener
# 4.构建一个Request请求对象(包括人人网登录的用户名和密码,并进行转码)
# 5.发送Request请求,返回响应
# 6.再次发送请求,请求需要登录才能访问的页面,返回响应

'''
cookie = cookielib.CookieJar()
cookie_handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.bulid_opener(cookie_handler)

url = "http://www.renren.com/PLogin.do"
# 要据html表单的标签名
data = {"email":"username","password":"123456"}
# 通过urlencode()进行编码转换
data = urllib.urlencode(data)
renrenHeaders = {
	"User-Agent":"",
	"Connection":"keep-alive"
}
# 带data的请求为post请求
request = urllib2.Request(url,data=data,headers=renrenHeaders)
response = opener.open(request)
print(resopnse.read())
# 第二次发送请求
cookie_response = opener.open("http://www.renren.com/410043129/profile")
print(cookie_response.read())
'''







'''
案例5:通过授权验证的方式进入某一服务器
=====================================
了解即可,不常用
'''
# 1.构建一个密码管理对象,可以用来保存和HTTP请求相关的授权账户信息
# 2.添加授权账户信息
# 3.构建HTTP基础验证处理器类HTTPBasicAuthHandler
# 4.构建代理处理基础验证相关的处理器类ProxyBasicAuthHandler
# 5.通过HTTP基础验证处理器类和代理处理基础验证处理器类构建自定义opener
# 6.生成http请求
# 7.用授权验证信息处理http请求,生成响应对象







'''
案例6:用正则表达式爬取内涵段子的段子内容,并输出到文本
'''
# 1.定义Spider类
# 2.初使化属性:起始页,爬取开关
# 3.定义方法
#  3.1 loadPage
#  3.2 dealPage
#  3.3 writePage
#  3.4 startWork

class NeihanduanziSpider(object):
	"""docstring for Spider"""
	def __init__(self, startPage):
		super(Spider, self).__init__()
		self.startPage = startPage
		self.switch = True # 定义开关

	def loadPage(self):
		"""
		加载html页面
		"""
		print("正在加载页面...")
		url = "http://www.neihanpa.com/article/list_5_" + str(self.startPage) + ".html"
		headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

		request = urllib2.Request(url,headers = headers)
		response = urllib2.urlopen(request)
		html = response.read()
		# print(html)
		# 用正则匹配内涵段子的内容
		pattern = re.compile('<div\sclass="f18 mb20">(.*?)</div>',re.S)
		# 将正则匹配对象应用到html源码字符串里,返回这个字符串里所有段子的列表
		content_list = pattern.findall(html)
		# 用dealPath处理段子里的标签
		# for duanzi in content_list:
		# 	print(duanzi)
		self.dealPage(content_list)

	def dealPage(self,contentList):
		for duanzi in contentList:
			duanzi = duanzi.replace("<p>","").replace("</p>","").replace("<br>","").replace("<br />", "").replace("&ldquo", "").replace("&rdquo", "")
			# 进行编码转换
			# print(duanzi)
			# print(duanzi.decode("gbk"))
			# 处理完后调用写入文件
			self.writePage(duanzi)

	def writePage(self,item):
		"""
		"""
		print("正在将段子写入文件...")
		with open("duanzi.txt","a") as f:
			f.write(item)
		
	def startWork(self):
		"""控制爬虫运行"""
		while self.switch:
			self.loadPage()
			command = raw_input("如果继续爬取,请按回车(退出输入quit): ")
			if command == "quit":
				self.switch = False
			self.startPage += 1
		print("谢谢使用")



'''
案例7:用lxml解析网页元素,爬取贴吧中的图片
'''
class BaiduTiebaImageSpider(object):
	"""docstring for BaiduTiebaImageSpider"""
	def __init__(self):
		super(BaiduTiebaImageSpider, self).__init__()
		self.tiebaName = raw_input("请输入要爬取的贴吧名: ")
		self.startPage = int(raw_input("请输入起始页: "))
		self.endPage = int(raw_input("请输入结束页: "))

	def loadPage(self,url):
		headers = {
			"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
		}
		request = urllib2.Request(url,headers = headers)
		response = urllib2.urlopen(request)
		tiebaHomehtml = response.read()
		print("正在加载页面...")
		# 从页面的html中用lxml解析出帖子的link
		tiebaHomehtmlDom = etree.HTML(tiebaHomehtml)
		# 为何此处匹配为空,返回空列表
		tiezi_link_list = tiebaHomehtmlDom.xpath('//div[@class="t_con cleafix"]/div//a/@href')
		print(tiezi_link_list)
		for tiezi in tiezi_link_list:
			tieziLink = "http://tieba.baidu.com" + tiezi
			print(tieziLink)
			self.loadImage(tieziLink)

		# print(tiebaHomehtml)

	def loadImage(self,tiezi_link):
		headers = {
			"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
		}
		request = urllib2.Request(tiezi_link,headers=headers)
		tieziHtml = urllib2.urlopen(request).read()
		# 解析
		tieziHtmlDom = etree.HTML(tieziHtml)
		image_link_list = tieziHtmlDom.xpath('//img[@class="BDE_Image"]/@src')
		for image_link in image_link_list:
			print("图片地址为 %s" % iamge_link)
			writeFile(image_link)

	def writeFile(self,image_link):
		headers = {
			"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
		}
		request = urllib2.Request(image_link,headers = headers)
		image = urllib2.urlopen(request).read()
		filename = image_link[-10:]
		with open(filename,"wb") as f:
			f.write(image)
		print("成功下载图片 %s" % filename)

	def startWork(self):
		kw = {
			"kw":self.tiebaName
		}
		tieba = urllib.urlencode(kw)
		url = "http://tieba.baidu.com/f?" + tieba
		for page in range(self.startPage,self.endPage+1):
			pn = str((page-1)*50)
			fullurl = url + "&pn=" + pn
			print(fullurl)
			self.loadPage(fullurl)

		

if __name__ == '__main__':
	# duanzi = NeihanduanziSpider(1)
	# duanzi.startWork()
	tieba = BaiduTiebaImageSpider()
	tieba.startWork()