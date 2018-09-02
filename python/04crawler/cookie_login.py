#coding=utf-8

import urllib
import urllib2
import cookielib

# CookieJar():保存cookie的值
cookie = cookielib.CookieJar()

# 构建一个HttpCookie处理器对象,用来处理cookie
cookie_handler = urllib2.HTTPCookieProcessor(cookie)

# 通过处理器对象构建一个opener
opener = urllib2.build_opener(cookie_handler)

# opener.addheaders = [("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"),("Connection","keep-alive")]

url = "http://www.renren.com/PLogin.do"
data = {"username":"zhaofeiyue1234@163.com","password":"1995421123"}

ua_headers = {
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
	"Connection":"keep-alive"
}

data = urllib.urlencode(data)
request = urllib2.Request(url,data=data,headers = ua_headers)
response = opener.open(request)
print(response.read())
