# coding=utf-8
from bs4 import BeautifulSoup
import bs4
import re

html = """
<html><head><title>THe Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b> The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elise" class="sister" id="link1"><!-- Elise --></a>'
<a href="http://example.com/lacie: class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
# 1 创建BeautifulSoup对象
soup = BeautifulSoup(html)
# 2 格式化输出soup对象的内容
print(soup.prettify())

# 3 BeautifulSoup的四种对象

# 3.1 Tag：HTML的一个个标签
print(soup.title, soup.head, soup.a, soup.p)
# Tag的两个重要属性：name和attrs
print(soup.title.name, soup.head.name, soup.a.name, soup.p.name, soup.name)
print(soup.title.attrs, soup.head.attrs, soup.a.attrs, soup.p.attrs, soup.attrs)
# attrs返回一个字典类型
print(soup.p['class'], soup.p.get('class'))
# 可以对这些属性和内容进行修改或删除
soup.p['class'] = 'newClass'
print(soup.p)
del soup.p['class']
print(soup.p)

# 3.2 NavigableString：可遍历的字符串
print(soup.p.string, soup.p.text)
print(soup.strings, soup.text)

# 3.3 BeautifulSoup:该对象表示的是一个文档的全部内容，可以把它当作一个特殊的tag
print(soup.name, soup.attrs)

# 3.4 Comment：一个特殊类型的NavigableString对象
print(soup.a)
print(soup.a.string, type(soup.a.string))
if type(soup.a.string) == bs4.element.Commemt:
    print(soup.a.string)
# 注意到a标签的内容实际上是注释，但是用.string或者.text输出它时会将注释符号去掉

# 4 遍历文档树
# 4.1 直接子节点:要点: .contents和.children
# .contents属性将tag的子节点以列表的形式输出
print(soup.head.contents, len(soup.head.contents), soup.head.contents[0])
# .children返回一个列表生成器
print
soup.head.children
for i, child in enumerate(soup.body.children):
    print(child)
    print(i)

# 4.2 所有子孙节点：.descendants
# .contents和.children仅包含tag的直接子节点，.descendants属性可以对所有tag的子孙节点进行递归
for i, child in enumerate(soup.descendants):
    print(i)
    print(child)

# 4.3 节点内容:如果tag的子节点数<=1，输出最里面的内容，如果>1，输出None
print(soup.head.string)
print(soup.title.string)
print(soup.body.string)

# 4.4 多个内容：.strings 和 .stripped_strings
# .strings：获取多个内容，不过需要遍历
for i, string in enumerate(soup.strings):
    print(i)
    print(string)
# .stripped_strings:对strings做strip处理：处理完了为空的则不返回
for i, string in enumerate(soup.stripped_strings):
    print(i)
    print(string)

# 4.5 父节点： .parent
print(soup.p.parent)

# 4.6 祖宗节点： .parents
print(type(soup.p.parents))
for i, parent in enumerate(soup.p.parents):
    print(i)
    print(parent)
# 4.7 兄弟节点： .next_sibling, .previous_sibling
# 4.8 全部兄弟节点： .next_siblings, .previous_siblings
# 4.9 前后节点： .next_element, .previous_element
# 4.10 全部前后节点： .next_elements, .previous_elements

# 5 搜索文档树
# 5.1 find_all():搜索当前tag的所有tag子节点
soup.find_all('b')
soup.find_all(re.compile('^b'))
soup.find_all(['a', 'b'])
soup.find_all(True)  # 找到所有
