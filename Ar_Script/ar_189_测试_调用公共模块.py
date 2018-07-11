from selenium import webdriver
from Ar_Script.ar_188_测试_公共模块 import Public
import time

driver=webdriver.Chrome()
driver.get('http://mail.qq.com')

Public().login_one(driver)
time.sleep(5)
Public().quit_test(driver)