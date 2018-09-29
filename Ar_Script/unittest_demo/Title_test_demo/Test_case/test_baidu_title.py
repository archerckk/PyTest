from selenium import webdriver
from time import sleep
import unittest

class Test_baidu(unittest.TestCase):
    '测试百度是否能正常搜索'
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url='http://www.baidu.com'

    def test_baidu(self):
        '搜索关键字【selenium 测试】'
        driver=self.driver
        driver.get(self.base_url)
        driver.find_element_by_id('kw').clear()
        driver.find_element_by_id('kw').send_keys('selenium 测试')
        driver.find_element_by_id('su').click()
        sleep(7)
        self.assertEqual(driver.title,'selenium 测试_百度搜索')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
