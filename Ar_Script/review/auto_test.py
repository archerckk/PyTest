from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
from time import ctime,sleep

'demo代码'
# driver=webdriver.Chrome()
#
# driver.get('http://www.baidu.com')
#
# driver.find_element_by_id('kw').send_keys('selenium2')
# driver.find_element_by_id('su').click()
#
# time.sleep(5)
#
# driver.quit()


'控制浏览器的前进后退'
# driver=webdriver.Chrome()
#
# driver.get('http://www.baidu.com')
#
# print('当前的网页标题为：%s'%driver.title)
#
# driver.get('http://news.baidu.com')
#
# print('当前的网页标题为：%s'%driver.title)
#
# driver.back()
#
# print('当前的网页标题为：%s'%driver.title)
#
# driver.forward()
#
# print('当前的网页标题为：%s'%driver.title)
#
# driver.refresh()
#
# print('当前的网页标题为：%s'%driver.title)
#
# time.sleep(3)
# driver.quit()

'模拟126邮箱登录'
# account='archerckk'
# psw='a3203589'
#
# driver=webdriver.Chrome()
# driver.get('http://www.126.com')
#
# driver.switch_to.frame('x-URS-iframe')
#
# driver.find_element_by_xpath('//div[@id="account-box"]/div[@class="u-input box"]/input[@class="j-inputtext dlemail"]').send_keys(account)
# driver.find_element_by_xpath('//input[@name="password" and @class="j-inputtext dlpwd"]').send_keys(psw)
#
# driver.find_element_by_id('dologin').click()
#
# time.sleep(7)
#
# driver.quit()

# '鼠标事件加键盘事件'
# driver = webdriver.Chrome()
# driver.get('http://www.baidu.com')
# option = driver.find_element_by_link_text('设置')
# map = driver.find_element_by_link_text('地图')
# target = driver.find_element_by_id('kw')
#
# '将鼠标移动到设置项'
# ActionChains(driver).move_to_element(option).perform()
# time.sleep(3)
#
# '鼠标右键'
# ActionChains(driver).context_click(map).perform()
# time.sleep(3)
#
# target.send_keys('Selenium2')
# target.send_keys(Keys.BACK_SPACE)
# target.send_keys(Keys.SPACE)
# target.send_keys('教程')
# target.send_keys(Keys.CONTROL, 'A')
# target.send_keys(Keys.CONTROL, 'X')
# target.send_keys(Keys.CONTROL, 'V')
# target.click()
#
# time.sleep(2)
# driver.quit()

'显式等待'
# driver=webdriver.Chrome()
# driver.get('http://www.baidu.com')
# print(ctime())
#
# for i in range(10):
#     try:
#         element=driver.find_element_by_id('kw22')
#         if element.is_displayed():
#             break
#     except:pass
#     sleep(1)
# print('timeout')
# print(ctime())

'隐式等待'
driver=webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.implicitly_wait(10)

print(ctime())

try:
    driver.find_element_by_id('kw')
except NoSuchElementException as e:
    print(e)
finally:
    print(ctime())

driver.quit()


