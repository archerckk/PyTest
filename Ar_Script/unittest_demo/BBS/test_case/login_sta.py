from time import sleep
import unittest,random,sys
sys.path.append('./models')
sys.path.append('./page_obj')
from models import function,myunit
from page_obj.loginPage import Login


class LoginTest(myunit.MyTest):
    '账户登录测试'

    def user_login_verify(self,username='',password=''):
        Login(self.driver).user_login(username,password)

    # def test_login1(self):
    #     '错误账号'
    #     self.user_login_verify(username='123',password='')
    #     po=Login(self.driver)
    #
    #     # self.assertEqual(po.username_error_msg,'请输入正确的帐号！')
    #     sleep(1)
    #     print(po.username_error_msg)
    #     file_cur=function.insert_img(self.driver,'账号错误.png')
    #     print(file_cur)

    # def test_login2(self):
    #     '正确账号，错误密码'
    #     self.user_login_verify(username='137160564',password='123')
    #     po=Login(self.driver)
    #     sleep(1)
    #     function.insert_img(self.driver,'正确账号，错误密码.png')
    #
    # def test_login3(self):
    #     '正确账号，密码输入为空'
    #     self.user_login_verify(username='644326394',password='')
    #     po = Login(self.driver)
    #     sleep(1)
    #     function.insert_img(self.driver, '正确账号，密码输入为空.png')
    #
    def test_login4(self):
        '正确整好，正确密码'
        self.user_login_verify(username='137160564', password='chaoheweijing')
        # self.user_login_verify(username='137160564', password='fengmang3729')
        po = Login(self.driver)
        sleep(1)
        # print(po.success_msg)
        po.success_msg('137160564')
        # self.assertEqual(po.success_msg)
        function.insert_img(self.driver, '正确登录.png')

if __name__ == '__main__':
    unittest.main()