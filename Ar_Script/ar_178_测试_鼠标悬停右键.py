from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver=webdriver.Chrome()
driver.get('http://www.baidu.com')

'获取悬停的元素位置'
float_factor=driver.find_element_by_link_text('设置')
ActionChains(driver).move_to_element(float_factor).perform()
time.sleep(5)

'获取右击的元素位置'
right_click=driver.find_element_by_link_text('新闻')
ActionChains(driver).context_click(right_click).perform()
time.sleep(5)

driver.quit()
