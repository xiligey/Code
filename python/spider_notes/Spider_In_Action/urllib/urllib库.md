[TOC]

# 一、urllib库的基本使用

## 1读取静态网页

```python
import urllib
import urllib2
url = 'http://cuiqingcai.com/947.html'
print urllib2.urlopen(url).read()
```

> urllib2.urlopen(url ,data=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT, cafile=None, capath=None, cadefault=False, context=None)

urllib2.urllib()的参数含义：

参数      | 解释
------- | ----------------------------------------
url     | 1.可以是要访问的网址 2.也可以是由网址构成的Request对象        | 建议优先使用第2种方法
data    | 访问url时需要传输的数据 默认为None
timeout | 设置超时时长 默认为socket._GLOBAL_DEFAULT_TIMEOUT

> 举个栗子：

> ```python
> a = urllib2.urlopen('http://www.baidu.com', data=None, timeout=10).read()
> b = urllib2.urlopen(urllib2.Request('http://www.baidu.com', data=None, timeout=10).read()
> print a, b
> ```

## 2.读取动态网页:动态传送参数数据

### 2.1 post方式

```python
values = {'username': '635943647@qq.com', 'password': '*******'}
data = urllib.urlencode(values)    # data='username=635943647%40qq.com&password=%2A%2A%2A%2A%2A'
url = 'https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn'
request = urllib2.Request(url, data)
response = urllib2.urlopen(request)
print response.read()
```

### 2.2 get方式

```python
values = {'username': '635943647@qq.com', 'password': '*******'}
data = urllib.urlencode(values)    # data='username=635943647%40qq.com&password=%2A%2A%2A%2A%2A'
url = 'https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn'
get_url = url + data
request = urllib2.Request(geturl)
respnse = urllib2.urlopen(request)
print response.read()
```

# 二、urllib库的高级使用

## 1.设置Headers

> 有些网站不会同意程序直接访问，也就不能得到想要的响应值，所以为了模拟浏览器的工作，我们需要设置一些Headers的属性（头信息）

agent：请求的身份， referer:用来反盗链（如果referer不是它自己，有的服务器不会响应） 所以构建以下headers headers = { 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' ,'Referer':'<http://www.zhihu.com/articles'}> 然后把headers传入Request参数里就可以了

> <font color="Red">注意：</font>

> 如果有必要，还有一些属性也要添加进去，具体哪些：网站F12查看

## 2.代理设置

> urllib2默认使用环境变量http_proxy来设置HTTP Proxy。有的网站会检测同一个ip的访问频率，如果频率过高，它会禁止这个ip的访问（反爬虫的重要手段之一）。所以，我们可以设置一些代理服务器，每隔一会换一个代理ip，这样网站就察觉不到了（反反爬虫的重要手段之一）。

```python
import urllib2
enableproxy = True
proxy_handler = urllib2.ProxyHandler({"http://some-proxy.com:8080"})    # 能正常工作的代理ip
numm_proxy_handler = urllib2.ProxyHandler({})    # 无代理

if enable_proxy:
    opener = urllib2.build_opener(proxy_andler)
else:
    opener = urllib2.build_opener(null_proxy_handler)
urllib2.install_opener(opener)
```

## 3.超时设置

可以设置等待多长时间算超时

```python
import urllib2
# 两种设置超时时长的方法：如果有data参数了，就不用加"timeout="这几个字
response1 = urllib2.urlopen('http://www.baidu.com', timeout=10)
response2 = urllib2.urlopen('hepp://www.baidu.com', data, 10)
```

<http://latex.codecogs.com/svg.latex?\frac{1}{\pi}=\frac{2\sqrt{2}}{9801}\sum_{k=0}^\infty\frac{(4k)!(1103+26390k)}{(k!)^4396^{4k}}>
