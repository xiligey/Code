# coding=utf-8
from selenium import webdriver
import time
driver = webdriver.Edge()
driver.get('http://www.51lietou.com/hr/login')
driver.find_element_by_name('username').clear()
driver.find_element_by_name('username').send_keys('plcxjl')
driver.find_element_by_id('password').clear()
driver.find_element_by_id('password').send_keys('1')
driver.find_element_by_id('loginButton').click()
time.sleep(3)
driver.quit()