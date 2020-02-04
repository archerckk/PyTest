from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import pytest
import allure
import time
import json
import os
import logging
import random

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s')
clear_package = 'adb shell pm clear com.meetu.android'
# os.popen(clear_package)

is_login = False

class Test_meetu_release:

    def setup(self):
        with open('./resources/phone.json')as f:
            desired_caps=json.load(f)['mate8_meetu']

        self.driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        self.windows_size=self.driver.get_window_size()
        self.height=self.windows_size['height']
        self.width=self.windows_size['width']

        # self.driver.implicitly_wait(30)


    def teardown(self):
        self.driver.quit()

    def wait_time(self,loc,times=60,clear=False):
        wait=WebDriverWait(self.driver,times,0.5)
        if clear:
            wait.until_not(expected_conditions.presence_of_element_located(loc))
        else:
            wait.until(expected_conditions.presence_of_element_located(loc))

    def stop_app(self):
        stop_command='adb shell am force-stop com.meetu.android'
        os.popen(stop_command)

    def start_app(self):
        start_command = 'adb shell am start com.meetu.android/com.meetu.android.SplashActivity '
        os.popen(start_command)

    def switch_native(self):
        context = self.driver.contexts
        print(context)
        self.driver.switch_to.context(context[0])

    @allure.story('邮箱登录功能验证')
    def test_login(self):
        global is_login
        email_login_xpath='//*[@text="Email"][@class="android.widget.TextView"]/..'
        login_text_xpath='//*[@text="Login to MeetU"][@class="android.widget.TextView"]'
        account_xpath='//*[@text="Email"][@class="android.widget.TextView"]/../android.widget.EditText'

        password_xpath='//*[@text="Password"][@class="android.widget.TextView"]/../android.widget.EditText'
        continue_xpath = '//*[@text="Continue"][@class="android.widget.TextView"]'

        guide_xpath='//*[@text="Got it"][@class="android.widget.TextView"]/..'
        main_match_xpath='//*[contains(@text,"Instant")]'
        search_text='//android.widget.TextView[contains(@text,"Searching for more people"]'

        loc_login_text=('xpath',login_text_xpath)
        loc_guide=('xpath',guide_xpath)
        loc_button=('xpath',"//android.widget.Button[contains(@text,'允许')]")
        loc_search=('xpath',search_text)


        back='adb shell input keyevent 4'
        if self.driver.find_elements_by_xpath(email_login_xpath):
            self.driver.find_element_by_xpath(email_login_xpath).click()

            self.wait_time(loc_login_text)

            if self.driver.find_elements_by_xpath(login_text_xpath):
                self.driver.find_element_by_xpath(account_xpath).send_keys('501824353@qq.com')
                self.driver.find_element_by_xpath(password_xpath).send_keys('a12345')
                time.sleep(2)
                self.driver.find_element_by_xpath(continue_xpath).click()

                self.wait_time(loc_button)
                if "允许" in self.driver.page_source:
                    self.driver.find_element_by_xpath("//android.widget.Button[contains(@text,'允许')]").click()
                    is_login = True

                else:
                    self.driver.switch_to.alert.accept()
                    is_login = True

                time.sleep(3)

                self.switch_native()

                # main_match_result = self.driver.find_elements_by_xpath(main_match_xpath)
                if "Matches" in self.driver.page_source:
                    logging.debug('邮箱登录验证通过')
                else:
                    logging.debug('登录失败')
                    assert is_login==True

                self.wait_time(loc_search,clear=True)
                self.wait_time(loc_guide)
                if self.driver.find_elements_by_xpath(guide_xpath):
                    logging.debug('关闭滑动引导test')
                os.popen(back)
                logging.debug('关闭滑动引导')
                self.stop_app()

                # time.sleep(3)


    @allure.story('测试卡片滑动点击')
    def test_card_slid_click(self):
        # if not is_login:
        #     pytest.xfail('登录失败，用例标记为xfail')

        search_text = '//android.widget.TextView[contains(@text,"Searching for more people"]'
        loc_search = ('xpath', search_text)

        self.wait_time(loc_search,clear=True)
        logging.debug('等待完毕，执行滑动')

        #右滑喜欢1次
        self.driver.swipe(self.width*0.5,self.height*0.5,self.width*0.9,self.height*0.5,duration=2000)
        time.sleep(2)

        #上滑超级喜欢1次
        self.driver.swipe(self.width*0.5,self.height*0.5,self.width*0.5,0,duration=1000)
        time.sleep(2)

        #左滑不喜欢13次
        for i in range(14):
            self.driver.swipe(self.width*0.5,self.height*0.5,0,self.height*0.5,duration=1000)
            time.sleep(2)

        upgrade_xpath='//*[@text="UPGRADE"][@class="android.widget.TextView"]/..'
        upgrad_result=self.driver.find_elements_by_xpath(upgrade_xpath)
        assert upgrad_result!=0

        stop_command='adb shell am force-stop com.meetu.android'
        os.popen(stop_command)

        start_command='adb shell am start com.meetu.android/com.meetu.android.SplashActivity '
        os.popen(start_command)
        #
        time.sleep(5)

        upgrade_xpath = '//*[@text="UPGRADE"][@class="android.widget.TextView"]/..'
        upgrad_result = self.driver.find_elements_by_xpath(upgrade_xpath)
        logging.debug(upgrad_result)
        assert upgrad_result != []

        logging.debug('卡片全部划掉了，杀掉进程，重新启动没有产生新卡片')

    @allure.story('即时匹配聊天发送消息成功')
    def test_instant_chat(self):
        # if not is_login:
        #     pytest.xfail('登录失败，用例标记为xfail')

        random_int = random.randint(1, 100)
        message_send = 'test message{}'.format(random_int)
        instant_xpath = '//*[@text="Instant"][@class="android.widget.TextView"]/..'
        loc_instant=('xpath',instant_xpath)

        chat_xpath= '//*[@text="Chat"][@class="android.widget.TextView"]'
        loc_chat=('xpath',chat_xpath)

        message_xpath= '//*[@text="{}"][@class="android.widget.TextView"]/..'.format(message_send)


        edit_message_xpath= '//android.widget.EditText[contains(@text,"Enter message content")]'
        loc_message = ('xpath', edit_message_xpath)

        # time.sleep(30)
        self.wait_time(loc_instant)


        self.driver.find_element_by_xpath(instant_xpath).click()
        self.wait_time(loc_chat)

        self.driver.find_element_by_xpath(chat_xpath).click()

        self.switch_native()
        self.wait_time(loc_message)
        self.switch_native()
        self.driver.find_element_by_xpath(edit_message_xpath).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(edit_message_xpath).send_keys(message_send)
        time.sleep(2)
        # self.driver.find_element_by_xpath(edit_message_xpath).click()
        #执行发送消息
        self.driver.execute_script('mobile: performEditorAction', {'action': 'send'})
        time.sleep(12)


        message=self.driver.find_element_by_xpath(message_xpath)
        logging.debug(message)
        result=message.find_elements_by_class_name('android.widget.ImageView')
        # logging.debug('元素为：',result)
        result_int=len(result)
        print('结果为：',result_int)
        assert result_int== 1
        logging.debug('即时匹配聊天发送消息成功')


        #测试代码
        # icon_xpath='//*[@resource-id="com.meetu.android:id/oz"]'
        # tab=self.driver.find_element_by_xpath(icon_xpath)
        # result=len(tab.find_elements_by_class_name('android.widget.ImageView'))
        # logging.debug(result)



if __name__ == '__main__':
     pytest.main('ar_347_test_MeetU_test.py::Test_meetu_release::test_card_slid_click')