#coding=utf-8

import urllib2
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

'''
# Handler处理器和自定义Opener

opener是 urllib2.OpenerDirector 的实例，我们之前一直都在使用的urlopen，它是一个特殊的opener（也就是模块帮我们构建好的）。

但是基本的urlopen()方法不支持代理、cookie等其他的HTTP/HTTPS高级功能。所以要支持这些功能：

使用相关的 Handler处理器 来创建特定功能的处理器对象；
然后通过 urllib2.build_opener()方法使用这些处理器对象，创建自定义opener对象；
使用自定义的opener对象，调用open()方法发送请求。
如果程序里所有的请求都使用自定义的opener，可以使用urllib2.install_opener() 将自定义的 opener 对象 定义为 全局opener，表示如果之后凡是调用urlopen，都将使用这个opener（根据自己的需求来选择）
'''




'''
案例1: 自定义的Opener(开放器/开始器),如同urllib2.urlopen()一样
# 步骤
1. 构建处理器对象
2. 通过处理器对象构建Opener对象
3. 用Opener对象的open方法发送请求,获取响应
'''

'''
# 构建处理器对象
http_handler = urllib2.HTTPHandler()
https_handler = urllib2.HTTPSHandler()
# 用处理器对象去构建opener开放器对象
http_opener = urllib2.build_opener(http_handler)
# 用Opener对象去发送请求,返回响应
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"}
request = urllib2.Request("http://www.baidu.com",headers=headers)
response = http_opener.open(request)
print(response.code)
print(response.read())
'''







'''
案例2: 通过代理处理器来使用代理,去访问网站服务器
代理服务器: ProxyHandler({"http/https" : "IpAddress:port"})
'''

proxy_handler = urllib2.ProxyHandler({"https":"124.193.37.5:8888"})
null_handler = urllib2.ProxyHandler({})

print("hello")

# 定义代理开关
proxySwitch = True
if proxySwitch:
	opener = urllib2.build_opener(proxy_handler)
else:
	opener = urllib2.build_opener(null_handler)

url = "http://www.baidu.com/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"}
request = urllib2.Request(url,headers=headers)
response = opener.open(request)
print(response.read())


'''
案例3:
'''