# coding=utf-8
#    Urllib库的基本使用
import urllib
import urllib2

# 1 读取网页内容：先使用urllib2.urlopen打开网址，再read读取
html = 'http://cuiqingcai.com/947.html'
response = urllib2.urlopen(html, )
# print response.read()
"""
Urllib2.urlopen(url ,data=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT,
                cafile=None, capath=None, cadefault=False, context=None)

url           1.可以是要访问的网址    2.也可以是由网址构成的Request对象  建议优先使用第2种方法
data          访问url时要传送的数据
timeout       设置超时时间

举个栗子：
a = urllib2.urlopen('http://www.baidu.com', data=None, timeout=10).read()
b = urllib2.urlopen(urllib2.Request('http://www.baidu.com'), data=None, timeout=10).read()
print a
print b
"""
# 2 读取动态网页内容：动态传送参数数据
"""
传输参数有两种方法
一、post
举个栗子：
values = {'username': '635943647@qq.com', 'password': '*****'}
data = urllib.urlencode(values)
url = 'https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn'
request = urllib2.Request(url, data)
response = urllib2.urlopen(request)
print response.read()

二、get
    get直接以链接方式访问，链接中包含了所有的参数，如果链接是用来登录则包括你的登录的账号和密码，是一种
    比较直观但是不安全的方法
举个栗子：
values = {'username': '635943647@qq.com', 'password': '*****'}
data = urllib.urlencode(values)
url = 'http://passport.csdn.net/account/login'
geturl = url + data         # geturl=http://passport.csdn.net/account/login/username=635943647%40qq.com&password=%2A%2A%2A%2A%2A
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print response.read()
"""
values = {'username': '635943647@qq.com', 'password': '*****'}
data = urllib.urlencode(values)  # data='username=635943647%40qq.com&password=%2A%2A%2A%2A%2A'
url = 'https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn'
request = urllib2.Request(url, data)
response = urllib2.urlopen(request)
print(response.read())
