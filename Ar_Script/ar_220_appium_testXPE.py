from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
import unittest

class SearchTest(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['automationName'] = 'Appium'
        desired_caps['deviceName'] = '68cac4b1'
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.4'
        desired_caps['noReset'] = True
        desired_caps["appPackage"] = "com.picstudio.photoeditorplus"
        desired_caps["appActivity"] = "com.picstudio.photoeditorplus.camera.MainActivity"

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        sleep(5)

    def test_case(self):
        driver=self.driver
        # driver.find_element_by_id('sl').click()
        # driver.find_elements_by_android_uiautomator("new UiSelector().text(\"Collage\")")[0].click()
        # driver.tap([(752,252),(1032,612)],500)
        # driver.find_element_by_xpath(r'//android.widget.TextView[contains(@text,"collage")]').click()
        collage=driver.find_element_by_xpath("//*[@resource-id='com.picstudio.photoeditorplus:id/so'][@text='Collage']")
        collage.click()
        sleep(10)
        if 'Collage' in driver.page_source:
            assert print('没有跳转到拼图页面')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()