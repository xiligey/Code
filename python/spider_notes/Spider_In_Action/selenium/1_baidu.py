# coding=utf-8
from selenium import webdriver
driver = webdriver.Firefox()
driver.get('http://www.baidu.com')
driver.find_element_by_id('kw').send_keys('selenium')   # 搜索框里传送文字"selenium"
driver.find_element_by_id('su').click()                 # 点击"百度一下"按钮
driver.quit()                                           # 退出浏览器
