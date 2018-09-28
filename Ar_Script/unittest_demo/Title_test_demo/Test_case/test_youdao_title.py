from selenium import webdriver
from time import sleep
import unittest
from selenium.webdriver.common.keys import Keys

class Test_baidu(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url='http://www.youdao.com'

    def test_baidu(self):
        driver=self.driver
        driver.get(self.base_url)
        driver.find_element_by_id('translateContent').clear()
        driver.find_element_by_id('translateContent').send_keys('selenium')
        driver.find_element_by_id('translateContent').send_keys(Keys.ENTER)
        sleep(3)
        self.assertEqual(driver.title,'【selenium】什么意思_英语selenium的翻译_音标_读音_用法_例句_在线翻译_有道词典')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
