#coding=utf-8

import urllib
import urllib2

# 爬取贴吧的页面


def loadPage(url,filename):
	"""
		从url中加载网页
		url:
		filename:
	"""
	print("正在加载 %s" % filename)
	ua_headers =  {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"}
	request = urllib2.Request(url,headers = ua_headers)
	return urllib2.urlopen(request).read()

def writePage(html,filename):
	"""
		作用: 将从网上爬取的html代码写入到本地文件
		html:
		filename: 
	"""
	print("正在保存 %s" % filename)
	# 文件写入
	with open(filename,'wb') as f:
		f.write(html)
	print("-"*30)

def getUrls(url,beginPage,endPage):
	"""
		获取要抓取页面的url
		url:
		beginPage:
		endPage:
	"""
	for page in range(beginPage,endPage+1):
		pn = (page-1) * 50
		filename = "第" + str(page) + "页.html"
		fullurl = url + "&pn=" + str(pn)
		html = loadPage(fullurl,filename)
		writePage(html,filename)
	print("谢谢使用!")

def main():
	tiebaName = raw_input("请输入贴吧名: ")
	beginPage = int(raw_input("请输入起始页: "))
	endPage = int(raw_input("请输入结束页: "))

	url = "http://tieba.baidu.com/f?"
	wd = {"kw":tiebaName}
	wd = urllib.urlencode(wd)
	fullurl = url + wd
	getUrls(fullurl, beginPage, endPage)

if __name__ == '__main__':
	main()