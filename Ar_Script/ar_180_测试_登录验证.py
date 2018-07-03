from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get('https://mail.qq.com/')

account='137160564'
psw='chaoheweijing'
title=driver.title
url=driver.current_url

print('-'*100)
print('登录前标题：%s'%title)
print('登录前网址：%s'%url)

driver.switch_to.frame('login_frame')
driver.find_element_by_id('u').clear()
driver.find_element_by_id('u').send_keys(account)
driver.find_element_by_id('p').clear()
driver.find_element_by_id('p').send_keys(psw)
driver.find_element_by_id('login_button').click()
time.sleep(5)

title=driver.title
url=driver.current_url


print('-'*100)
print('登录后标题：%s'%title)
print('登录后网址：%s'%url)
user=driver.find_element_by_id('useraddr').text
print('登录的账号为：%s'%user)

driver.quit()