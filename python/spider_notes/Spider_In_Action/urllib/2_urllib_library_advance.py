# coding=utf-8
import urllib
import urllib2
import re
import StringIO
import gzip

# 1 提取动态的lt和execution
url = 'https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn'
string = urllib2.urlopen(url).read()
pattern_lt = re.compile('name="lt" value="(.*)" />')
pattern_execution = re.compile('name="execution" value="(.*)" />')
lt = re.findall(pattern_lt, string)[0]
execution = re.findall(pattern_execution, string)[0]
print(lt, execution)

# 2 设置headers和post_data，然后request并得到response
post_url = 'https://passport.csdn.net/account/login?from=http%3A%2F%2Fmy.csdn.net%2Fmy%2Fmycsdn'

headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate, br',
           'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
           'Connection': 'keep-alive',
           'Host': 'passport.csdn.net',
           'Referer': 'https://passport.csdn.net/account/login?from=http%3A%2F%2Fmy.csdn.net%2Fmy%2Fmycsdn',
           'Content-Type': 'application/x-www-form-urlencoded'
           }
post_data = {'_eventId': 'submit',
             'execution': execution,
             'lt': lt,
             'password': 'nzdwzdnm98',
             'username': '635943647@qq.com'}
post_data = urllib.urlencode(post_data)
request = urllib2.Request(post_url, post_data, headers)
response = urllib2.urlopen(request)
data = response.read()

# 3 data解压缩
buf = StringIO.StringIO(data)
gzip_f = gzip.GzipFile(fileobj=buf)
content = gzip_f.read()
print(content)
