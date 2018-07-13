import csv
from selenium import webdriver
import time

'''
1.先从csv文件里面拿到账号跟密码
2.定位到对应的标签输入对应的值
3.登录成功后打印登录的账号
4.退出账号
5.重新打开并且登录
'''
class Login:

    def __init__(self):
        self.data=csv.reader(open('resources/test_account.csv','r'))



    def account_login(self):
        for account in self.data:
            self.driver = webdriver.Chrome()
            self.driver.get('http://mail.qq.com')
            self.driver.switch_to.frame('login_frame')
            self.driver.find_element_by_id('u').clear()
            self.driver.find_element_by_id('u').send_keys(account[1])
            self.driver.find_element_by_id('p').clear()
            self.driver.find_element_by_id('p').send_keys(account[2])
            self.driver.find_element_by_id('login_button').click()
            time.sleep(5)
            print('登录账号：【%s】成功'%self.driver.find_element_by_id('useraddr').text)
            self.driver.quit()

if __name__ == '__main__':
    login=Login()
    login.account_login()

