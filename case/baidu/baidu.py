#coding=utf-8
from selenium import webdriver
import time
from common import location

#调用location.py 文件的定位方法
we = location
#dr = webdriver.Chrome()
dr = webdriver.Firefox()
dr.get('http://www.baidu.com')
#调用封装的方法
we.findId(dr, "kw").send_keys('selenium')
time.sleep(2)
we.findId(dr, "su").click()
time.sleep(2)
dr.quit()
