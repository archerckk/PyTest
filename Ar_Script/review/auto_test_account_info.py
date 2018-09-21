from selenium import webdriver
from time import sleep


class Public:

    def __init__(self):
        self.account='137160564'
        self.psw='chaoheweijing'

    def login(self,driver):
        driver.switch_to.frame('login_frame')
        driver.find_element_by_id('u').clear()
        driver.find_element_by_id('u').send_keys(self.account)
        driver.find_element_by_id('p').clear()
        driver.find_element_by_id('p').send_keys(self.psw)
        driver.find_element_by_id('login_button').click()

    def login_option(self,driver,account,password):
        driver.switch_to.frame('login_frame')
        driver.find_element_by_id('u').clear()
        driver.find_element_by_id('u').send_keys(account)
        driver.find_element_by_id('p').clear()
        driver.find_element_by_id('p').send_keys(password)
        driver.find_element_by_id('login_button').click()

    def web_quit(self,driver):
        driver.find_element_by_link_text('退出').click()
        print(driver.title)
        driver.quit()
