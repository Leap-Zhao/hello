#coding=utf-8

import urllib
import urllib2

# http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null
url = "http://fanyi.youdao.com/translate?"

key = raw_input("输入要翻译的文本: ")
formdata = {
	"smartresult":"dict",
	"smartresult":"rule",
	"action":"FY_BY_CLICKBUTTION",
	"client":"fanyideskweb",
	"doctype":"json",
	"from":"AUTO",
	"i":key,
	"keyfrom":"fanyi.web",
	"to":"AUTO",
	"typoResult":"false",
	"version":"2.1"
}

ua_header = {
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
}

data = urllib.urlencode(formdata)
request = urllib2.Request(url,data=data,headers=ua_header)
print(urllib2.urlopen(request).read())
