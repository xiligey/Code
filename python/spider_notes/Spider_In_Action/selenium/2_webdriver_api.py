# coding=utf-8
from selenium import webdriver
driver = webdriver.Firefox()

driver.maximize_window()                # 1 浏览器最大化
driver.set_window_size(1000, 600)       # 2 浏览器宽480高300

first_url = 'http://www.baidu.com'
second_url = 'http://cuiqingcai.com'
driver.get(first_url)
driver.get(second_url)
driver.back()                           # 3_1 上一个网页
driver.forward()                        # 3_2 下一个网页

##########################################################
# 4 对象的定位：id、name、class name、link text、partial link text、xpath、css selector
# 对应的方法为：find_element_by_id()等等
driver.find_element_by_id('gs_htif0')
driver.find_element_by_name('btnk')
driver.find_element_by_tag_name('div')
driver.find_element_by_class_name('s_ipt')
driver.find_element_by_link_text('新 闻')
driver.find_element_by_partial_link_text('新')
# 重点介绍XPath和CSS
"""
<html> class="w3c">
<body>
    <div class="page-wrap">
    <div id="hd" name="q">
        <format target="_self" action="http://www.so.com/s">
        <span id="input-container">
            <input id="input" type="text" x-webkit-speech="" autocomplete="off" suggestwidth="501px">
"""
# xpath绝对路径
driver.find_element_by_xpath("/html/body/div[2]/form/span/input")
# xpath相对路径
driver.find_element_by_xpath("//input[@id='input']")    # 通过自身的id属性定位
driver.find_element_by_xpath("//span[@id='input-container']/input")     # 通过上一级目录的id属性定位
driver.find_element_by_xpath("//div[@name='q']/form/span/input")        # 通过上三级目录的id属性定位
driver.find_element_by_xpath("//div[@id=' hd' or @name=' q']")      # 布尔逻辑运算定位
"""CSS选择器常见语法
*                       通用元素选择器           任何元素
E                       标签选择器               匹配所有使用E标签的元素
.info                   class选择器              匹配所有class属性中包含info 的元素
#footer                 id选择器                 匹配所有id=footer的元素
E,F                     多元素选择器             同时匹配所有E或F元素
E F                     后代元素选择器            匹配所有属于E元素后代的F元素
E>F                     子元素选择器              匹配所有属于E元素的子元素F
E+F                     毗邻元素选择器            匹配紧跟E元素之后的同级元素F，只匹配第一个，等同于下一个兄弟节点
E~F                     同级元素选择器            匹配所有在E元素之后的同级F元素
E[att='val']            属性att的值等于val的E元素
E[att^='val']           属性att的值以val开头的E元素
E[att$='val']           属性att的值以val结尾的E元素
E[att*='val']           属性att的值包含val的E元素
E[att1='v1'][att2*='v2']属性att1的值为v1，att2的值包含v2的E元素
E:contains('xxxx')      内容中包含xxxx的E元素
E:not(s)                匹配不符合当前选择器的任何元素                     """

"""CSS语法匹配例子
<div class="formdiv">
<form name="fnfn">
<input name="username" type="text"></input>
<input name="password" type="text"></input>
<input name="continue" type="button"></input>
<input name="cancel" type="button"></input>
<input value="SYS123456" name="vid" type="text">
<input value="ks10cf6d6" name="cid" type="text">
</form>
<div class="subdiv">
<ul id="recordlist">
<p>Heading</p>
<li>Cat</li>
<li>Dog</li>
<li>Car</li>
<li>Goat</li>
</ul>
</div>
</div>

通过CSS语法匹配之后的结果
css=div
css=div.formdiv

css=#recordlist
css=ul#recordlist

"""