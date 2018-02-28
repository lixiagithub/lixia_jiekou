# coding:utf-8
import unittest
import time
from selenium import webdriver
from common.logger import Log


class Test1(unittest.TestCase):

    log = Log()

    def setUp(self):
        print("start!")
        self.log.info("----开始----")
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.baidu.com")
        self.driver.implicitly_wait(3)

    def tearDown(self):
        print("2end!")
        self.driver.close()

    def test_01(self):
        u"""百度搜索"""
        self.driver.find_element_by_id("kw").send_keys("yoyo")
        time.sleep(3)

    def test_02(self):
        self.driver.find_element_by_id("kw").send_keys("haha")
        time.sleep(3)

if __name__ == "__main__":
    unittest.main()
