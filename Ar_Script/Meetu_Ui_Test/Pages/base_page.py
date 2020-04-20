from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from appium import webdriver
import time
from  Ar_Script.Meetu_Ui_Test.common.logger import Loger
import logging

class BasePage(object):

    def __init__(self,driver):
        self.driver=driver
        self.log=Loger()

    def find_element(self,*loc,check=False):
        try:
            if check:
                WebDriverWait(self.driver, 30, 0.5).until(EC.invisibility_of_element_located(loc))
                return self.driver.find_element(*loc)

            WebDriverWait(self.driver,30,0.5).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except :
            logging.debug("页面上找不到{}元素".format(loc))

    def find_elements(self, *loc,check=False):
        try:
            if check:
                WebDriverWait(self.driver, 30, 0.5).until(EC.invisibility_of_element_located(loc))
                return self.driver.find_elements(*loc)

            WebDriverWait(self.driver, 30, 0.5).until(EC.visibility_of_element_located(loc))
            return self.driver.find_elements(*loc)
        except:
             logging.debug("页面上找不到{}元素".format(loc))



    def send_keys(self,loc,value,click_first=True,clear_first=True):
        try:
            loc=getattr(self,"_{}".format(loc))
            if click_first:
                self.driver.find_element(*loc).click()

            if clear_first:
                self.driver.find_element(*loc).clear()

            self.driver.find_element(*loc).send_keys(value)
        except AttributeError:
             logging.debug("页面上找不到{}元素".format(loc))

    def is_toast_exist(self,driver,text):
        try:
            text_loc=(By.XPATH,".//*[contains(@text,'{}')]".format(text))
            WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located(text_loc))
            return True
        except Exception as e:
            logging.debug(e)
            # print("页面上没有找到{}".format(text))
            return False

class StarPage(BasePage):

    '各种要需要用到的页面元素'
    account_login_loc=(By.XPATH,'//*[@text="Login with MeetU Account"]')

    facebook_login_loc=''

    google_login_loc=''

    def click_account_login(self):
        self.find_element(*self.account_login_loc).click()

    def click_facebook_login(self):
        self.find_element(*self.facebook_login_loc).click()

    def click_google_login(self):
        self.find_element(*self.google_login_loc).click()

class Account_login_page(BasePage):

    '各种要需要用到的页面元素'
    account_father_loc=(By.XPATH,'//*[@text="Email"]/..')
    account_loc=(By.CLASS_NAME,'android.widget.EditText')

    psw_father_loc=(By.XPATH,'//*[@text="Password"]/..')
    psw_loc=(By.CLASS_NAME,'android.widget.EditText')

    login_loc=(By.XPATH,'//*[@text="Continue"][@class="android.widget.TextView"]')

    forget_psw_loc=(By.XPATH,'//*[@text="I\'ve forgotten my password?]')

    sign_up_loc=(By.XPATH,'//*[@text="Sign up"]')

    account_format_error=(By.XPATH,'//*[@text="It doesn’t same to be an email."]')

    psw_empty_error=(By.XPATH,'//*[@text="No less than 6 characters]')


    def account_input(self,value):
        # self.send_keys(self.account_loc,value=value)
        return self.find_element(*self.account_father_loc).find_element(*self.account_loc).send_keys(value)

    def psw_input(self,value):
        # self.send_keys(self.account_loc,value=value)
        return self.find_element(*self.psw_father_loc).find_element(*self.psw_loc).send_keys(value)


    def click_forget_psw(self):
        self.find_element(*self.forget_psw_loc).click()

    def click_sign_up(self):
        self.find_element(*self.sign_up_loc).click()

    def click_login(self):
        self.find_element(*self.login_loc).click()

    def network_error_is_exist(self):
        return self.is_toast_exist(self.driver,'Network')

class Home_page(BasePage):
    '各种要需要用到的页面元素'
    match_card_title_loc = (By.XPATH, '//*[@text="Match"]')
    # permission_allow_loc = (By.XPATH, '//*[contain(@text,"始终允许")]')
    permission_allow_loc = (By.XPATH, '//*[@text="始终允许"]')

    guide_first_click_loc=(By.XPATH,'//*[@text="Try it"]')
    card_num_show_test_server_loc=(By.XPATH,'//*[contains(@text,"1/")]')


    def permission_allow(self):
        if self.find_elements(*self.permission_allow_loc):

            self.find_element(*self.permission_allow_loc).click()
            logging.debug('执行权限窗口点击')
        else:
            if "允许" in self.driver.page_source or "始终允许" in self.driver.page_source:
                self.driver.switch_to.alert.accept()
                logging.debug('执行权限运行')
            logging.debug('没有找到定位权限弹窗')

    def judge_login_success(self):

        result=self.find_elements(*self.match_card_title_loc)

        if result!=[]:
            return True
        else:
            return False

    def close_guide(self):

        if self.find_elements(*self.guide_first_click_loc):
            self.find_element(*self.guide_first_click_loc).click()

            for i in range(3):
                self.driver.keyevent(4)
                time.sleep(1)
        else:
             logging.debug('引导已关闭')

    def loading_finish_judge(self):
        if self.find_elements(*self.card_num_show_test_server_loc):
            return True
        else:
            logging.debug('卡片没有加载完成')
            return False