# -*- coding:UTF-8 -*-
import urllib
import urllib2
import re

page = 1
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64)'
headers = {'User-Agent' : user_agent}			#有段时间显示403，但是网页访问没问题。之后加了user-agent。过了一会又可以正常获取源码了。
url = "http://www.budejie.com/text/" + str(page)
try:
	request = urllib2.Request(url,headers = headers)
	response = urllib2.urlopen(request)
	pageCode = response.read().decode('utf-8')
	#print response.read() 测试页面获取
except urllib2.URLError,e:
	if hasattr(e,"reason"):
		print u"连接失败原因：",e.reason


pattern = re.compile('<div.*?u-txt">.*?<a.*?>(.*?)</a>.*?<span.*?>(.*?)</span>.*?<div.*?class="j-r-list-c-desc">.*?<a.*?>(.*?)</a>.*?<i.*?class="icon-up ui-icon-up">.*?<span>(.*?)</span>',re.S)
items = re.findall(pattern,pageCode)
#litems = list(items)
#fitems = litems.strip('<br />')  1.去除<br />
for item in items:
	print u"作者：%s\t\t\t时间:%s\n内容:%s\n点赞数:%s\n" %(item[0],item[1],item[2],item[3])  #2.时间居右
