from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get('http://youdao.com/')

# driver.find_element_by_link_text('下载词典客户端').click()
driver.find_element_by_xpath("//input[@placeholder='在此输入要翻译的单词或文字']").send_keys('hello')
driver.find_element_by_xpath("//input[@placeholder='在此输入要翻译的单词或文字']").submit()

time.sleep(3)
driver.quit()