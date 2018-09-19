from selenium import  webdriver
import os
import time

driver=webdriver.Chrome()
driver.get('http:www.baidu.com')

driver.find_element_by_id('kw').send_keys('Selenium')
driver.find_element_by_id('su').click()
time.sleep(5)
driver.get_screenshot_as_file(os.getcwd()+os.sep+'测试截图.jpg')

driver.quit()