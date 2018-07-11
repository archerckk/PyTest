from selenium import webdriver
from ar_188_测试_公共模块 import Public
import time

class Login_test:

    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get('http://mail.qq.com')

    def login_137(self):
        account='137160564'
        psw='chaoheweijing'
        Public().login_two(self.driver,account,psw)
        self.driver.quit()

    def login_501(self):
        account='501824353'
        psw='fengmang3729'
        Public().login_two(self.driver,account,psw)
        self.driver.quit()


if __name__ == '__main__':
    Login_test().login_137()
    time.sleep(5)
    Login_test().login_501()