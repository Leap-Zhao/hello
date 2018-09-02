#coding=utf-8


# 根据ajax动态加载的网页,从中获取json文件
import urllib2
import urllib

# https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start=20
url = "https://movie.douban.com/j/new_search_subjects?"

ua_header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"}

form_data = {
	"range":"0,10",
	"sort":"T",
	"start":"0"
}
data = urllib.urlencode(form_data)
# print(data)

request = urllib2.Request(url,data = data,headers = ua_header)
response = urllib2.urlopen(request)
print(response.read())


