from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from appium import webdriver

class BasePage(object):

    def __init__(self,driver):
        self.driver=driver

    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,30,0.5).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except :
            print("页面上找不到{}元素".format(loc))

    def find_elements(self, *loc):
        try:
            WebDriverWait(self.driver, 30, 0.5).until(EC.visibility_of_element_located(loc))
            return self.driver.find_elements(*loc)
        except:
            print("页面上找不到{}元素".format(loc))

    def send_keys(self,loc,value,click_first=True,clear_first=True):
        try:
            loc=getattr(self,"_{}".format(loc))
            if click_first:
                self.driver.find_element(*loc).click()

            if clear_first:
                self.driver.find_element(*loc).clear()

            self.driver.find_element(*loc).send_keys(value)
        except AttributeError:
            print("页面上找不到{}元素".format(loc))

    def is_toast_exist(self,driver,text):
        try:
            text_loc=(By.XPATH,".//*[contains(@text,'{}')]".format(text))
            WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located(text_loc))
            return True
        except Exception as e:
            print(e)
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

    login_loc=(By.XPATH,'//*[@text="Continue"]')

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