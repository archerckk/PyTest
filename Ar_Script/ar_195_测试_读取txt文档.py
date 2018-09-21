import os
from selenium import webdriver
from time import sleep

"""
1.打开txt文档，获取到里面文档的数据
2.遍历这些数据，将这些数据放进去参数里面
3.循环执行登陆脚本
"""

class Txt_login:

    def __init__(self):
        with open('resources/account.txt','r')as account:
            self.lines=account.readlines()

    def login(self):
        for line in self.lines:
            (user_name,password)=line.split(',')

            self.driver = webdriver.Chrome()
            self.driver.get('http://mail.qq.com')
            self.driver.switch_to.frame('login_frame')
            self.driver.find_element_by_id('u').clear()
            self.driver.find_element_by_id('u').send_keys(user_name)
            self.driver.find_element_by_id('p').clear()
            self.driver.find_element_by_id('p').send_keys(password)
            self.driver.find_element_by_id('login_button').click()
            sleep(5)
            print('登录账号：【%s】成功' % self.driver.find_element_by_id('useraddr').text)
            self.driver.quit()

if __name__ == '__main__':
    Txt_login().login()