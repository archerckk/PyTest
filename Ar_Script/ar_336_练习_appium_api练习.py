from appium import webdriver
import unittest
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Api_demo(unittest.TestCase):

    def setUp(self) -> None:
        with open('resources/phone.json', 'r')as f:
            self.desired = json.load(f)

        self.driver=webdriver.Remote('http://localhost:4723/wd/hub',self.desired['moto_g5_taobao'])

    def is_toast_show(self,driver,text,max_time=30,rate=0.5):
        try:
            locate_doc = ('xpath', r'.//*[contains(@text,"{}")]'.format(text))
            WebDriverWait(driver, max_time, rate).until(EC.presence_of_element_located(locate_doc))
            return True
        except:
            return False

    def test_demo(self):
        ac=self.driver.current_activity
        print(ac)
        #启动app的时候考虑用这个去替代sleep
        self.driver.wait_activity(ac, 10, 1)

        nav_bar=self.driver.find_element_by_id('android:id/tabs')

        tabs=nav_bar.find_elements_by_class_name('android.widget.FrameLayout')

        for i in tabs:
            print(i)

        #测试toast 弹窗是否出现
        self.driver.back()
        result=self.is_toast_show(self.driver,'退出手机淘宝')

        self.assertEqual(result,True)

        #测试跳转是否成功
        tabs[1].click()




    def tearDown(self) -> None:
        self.driver.quit()