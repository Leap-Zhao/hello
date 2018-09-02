#!/usr/bin/env python
#coding=utf-8



import urllib2
import requests
import time

import json
import jsonpath
import chardet
from lxml import etree

import unittest
from bs4 import BeautifulSoup

from Queue import Queue
import threading
import sys

import pytesseract
from PIL import Image



# 导入webdriver
from selenium import webdriver
# 要想调用键盘操作需引入keys包
from selenium.webdriver.common.keys import Keys


reload(sys)
sys.setdefaultencoding('utf-8')

def openlink(url,headers):
	maxNum = 5
	for num in range(maxNum):
		try:
			request = urllib2.Request(url,headers = headers)
			response = urllib2.urlopen(request)
			return response
		except:
			if num < maxNum:
				continue
			else:
				print("Has tried %d times to access url %s, all failed" % (maxNum,url))
				break
				



'''
案例1:登录知乎
'''
'''
def zhihuLogin():
	# 构建一个Session对象,可以保存Cookie
	session = requests.Session()
	# 请求头
	headers = {
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
	}

	# 获取登录页面
	html = session.get(r"https://www.zhihu.com/signup?next=%2F",headers = headers).text
	print(html)
'''


'''
案例2: 以拉勾网城市JSON文件 http://www.lagou.com/lbs/getAllCitySearchLabels.json 为例，获取所有城市
'''
'''
url = "http://www.lagou.com/lbs/getAllCitySearchLabels.json"
request = urllib2.Request(url)
html = urllib2.urlopen(request).read()
# 获取的html为json格式,将其转化为unicode编码的python字符串对象
unicodeStr = json.loads(html)
# 匹配其中的name节点
cityList = jsonpath.jsonpath(unicodeStr, '$..name')
# 将city的python列表转化为json格式,dumps默认用ascii编码,ensure_ascii=False后用utf8编码
content = json.dumps(cityList,ensure_ascii=False)
# print输出内容时自动编码为utf8,所以不用写encode("utf-8")
print content
# 将内容保存到city.json文件中
with open("city.json","w") as f:
	# content内容为utf8编码,所以在写入文件时要加上encode("utf-8")
	f.write(content.encode("utf-8"))
print("output finished")
'''

# 注:encode就是把unicode转换成任意编码格式,decode就是把其它编码格式转换成unicode





'''
案例3: 用json与jsonpath 爬取糗事百科段子
url:   http://www.qiushibaike.com/8hr/page/1
'''
'''
url = "http://www.qiushibaike.com/8hr/page/1"
headers = {
	"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"
}

response = openlink(url, headers)
qiushihtml = response.read()

# 将返回的html解析为htmlDom,用etree.HTML
qiushihtmlDom = etree.HTML(qiushihtml)
# 解析htmlDom,用xpath的模糊查询
nodeList = qiushihtmlDom.xpath('//div[contains(@id,"qiushi_tag")]')

items = {}

for node in nodeList : 
	# xpath返回列用,这个列表就这一个参数,用索引方式取出来用户名
	content = node.xpath('.//div[@class="content"]/span')[0].text
	username = node.xpath('./div//h2')[0].text
	image = node.xpath('./div//img/@src')
	haoxiao = node.xpath('.//span[@class="stats-vote"]/i')[0].text
	items["username"] = username
	items["content"] = content
	items["image"] = image
	items["haoxiao"] = haoxiao
	with open("qiushi2.json","a") as f:
		f.write(json.dumps(items,ensure_ascii=False).encode("utf-8") + "\n")
'''








'''
案例4: 多线程+json+jsonpath爬取糗事百科段子
'''



'''
# 爬取网页的线程类
class ThreadCrawl(threading.Thread):
	"""采集线程的类ThreadCrawl"""
	def __init__(self, threadName,pageQueue,dataQueue):
		super(ThreadCrawl, self).__init__()
		self.threadName = threadName
		self.pageQueue = pageQueue
		self.dataQueue = dataQueue
		self.headers = {
			"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"
		}

	def run(self):
		print("启动%s" % self.threadName)
		# pageQueue为空时
		while not CRAWL_EXIT:
			try:
				# 从pageQueue中取出页码,先进先出
				# Queue可选参数block,默认为true
				# 1.如果队列为空,block为True时,不会结束,会进入阻塞状态,直到队列有新的数据
				# 2.如果队列为空,block为False时,就弹出一个Queue.empty异常
				page = self.pageQueue.get(False)
				# 从url取出html
				url = "http://www.qiushibaike.com/8hr/page/" + str(page) + "/"
				print(url)
				content = requests.get(url,headers= self.headers).text
				time.sleep(1)
				# 将页面的html放入源代码队列
				self.dataQueue.put(content)
			except:
				pass
		print("结束%s" % self.threadName)


# 解析网页内容的线程类
class ThreadParse(threading.Thread):
	def __init__(self,threadName,dataQueue,filename,lock):
		super(ThreadParse, self).__init__()
		self.threadName = threadName
		self.dataQueue = dataQueue
		self.filename = filename
		self.lock = lock

	def run(self):
		print("启动%s" % self.threadName)
		while not PARSE_EXIT:
			try:
				html = self.dataQueue.get(False)
				self.parse(html)
			except:
				pass
		print("退出%s" % self.threadName)

	def parse(self,html):
		html = etree.HTML(html)
		node_list = html.xpath('//div[contains(@id,"qiushi_tag")]')
		
		for node in node_list:
			content = node.xpath('.//div[@class="content"]/span')[0].text
			username = node.xpath('./div//h2')[0].text
			image = node.xpath('./div//img/@src')
			haoxiao = node.xpath('.//span[@class="stats-vote"]/i')[0].text
			print(username)
			items = {}
			items["username"] = username
			items["content"] = content
			items["image"] = image
			items["haoxiao"] = haoxiao

            # with 后面有两个必须执行的操作：__enter__ 和 _exit__
            # 不管里面的操作结果如何，都会执行打开、关闭
            # 打开锁、处理内容、释放锁
			with self.lock:
				print("写入文件")
				self.filename.write(json.dumps(items,ensure_ascii=False).encode("utf-8") + "\n")

CRAWL_EXIT = False
PARSE_EXIT = False

def main():
	# 页码的队列
	pageQueue = Queue(10)
	# 放入1-10的页码
	for i in range(1,11):
		pageQueue.put(i)
	# 采集结果(每页html源码)的数据队列,参数为空表示不限制
	dataQueue = Queue()

	# 解析的内容放置的文件
	filename = open("duanzi.json","a")

	# 创建锁
	lock = threading.Lock()

	# 三个采集线程的名字
	crawlList = ['thread-1','thread-2','thread-3']
	# 存储三个采集线程的列表集合
	threadcrawl = []
	for threadName in crawlList:
		thread = ThreadCrawl(threadName,pageQueue,dataQueue)
		thread.start()
		threadcrawl.append(thread)

	# 解析线程名称列表
	threadParseNameList = ['thread-parse-1','thread-parse-2','thread-parse-3']
	# 存储三个解析线程的列表
	threadParseList = []
	for threadParseName in threadParseNameList:
		thread = ThreadParse(threadParseName,dataQueue,filename,lock)
		thread.start()
		threadParseList.append(thread)

	# 等待pageQueue队列为空,也就是等待之前的操作执行完毕
	# pageQueue为空时,empty返回true,循环条件为false,跳出循环,否则主程序一直循环下去
	while not pageQueue.empty():
		pass

	# pageQueue为空后,将CRAW_EXIT设为True,这样爬取网页的子线程就可以跳出循环
	global CRAWL_EXIT
	CRAWL_EXIT = True

	print("pageQueue为空")

	# 爬取的子线程用join方法等待主线程执行完毕
	for thread in threadcrawl:
		thread.join()
		print("1")

	# 等待dataQueue为空,dataQueue为空时说明html页面源码已经全被解析
	while not dataQueue.empty():
		pass
	# dataQueue为空后,将PARSE_EXIT设为空,这样解析网页的子线程就可以跳出循环
	global PARSE_EXIT
	PARSE_EXIT = True

	print("dataQueue为空")

	#解析的子线程用join方法等待主线程执行完毕
	for thread in threadParseList:
		thread.join()
		print("2")


	with lock:
		#关闭文件
		filename.close()

	print("谢谢使用")



if __name__ == '__main__':
	main()
'''







'''
案例4:练习使用selenium和PhantomJs(headless浏览器)
'''

'''
# 调用环境就量指定的PhantomJS浏览器创建浏览器对象
driver = webdriver.PhantomJS()

# get方法会一直等到页面被完全加载,然后才会继续程序,通常测试会在这里选择 time.sleep(2)
driver.get("http://www.baidu.com")

# # 获取页面名为wrapper的id标签的文本内容
# data  = driver.find_element_by_id("wrapper").text
# print(data)
# # 打印页面标题,"百度一下,你就知道"
# print(driver.title)
# # 生成当前页面快照并保存
# driver.save_screenshot("baidu.png")

# id="kw"是百度看过输入框,输入字符器"长城"
driver.find_element_by_id("kw").send_keys(u"长城")
# id="su"是百度搜索按钮,click()是模拟点击
driver.find_element_by_id("su").click()
# 获取新的页面快照
driver.save_screenshot("changcheng.png")

# 退出浏览器
driver.quit()

'''



'''
案例5:用selenium与PhantomJs登录豆瓣
url: https://www.douban.com/
'''

'''
driver = webdriver.PhantomJS()
# 加载页面
driver.get("https://www.douban.com/")
#获取用户名和密码登录框
driver.find_element_by_id("form_email").send_keys("zhaofeiyue1234@163.com")
driver.find_element_by_id("form_password").send_keys("baoaiyue1314")
#点击登录按钮
driver.find_elements_by_class_name("bn-submit")[0].click()

#等待2秒,登录完成
time.sleep(2)

# 生成快照
driver.save_screenshot("douban.png")

# 将源码保存
with open("douban.html","w") as f:
	f.write(driver.page_source)

# 退出浏览器
driver.quit()
'''



'''
案例6:爬取斗鱼直播的所有房间名与直播观看人数 (有问题,运行不成功)
说明: 有些动态页面点击后,url不变,适用于此种方式,斗鱼的直播点击下一页URL不变
所用技术:bs4解析,unittest测试,selenium,PhantomJS
url:https://www.douyu.com/directory/all
'''

'''
class douyu(unittest.TestCase):
	# 初使化方法
	def setUp(self):
		self.driver = webdriver.PhantomJS()
		print("1")

	# 具体的测试方法,一定要以test开头
	def testDouyu(self):
		self.driver.get("https://www.douyu.com/directory/all")
		print("开始获取")
		while True:
			# 指定xml解析
			soup = BeautifulSoup(self.driver.page_source,'lxml')
			# 返回当前页面所有房间标题列表和观众人数
			titles = soup.find_all('h3',{'class':'ellipsis'})
			nums = soup.find_all('span',{'class':'dy-num fr'})

			# 使用zip函数把两个列表合并,并组建一个元组对的列表[('title1',30),('title2',40)]
			for title,num in zip(titles,nums):
				print u"观众人数: -" + num.get_text().strip() + u"-\t房间名: " + title.get_text().strip()

			# 如果是最后一页,则退出循环
			if self.driver.page_source.find('shark-pager-disable-next') != -1:
				break

			# 不是最后一页,点击下一页
			self.driver.find_element_by_class_name('shark-pager-next').click()


	# 退出时的清理方法
	def tearDown(self):
		print("加载完成...")
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()

'''


'''
案例7:让页面执行javascript代码完成一些下拉之类的动作
所用知识: js基础,selenium,PhantomJS
'''

# 让百度首页的搜索框加红边框,让logo消失
def baiduAddJs():
	driver = webdriver.PhantomJS()
	driver.get("http://www.baidu.com")

	# 加入第一个js脚本:给百度搜索框加红色边框
	# 1.编写js脚本
	js = '''
		var q = document.getElementById("kw");
		q.style.border = "2px solid red"
	'''
	# 2.调用js脚本
	driver.execute_script(js)
	# 查看页面快照
	driver.save_screenshot("redbaidu.png")

	# 加入另一个脚本:隐藏百度logo
	# 1.获取隐藏的图像
	baiduLogo = driver.find_element_by_xpath("//*[@id='lg']/img")
	# 2.编写js脚本
	js2 = '$(arguments[0]).fadeOut()'

	# 3.为某一元素执行js脚本
	driver.execute_script(js2,baiduLogo)
	time.sleep(2)
	# 4.查看快照
	driver.save_screenshot("nullbaidu.png")

	# 退出浏览器
	driver.quit()


# 让豆瓣的页面下拉10000像素
def doubanAddJs():
	# 获取PhantomJs浏览器
	driver = webdriver.PhantomJS()
	driver.get("https://movie.douban.com/typerank?type_name=剧情&type=11&interval_id=100:90&action=")

	# 执行js脚本:模拟滚动条滚动到底部
	# 1.编写执行的js
	js = 'document.body.scrollTop = 10000'
	time.sleep(3)
	driver.save_screenshot("douban.png")

	# 2.执行脚本
	driver.execute_script(js)
	# 执行脚本后睡眠3秒,让操作完成
	time.sleep(10)
	# 3.保存照片
	driver.save_screenshot("newdouban.png")

	# 退出浏览器
	driver.quit()


# baiduAddJs()
# doubanAddJs()





'''
案例8: 验证码的图像处理
说明: 给一张验证码图片,生成对应的字符
技术: tesseract,PIL(python image libary)
'''
image = Image.open('./image/2.jpg')
text = pytesseract.image_to_string(image)
print(text)















































































































	