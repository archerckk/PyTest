from ddt import ddt,data,unpack
from appium import webdriver
import unittest
import json
import time

"""
//android.widget.EditText[@content-desc="请输入QQ号码或手机或邮箱"
password
login

dialogText
com.tencent.mobileqq:id/dialogRightBtn

ivTitleName
"""

@ddt
class QQ_login(unittest.TestCase):

    def setUp(self):
        with open('resources/phone.json')as f:
            desired=json.load(f)
        self.driver=webdriver.Remote('http://localhost:4723/wd/hub',desired['mate8_qq'])


    @data(
        # ('137160564','12347','帐号或密码错误，请重新输入。'),
        ('137160564','2@#%%%@#%^','帐号或密码错误，请重新输入。'),
        # ('137160564','null',False),
        ('137160564','chaoheweijing',True)
    )
    @unpack
    def test_login(self,user_name,password,result):
        time.sleep(3)
        account_input=self.driver.find_element_by_accessibility_id('请输入QQ号码或手机或邮箱')
        account_input.clear()
        account_input.send_keys(user_name)

        password_input= self.driver.find_element_by_accessibility_id('密码 安全')
        password_input.clear()
        password_input.send_keys(password)
        # self.driver.find_element_by_xpath('//*[@content-desc="请输入QQ号码或手机或邮箱"').send_keys('137160564')
        # self.driver.find_element_by_id('password').send_keys('chaoheweijin')

        login_button=self.driver.find_element_by_id('login')



        if password=='null':
            password_input.clear()
            self.assertEqual(login_button.is_enabled(),result)
        elif password=='chaoheweijing':
            login_button.click()
            self.driver.implicitly_wait(6)

            # self.assertEqual(login_button.is_displayed(),result)
            self.assertEqual(self.driver.find_element_by_accessibility_id('搜索').is_displayed(),result)
        else:
            login_button.click()
            time.sleep(3)
            text=self.driver.find_element_by_id('dialogText').text
            print(text)
            self.assertEqual(text,result)


    def tearDown(self) -> None:
        self.driver.quit()