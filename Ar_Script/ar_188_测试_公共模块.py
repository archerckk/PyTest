import time
class Public:

    def __init__(self):
        self.account='137160564'
        self.psw='chaoheweijing'


    def login_one(self,driver):
        print(driver.title)
        driver.switch_to.frame('login_frame')
        driver.find_element_by_id('u').clear()
        driver.find_element_by_id('u').send_keys(self.account)
        driver.find_element_by_id('p').clear()
        driver.find_element_by_id('p').send_keys(self.psw)
        driver.find_element_by_id('login_button').click()

    def login_two(self,driver,account,psw):
        # print(driver.title)
        driver.switch_to.frame('login_frame')
        driver.find_element_by_id('u').clear()
        driver.find_element_by_id('u').send_keys(account)
        driver.find_element_by_id('p').clear()
        driver.find_element_by_id('p').send_keys(psw)
        driver.find_element_by_id('login_button').click()
        time.sleep(5)
        print('登陆账号：【%s】成功！'%driver.find_element_by_id('useraddr').text)


    def quit_test(self,driver):
        driver.find_element_by_link_text('退出').click()
        print(driver.title)
        driver.quit()