import pytest
import allure
from Ar_Script.Meetu_Ui_Test.Pages.base_page import *
import json
from appium import webdriver
import time

class Test_login:

    def setup(self):

        with open('C:\PyTest\Ar_Script\Meetu_Ui_Test\config\phone.json')as f:
            desired_caps = json.load(f)['mate8_meetu']

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.account_page=Account_login_page(self.driver)
        self.start_page=StarPage(self.driver)
        # self.windows_size = self.driver.get_window_size()
        # self.height = self.windows_size['height']
        # self.width = self.windows_size['width']

        self.driver.implicitly_wait(30)

    # def setup_class(self):
    #     se

    def teardown(self):
        self.driver.quit()

    @allure.story('meetu账号登录测试')
    @pytest.mark.parametrize('account,psw',
                             [
                                 ('644326394@qq.com','a12345'),
                                 ('1','1'),
                                 ('644326394@QQ.COM','1'),
                                 ('1','123456')
                               ]
    )
    def test_login(self,account,psw):
        self.start_page.click_account_login()
        self.account_page.account_input(account)
        self.account_page.psw_input(psw)
        # time.sleep(3)
        # self.driver.keyevent(4)
        self.account_page.click_login()
        if account==''and psw=='':
            # assert self.account_page.find_element(self.account_page.account_format_error)!=None
            # assert self.account_page.find_element(self.account_page.psw_empty_error)!=None
            assert self.account_page.find_element(self.account_page.login_loc).get_attribute('clickable')==False

        elif psw=='':
            # assert self.account_page.find_elements(self.account_page.account_format_error)==[]
            # assert self.driver.find_element(self.account_page.psw_empty_error)!=None
            assert self.account_page.find_element(self.account_page.login_loc).get_attribute('clickable')==False


        elif account=='':
            # assert self.account_page.find_element(self.account_page.account_format_error) !=None
            # assert self.driver.find_elements(self.account_page.psw_empty_error) ==[]
            assert self.account_page.find_element(self.account_page.login_loc).get_attribute('clickable')==False


        # time.sleep(30)
        else:
            result=self.account_page.is_toast_exist(self.driver,'Network')
            assert result==True


if __name__ == '__main__':
    pytest.main(['login_test.py::Test_login'])