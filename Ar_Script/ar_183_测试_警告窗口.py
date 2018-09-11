from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver=webdriver.Chrome()
driver.get('http://www.baidu.com')

option=driver.find_element_by_link_text('设置')

ActionChains(driver).move_to_element(option).perform()

driver.find_element_by_link_text('搜索设置').click()
time.sleep(2)
# driver.find_element_by_xpath("//div[@id='gxszButton']/a[@class='prefpanelgo']").click()
driver.find_element_by_class_name('prefpanelgo').click()

# driver.find_element_by_xpath('//*[@id="gxszButton"]/a[1]').click()

# time.sleep(2)
print(driver.switch_to_alert().text)

driver.switch_to_alert().accept()

time.sleep(2)

driver.find_element_by_id('kw').send_keys('测试内容')
driver.find_element_by_id('su').click()

print(driver.title)
time.sleep(2)

driver.quit()