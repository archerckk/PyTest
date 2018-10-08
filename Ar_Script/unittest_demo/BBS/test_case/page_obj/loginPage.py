from selenium.webdriver.common.by import By
from time import sleep
from .base import Page

class Login(Page):

    url='/'

    #网页元素定位loc
    # xpath写法"//div[@id='mzCust']/div/img"
    user_loc=(By.ID,'u')
    psw_loc=(By.ID,'p')
    submit_loc=(By.ID,'login_button')

    def login_username(self,username):
        return self.find_element(*self.user_loc).send_keys(username)

    def login_password(self,password):
        return self.find_element(*self.psw_loc).send_keys(password)

    def login_submit(self):
        return self.find_element(*self.submit_loc).click()

    def user_login(self,username='username',password='psw'):
        self.open()
        self.driver.refresh()
        sleep(3)
        self.driver.switch_to.frame('login_frame')
        self.login_username(username)
        self.login_password(password)
        self.login_submit()
        sleep(3)

    error_msg_loc=(By.ID,'err_m')
    success_msg_loc=(By.ID,'useraddr')

    def username_error_msg(self):
        return self.find_element(*self.err_msg_loc).text

    def psw_error_msg(self):
        return self.find_element(*self.err_msg_loc).text

    def success_msg(self,username):
        assert self.find_element(*self.success_msg_loc).text==username+'@qq.com'
        return '登录成功'
