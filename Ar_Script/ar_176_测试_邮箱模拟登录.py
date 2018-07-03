from selenium import webdriver
import time

driver=webdriver.Chrome()

driver.get('http://mail.qq.com')
account='137160564'
psw='chaoheweijing'
# pp='a3203589'

'QQ邮箱登录'
'先选中对应的框架，然后才能进行元素的定位'
driver.switch_to.frame('login_frame')
driver.find_element_by_id('u').clear()
driver.find_element_by_id('u').send_keys(account)
driver.find_element_by_id('p').clear()
driver.find_element_by_id('p').send_keys(psw)
driver.find_element_by_id('login_button').click()
time.sleep(5)


'126测试代码'
'先选中对应的框架，然后才能进行元素的定位'
# driver.get('https://mail.126.com/')
# driver.switch_to.frame('x-URS-iframe')
# driver.find_element_by_xpath("//input[@name='email' and @class='j-inputtext dlemail']").send_keys('archerckk')
# driver.find_element_by_xpath("//input[@name='password' and @class='j-inputtext dlpwd']").send_keys('a3203589')
# driver.find_element_by_id('dologin').click()
# time.sleep(5)


# driver.quit()