from selenium import webdriver
from Ar_Script.review.auto_test_account_info import Public
from time import sleep

class Mail_Login:

    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get('http://mail.qq.com')
        self.driver.refresh()

    def login_1(self):
        account='137160564'
        password='chaoheweijing'
        Public().login_option(self.driver,account,password)
        sleep(5)
        try:
            print('【%s】'%self.driver.find_element_by_id('useraddr').text+'登陆成功')
        except:
            print('登陆失败')
        self.driver.quit()

    def login_2(self):
        account = '501824353'
        password = 'fengmang3729'
        Public().login_option(self.driver, account, password)
        sleep(5)
        try:
            print('【%s】'%self.driver.find_element_by_id('useraddr').text+'登陆成功')
        except:
            print('登陆失败')
        self.driver.quit()

if __name__ == '__main__':
    Mail_Login().login_1()
    Mail_Login().login_2()
