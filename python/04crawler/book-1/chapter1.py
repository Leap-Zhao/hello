#coding=utf-8

import urllib2

# 从url链接里读取html
def download(url):
	print("Downloading: %s" % url)
	try:
		headers = {
			"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
			"Connection" : "keep-alive"
		}
		request = urllib2.Request(url,headers = headers)
		html = urllib2.urlopen(request).read()
	except urllib2.URLError as e:
		print("Download error: %s" % e.reason )
		html = None
	return html

if __name__ == '__main__':
	url = "http://www.baidu.com/"
	print download(url)

