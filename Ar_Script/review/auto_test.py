from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import os
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
# driver=webdriver.Chrome()
# driver.get('http://www.baidu.com')
# driver.implicitly_wait(10)
#
# print(ctime())
#
# try:
#     driver.find_element_by_id('kw')
# except NoSuchElementException as e:
#     print(e)
# finally:
#     print(ctime())
#
# driver.quit()

'窗口切换'
# driver=webdriver.Chrome()
# driver.get('http://www.baidu.com')
#
# search_element=driver.find_element_by_link_text('贴吧')
# search_element.send_keys(Keys.CONTROL,Keys.ENTER)
# current_handle=driver.current_window_handle
# print(driver.title)
#
# for handle in driver.window_handles:
#     if handle!=current_handle:
#         driver.switch_to.window(handle)
#         driver.find_element_by_id('wd1').send_keys('海贼王')
#         driver.find_element_by_link_text('进入贴吧').click()
#         sleep(2)
# print(driver.title)
#
# for handle in driver.window_handles:
#     if handle==current_handle:
#         driver.switch_to.window(current_handle)
#         driver.find_element_by_id('kw').send_keys('Selenium2')
#         driver.find_element_by_id('su').click()
#         sleep(2)
# print(driver.title)
#
# driver.quit()


'警告窗口处理'
# driver=webdriver.Chrome()
# driver.get('http://www.baidu.com')
#
# element=driver.find_element_by_link_text('设置')
# ActionChains(driver).move_to_element(element).perform()
# driver.find_element_by_link_text('搜索设置').click()
# sleep(3)
# driver.find_element_by_link_text('保存设置').click()
# sleep(2)
# print(driver.switch_to_alert().text)
# driver.switch_to_alert().accept()
#
# driver.find_element_by_id('kw').send_keys('selenium 教程')
# driver.find_element_by_id('su').click()
# sleep(2)
# print(driver.title)
#
# driver.quit()


'实现下载文件'
# cp=webdriver.ChromeOptions()
# prefs={'profile_default_content_popups':0,'download_default_directory':os.getcwd()}
# cp.add_experimental_option('prefs',prefs)
#
# driver=webdriver.Chrome(chrome_options=cp)
# driver.get('https://pypi.org/project/selenium/#files')
#
#
# driver.find_element_by_link_text('selenium-3.14.0.tar.gz').click()
#
# sleep(5)
# driver.quit()

'操作cookies'
# driver=webdriver.Chrome()
# driver.get('http://www.youdao.com')
#
# cookies=driver.get_cookies()
# for i in cookies:
#     print(i)
#
# print()
# driver.add_cookie({'name':'test','value':'123456'})
#
# for i in driver.get_cookies():
#     print(i)
# print()
# driver.delete_cookie('test')
#
# for i in driver.get_cookies():
#     print(i)
#
# driver.quit()

'调用公共模块'
from Ar_Script.review.auto_test_account_info import Public
from time import sleep

driver=webdriver.Chrome()
driver.get('http://mail.qq.com')
driver.refresh()
driver.implicitly_wait(5)

public=Public()

public.login(driver)
sleep(5)
public.web_quit(driver)