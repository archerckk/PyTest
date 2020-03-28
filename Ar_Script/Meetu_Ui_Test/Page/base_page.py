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

    def send_keys(self,loc,value,click_first,clear_first):
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
            WebDriverWait(driver,30,0.5).until(EC.visibility_of_element_located(text_loc))
            return True
        except Exception as e:
            print(e)
            # print("页面上没有找到{}".format(text))
            return False