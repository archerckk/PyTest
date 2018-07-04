from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from  selenium.webdriver.common.actions import key_actions

driver=webdriver.Chrome()
driver.get('httP://www.baidu.com')

search_window=driver.current_window_handle

tieba=driver.find_element_by_link_text('贴吧')
tieba.send_keys(Keys.CONTROL,Keys.ENTER)
time.sleep(2)
print('现在的窗口是：%s'%driver.title)


for handle in driver.window_handles:
    if handle!=search_window:
        driver.switch_to.window(handle)
        print('现在的窗口是：%s'%driver.title)
        driver.find_element_by_id('wd1').send_keys('海贼王')
        time.sleep(2)


for handle in driver.window_handles:
    if handle==search_window:
        driver.switch_to.window(handle)
        print('现在的窗口是：%s'%driver.title)
        driver.find_element_by_id('kw').send_keys('Selenium')
        driver.find_element_by_id('su').click()
        time.sleep(2)

driver.quit()


