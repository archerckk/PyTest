from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
# from selenium.webdriver.common.keys import Keys
import unittest


class SearchTest(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['automationName'] = 'Appium'
        desired_caps['deviceName'] = 'HC4AVYC01597'
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.4'
        desired_caps['noReset'] = True
        desired_caps["appPackage"] = "com.cnblogs.xamarinandroid"
        desired_caps["appActivity"] = "md522127645c21675e531a6ac609ef72b2a.SplashScreenActivity"
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        sleep(5)

    def test_case(self):
        driver = self.driver
        # 点击搜索按钮
        driver.find_element_by_accessibility_id("搜索").click()

        # 搜索框
        search_src_text = driver.find_element_by_id("com.cnblogs.xamarinandroid:id/search_src_text")
        search_src_text.click()
        sleep(1)
        # 输入搜索关键字“appium”
        driver.keyevent(29)  # a
        driver.keyevent(44)  # p
        driver.keyevent(44)  # p
        driver.keyevent(37)  # i
        driver.keyevent(49)  # u
        driver.keyevent(41)  # m
        sleep(1)
        # 回车搜索
        driver.keyevent(66)
        driver.keyevent(66)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()