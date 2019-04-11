from appium import webdriver
from time import sleep
import unittest
import os


#设备顺序为：三星C7，VIVO AX6
devices=['420c3a6d6a2da4bf','3665defe']
automationName=['UiAutomator2','Appium']
platformVersion=['7.1.1','5.0.2']



class SearchTest(unittest.TestCase):
    def setUp(self):
        self.package_name = 'com.aplus.camera.android'

        desired_caps = {}
        desired_caps['automationName'] = automationName[1]
        desired_caps['deviceName'] = devices[1]
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = platformVersion[1]
        desired_caps['noReset'] = True
        desired_caps["appPackage"] = "com.aplus.camera.android"
        desired_caps["appActivity"] = "com.aplus.camera.android.main.HomeActivity"
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        sleep(5)

    def test_sub_ui(self):
        driver = self.driver
        for i in range(5):
            print('执行第%s次：'%str(i+1))
            os.popen('adb shell pm clear %s ' % self.package_name)
            sleep(3)
            os.popen('adb shell am  start com.aplus.camera.android/com.aplus.camera.android.main.HomeActivity')
            sleep(10)

            try:
                # 检查购买按钮是否有出现
                self.assertNotIn('com.aplus.camera.android:id/mx',driver.page_source)
                print('下方购买按钮没有展示')
            except AssertionError:
                sub_icon = driver.find_element_by_xpath(
                    "//*[@resource-id='com.aplus.camera.android:id/mz']"
                    "[@class='android.widget.RelativeLayout']"
                )
                #获取订阅按钮上面的文案
                sub_icon_text = sub_icon.find_element_by_id('com.aplus.camera.android:id/a2c').text
                error_text = ['3-Day Free Trial', 'CONTINUE']

                print("订阅按钮文案为：%s" % sub_icon_text)

                #检查购买按钮的文案是否有出现continue和3-Day Free Trial
                try:
                    self.assertNotIn(sub_icon_text,error_text)
                    print('购买按钮没有显示异常文案')
                except AssertionError as e:
                    print(e)

                #检查购买按钮上方是否存在箭头
                try:
                    self.assertNotIn('com.aplus.camera.android:id/lx',driver.page_source,'购买按钮存在箭头')
                    print('购买按钮不存在箭头')
                except AssertionError as e:
                    print(e)

    def tearDown(self) :
        self.driver.quit()

