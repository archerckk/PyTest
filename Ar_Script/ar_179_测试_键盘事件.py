from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
driver.get('http://www.baidu.com')

target=driver.find_element_by_id('kw')
target.send_keys('Seleniumm')
target.send_keys(Keys.BACK_SPACE)
target.send_keys(Keys.SPACE)
target.send_keys('教程')
target.send_keys(Keys.CONTROL,'a')
target.send_keys(Keys.CONTROL,'x')
target.send_keys(Keys.CONTROL,'v')
target.click()
time.sleep(3)

driver.quit()

