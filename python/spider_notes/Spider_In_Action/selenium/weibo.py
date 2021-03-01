# coding=utf-8
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get('http://weibo.com/login.php')
driver.find_element_by_link_text('帐号登录').click()
driver.find_element_by_id('loginname').send_keys('18810686014')
driver.find_element_by_name('password').send_keys('zxc123!@#')
# print type(driver.find_element_by_class_name('W_btn_a btn_40px'))
driver.find_element_by_css_selector('a[tabindex="6"]').click()

