from selenium import webdriver
from time import sleep
import os

driver=webdriver.Chrome()
driver.get('http://www.baidu.com')


driver.find_element_by_id('kw').send_keys('调用JavaScript')
driver.find_element_by_id('su').click()
sleep(3)
driver.set_window_size(600,600)
sleep(3)
js='window.scrollTo(200,450);'
driver.execute_script(js)
sleep(3)
driver.get_screenshot_as_file(os.getcwd()+os.sep+'滚动条截图.png')

driver.quit()