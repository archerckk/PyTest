from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


class Page(object):
    '页面抽象对象创建'
    login_url='http://mail.126.com'

    def __init__(self,selenium_driver,base_url=login_url):
        self.base_url=base_url
        self.driver=selenium_driver
        self.timeout=30

    def _open(self,url):
        self.url=self.base_url+url
        self.driver.get(url)

    def open(self):
        self._open(self.login_url)

    def find_element(self,*loc):
        return self.driver.find_element(*loc)

class Login_page(Page):

    url='/'

    user_loc=(By.NAME,'email')
    password_loc=(By.CLASS_NAME,'j-inputtext dlpwd')
    submit_loc=(By.ID,'dologin')



    def send_user_name(self,name):
        self.find_element(*self.user_loc).send_keys(name)

    def send_user_psw(self, psw):
        self.find_element(*self.password_loc).send_keys(psw)

    def click_sub(self):
        self.find_element(*self.submit_loc).click()


def test_login(driver,user,psw):
    login_page=Login_page(driver)
    login_page.open()
    sleep(5)
    login_frame = 'x-URS-iframe'
    driver.switch_to.frame(login_frame)
    login_page.send_user_name(user)
    login_page.send_user_psw(psw)
    login_page.click_sub()

def main():
    driver=webdriver.Chrome()

    # driver.get('http://www.baidu.com')
    user='archerckk'
    psw='a3203589'

    test_login(driver,user,psw)

    text=driver.find_element_by_id('spnUid').text
    assert (text=='archerckk@126.com'),'用户名称不匹配，登陆失败！！'

    driver.quit()


main()
