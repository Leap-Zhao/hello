#coding=utf-8

import urllib2
import random
import urllib

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

'''
案例1: 获取百度的网页源码
url: http://www.baidu.com
'''
'''
# 构造一个request对象
request = urllib2.Request("http://www.baidu.com")
# 发送请求,接收响应response
response = urllib2.urlopen(request)
# 查看状态响应码
print("响应状态码: " + str(response.code))
# 从response中获取源码
print(response.read())
'''


'''
案例2: 在1的基础上升级一下
2.1 为request对象添加请求头,构造一个完整的http请求
2.2 随机添加/修改User-Agent
'''
'''
def completeRequest():
	# 构造请求头和url
	request_header = {
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
	}
	url = "http://www.itcast.cn"
	# 构造http请求
	request = urllib2.Request(url,headers = request_header)
	# 也可以通过Request.add_header()方法 添加/修改一个请求头
	request.add_header("Connection", "keep-alive")
	# 可以通过Request.get_header()方法查看一个请求头信息
	# request.get_header(header_name="Connection")

	# 下面同案例1
	response = urllib2.urlopen(request)
	print("状态码: " + str(response.code))
	print(request.get_header(header_name="User-Agent"))	
	print(response.read())

def randomUA():
	url = "http://www.itcast.cn"
	ua_list = [
		"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
		"Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
		"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16",
		"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)"
	]
	# random.random()方法返回一个在[0,1)范围内的实数
	# random.choice(seq) 传入一个序列,随机返回序列中的一个元素
	user_agent = random.choice(ua_list)
	request_header = {
		"User-Agent":user_agent
	}
	# 其它和上边的completeRequest()方法差不多
	request = urllib2.Request(url,headers = request_header)
	# request.add_header("User-Agent", user_agent)
	# request.add_header("Connection", "keep-alive")
	print("UA: %s" % request.get_header(header_name="User-Agent"))
	print(urllib2.urlopen(request).read())

# completeRequest()
# randomUA()
'''





'''
认识url编码(urllib.urlencode(dict))与url解码(urllib.unquote(str))
通过urllib.urlencode()方法，将字典键值对按URL编码转换，从而能被web服务器接受。
通过urllib.unquote()方法，把 URL编码字符串，转换回原先字符串。
'''
'''
>>> import urllib
>>> dict1 = {"mv":"美女","num":1}
>>> urllib.urlencode(dict1)
'mv=%E7%BE%8E%E5%A5%B3&num=1'
>>> dict2 = {"sg":"帅哥"}
>>> urllib.urlencode(dict2)
'sg=%E5%B8%85%E5%93%A5'
>>> word1 = urllib.urlencode(dict1)
>>> print urllib.unquote(word1)
mv=美女&num=1
'''





'''
案例3: 爬取某一贴吧的前5页,且分别写入5个文件
说明: 此为爬取get方式请求的网站,请求的贴吧名会在url中显示出来
url: http://tieba.baidu.com/f?kw=lol&ie=utf-8&pn=100

'''

'''
def parseTieBa(tiebaName):
	kw = urllib.urlencode({"kw":tiebaName})
	for page in range(1,6):
		pn = str((page-1)*50)
		url = "https://tieba.baidu.com/f?" + kw + "&pn=" + pn
		html = parseUrl(url)
		loadToFile(html,page)
def parseUrl(url):
	print("正在解析%s" % url)
	request_headers = {
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
		"Connection":"keep-alive"
	}
	request = urllib2.Request(url,headers=request_headers)
	return urllib2.urlopen(request).read()
def loadToFile(html,page):
	fileName = str(page)+"page.html"
	print("正在写入文件%s" % fileName)
	with open(fileName,"w") as f:
		f.write(html)

if __name__ == '__main__':
	tiebaName = raw_input("输入你要获取的贴吧名:")
	parseTieBa(tiebaName)
	print("完成")
'''



'''
案例4: 获取有道翻译的json结果 
说明: 爬取post方式请求的网站响应内容,实际上post提交的数据在请求主体中,所以爬取post提交的数据有两步
第一步要找到真正提交的URL地址,第二步将要提交的数据传输过去
需要传输的表单数据要动态的传递过去,传到request(url,data,headers)中的data
'''
'''
def postData(translateWord):
	url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"
	formdata = {
		"i":translateWord,
		"from":"AUTO",
		"to":"AUTO",
		"smartresult":"dict",
		"client":"fanyideskweb",
		"doctype":"json",
		"version":"2.1",
		"keyfrom":"fanyi.web",
		"action":"FY_BY_REALTIME",
		"typoResult":"false"
	}
	data = urllib.urlencode(formdata)
	request_headers = {
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
		"Connection":"keep-alive"
	}
	request = urllib2.Request(url,data=data,headers=request_headers)
	print(urllib2.urlopen(request).read())

postData("hello")
'''




'''
案例5: 当一个网站需SSL认证时,怎么忽略SSL认证,比如访问12306

# 需要SSL认证的网站,当你没有SSL认证时,会报如下错误:
# urllib2.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:590)>

# 解决方法:
1.导入ssl包 import ssl
2.用context = ssl._create_unverified_context()方法去表示忽略未经核实的SSL证书认证
3.在urlopen()方法里 指明添加 context 参数 urllib2.urlopen(request, context = context)
'''
'''
# 有时候运行如下代码并不会报URLError,很奇怪...

url = "https://www.12306.cn/mormhweb/"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
request = urllib2.Request(url, headers = headers)
response = urllib2.urlopen(request)
print response.read()
'''


'''
案例6: 爬取豆瓣上的某一类电影,此处以"经典类"为例
说明: 此网站是用Ajax动态加载的,所以要找到Ajax动态返回json内容的URL地址
URL: 访问网页的url为https://movie.douban.com/explore#!type=movie&tag=%E7%BB%8F%E5%85%B8&sort=recommend&page_limit=20&page_start=0
用Fiddler找到返回json的URL为https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%BB%8F%E5%85%B8&sort=recommend&page_limit=20&page_start=0
其中page_limit为每页限制的显示电影个数,page_start为起始页的电影数(第1页为0,第2页为20)
'''
def ajaxParse():
	url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%BB%8F%E5%85%B8&sort=recommend&page_limit=500&page_start=0"
	headers = {
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
	}
	request = urllib2.Request(url,headers=headers)
	print(urllib2.urlopen(request).read())
ajaxParse()








'''
案例1:用保存的Cookie登录renren网
'''
# 1.获取之前保存的Cookie值
# 2.构建Request对象
# 3.发送请求,返回响应

'''
url = "http://www.renren.com/"
headers = {
	"Host" : "",
	"Connection" : "",
	"User-Agent" : "",
	"Accept" : "",
	"Referer" : "",
	"Cookie" : "",
}

request = urllib2.Request(url,headers=headers)
response = urllib2.urlopen(request)
print(response.read())
'''











