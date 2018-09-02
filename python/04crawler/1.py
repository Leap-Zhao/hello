#coding=utf-8
import urllib
import urllib2
import sys
import time

# 构造请求头request head字典,带上User-Agent(必须的),表示浏览器
# ua_headers = {
# 	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
# }

# # 构造请求对象
# request = urllib2.Request("http://www.baidu.com",headers = ua_headers)

# # 发送请求,并返回服务器响应的类文件对象
# response = urllib2.urlopen(request)
# html = response.read()
# states = response.getcode()
# url = response.geturl()

# print(html)

# print(urllib2.urlopen(request).read())


'''
==================================
写一个百度搜索的api接口
==================================
'''

url = "http://www.baidu.com/s"
useragent_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"}
inputStr = "请输入关键字:".decode("utf8")
print(inputStr)
# keyword = raw_input(inputStr)
# wd = {"wd":keyword}

# wd = urllib.urlencode(wd)
# fulurl = url + "?" + wd

# print(fulurl)



'''
GET / HTTP/1.1
Host: www.baidu.com
Connection: keep-alive
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36
# Upgrade-Insecure-Requests: 1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
# Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cookie: BAIDUID=9A99D682A89A59210E2F4F2ADB8A5C06:FG=1; PSTM=1506508813; BIDUPSID=F1C8F842C7778B8D15116C84443CCE54; BDUSS=kxpVXZjNWtCVzRPY0s2VGRIZzZTQUR4NWZ5ampaSTdEVH4wNkJ0MDNwZ0dRcEZhQVFBQUFBJCQAAAAAAAAAAAEAAAC0lGk1yLG3ps7C3LBkuqLX0wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa1aVoGtWlaZ; MCITY=-70068%3A70100%3A131%3A; ispeed_lsm=0; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; H_PS_645EC=7f52L6j7JckQFOZsyAKB2vqzngaqXhPJCvNq3oXbACuZJmiANRw6zpA7jBck4MEZFgBX; BD_CK_SAM=1; PSINO=1; BD_HOME=1; H_PS_PSSID=1449_21091_22159; BD_UPN=12314753; sug=3; sugstore=1; ORIGIN=0; bdime=0
'''