from appium import webdriver
# from appium.webdriver.webelement import By
import pytest
import allure
import time
import json
import os
import logging

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s')
# clear_package = 'adb shell pm clear com.meetu.android'
# os.popen(clear_package)

class Test_meetu_release:

    def setup(self):
        with open('./resources/phone.json')as f:
            desired_caps=json.load(f)['sanxingC8_meetu']

        self.driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        self.windows_size=self.driver.get_window_size()
        self.height=self.windows_size['height']
        self.width=self.windows_size['width']


    def teardown(self):
        self.driver.quit()

    @allure.story('邮箱登录功能验证')
    def test_login(self):
        self.driver.implicitly_wait(5)
        email_login_xpath='//*[@text="Email"][@class="android.widget.TextView"]/..'
        login_text_xpath='//*[@text="Login to MeetU"][@class="android.widget.TextView"]'
        account_xpath='//*[@text="Email"][@class="android.widget.TextView"]/../android.widget.EditText'

        password_xpath='//*[@text="Password"][@class="android.widget.TextView"]/../android.widget.EditText'
        continue_xpath = '//*[@text="Continue"][@class="android.widget.TextView"]/..'

        guide_xpath='//*[@text="Got it"][@class="android.widget.TextView"]/..'
        main_match_xpath='//*[@text="Matches"][@class="android.widget.TextView"]/..'

        back='adb shell input keyevent 4'
        if self.driver.find_elements_by_xpath(email_login_xpath):
            self.driver.find_element_by_xpath(email_login_xpath).click()
            self.driver.implicitly_wait(3)
            if self.driver.find_elements_by_xpath(login_text_xpath):
                self.driver.find_element_by_xpath(account_xpath).send_keys('501824353@qq.com')
                self.driver.find_element_by_xpath(password_xpath).send_keys('a12345')
                self.driver.find_element_by_xpath(continue_xpath).click()
                time.sleep(6)
                self.driver.switch_to.alert.accept()
                time.sleep(5)
                if self.driver.find_elements_by_xpath(guide_xpath):
                    os.popen(back)
                    logging.debug('关闭滑动引导')
                time.sleep(3)
                main_match_result=self.driver.find_elements_by_xpath(main_match_xpath)
                assert main_match_result!=0
                logging.debug('邮箱登录验证通过')

    @allure.story('测试卡片滑动点击')
    def test_card_slid_click(self):
        # time.sleep(5)
        # #右滑喜欢1次
        # self.driver.swipe(self.width*0.5,self.height*0.5,self.width*0.9,self.height*0.5,duration=1000)
        # time.sleep(2)
        # #上滑超级喜欢1次
        # self.driver.swipe(self.width*0.5,self.height*0.5,self.width*0.5,0,duration=1000)
        # time.sleep(2)
        # for i in range(14):
        #     self.driver.swipe(self.width*0.5,self.height*0.5,0,self.height*0.5,duration=1000)
        #     time.sleep(2)
        #
        # upgrade_xpath='//*[@text="UPGRADE"][@class="android.widget.TextView"]/..'
        # upgrad_result=self.driver.find_elements_by_xpath(upgrade_xpath)
        # assert upgrad_result!=0
        #
        # stop_command='adb shell am force-stop com.meetu.android'
        # os.popen(stop_command)
        #
        # start_command='adb shell am start com.meetu.android/com.meetu.android.SplashActivity '
        # os.popen(start_command)
        #
        time.sleep(5)

        upgrade_xpath = '//*[@text="UPGRADE"][@class="android.widget.TextView"]/..'
        upgrad_result = self.driver.find_elements_by_xpath(upgrade_xpath)
        logging.debug(upgrad_result)
        assert upgrad_result != []

        logging.debug('卡片全部划掉了，杀掉进程，重新启动没有产生新卡片')

    @allure.story('测试即时匹配次数')
    def test_instant_chat(self):
        instant_xpath = '//*[@text="Instant"][@class="android.widget.TextView"]/..'
        chat_xpath= '//*[@text="Chat"][@class="android.widget.TextView"]'
        message_xpath= '//*[@text="test message"][@class="android.widget.TextView"]/..'
        edit_message_xpath= '//*[@text="Enter message content"][@class="android.widget.EditText"]'
        send='adb shell input KEYCODE_ENTER'
        result=0

        time.sleep(5)
        self.driver.find_element_by_xpath(instant_xpath).click()
        time.sleep(6)
        self.driver.find_element_by_xpath(chat_xpath).click()
        time.sleep(6)
        self.driver.find_element_by_xpath(edit_message_xpath).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(edit_message_xpath).send_keys('test message')
        time.sleep(2)
        # self.driver.find_element_by_xpath(edit_message_xpath).click()
        #执行发送消息
        self.driver.execute_script('mobile: performEditorAction', {'action': 'send'})
        time.sleep(2)

        message=self.driver.find_elements_by_xpath(message_xpath)
        if message_xpath!=[]:
            result=message[0].find_elements(('android.widget.ImageView')).size()
            logging.debug('结果为：',result)
        assert  result==1



if __name__ == '__main__':
     pytest.main('ar_347_test_MeetU_test.py::Test_meetu_release::test_card_slid_click')