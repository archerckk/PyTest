from selenium import webdriver
import time

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
account='archerckk'
psw='a3203589'

driver=webdriver.Chrome()
driver.get('http://www.126.com')

driver.switch_to.frame('x-URS-iframe')

driver.find_element_by_xpath('//div[@id="account-box"]/div[@class="u-input box"]/input[@class="j-inputtext dlemail"]').send_keys(account)
driver.find_element_by_xpath('//input[@name="password" and @class="j-inputtext dlpwd"]').send_keys(psw)

driver.find_element_by_id('dologin').click()

time.sleep(7)

driver.quit()