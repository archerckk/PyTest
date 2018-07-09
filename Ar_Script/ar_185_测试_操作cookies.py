from selenium import webdriver

driver=webdriver.Chrome()
driver.get('http://youdao.com')

cookie=driver.get_cookies()

driver.add_cookie({'name':'test','value':'test'})

for i in driver.get_cookies():
    print(i)
driver.delete_cookie('test')

print('删除之后的cookie为：')
for i in driver.get_cookies():
    print(i)

driver.quit()
