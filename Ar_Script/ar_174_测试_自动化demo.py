from selenium import  webdriver

driver=webdriver.Chrome()

driver.get('http://www.baidu.com')

# driver.find_element_by_id('kw').send_keys('Selenium2')
# driver.find_element_by_id('su').click()
# driver.find_element_by_link_text('贴吧').click()

# driver.find_element_by_xpath("//input[@id='kw' and @name='wd']").send_keys('测试内容')
driver.find_element_by_css_selector("form#form>span>input#kw").send_keys('测试内容')
driver.quit()