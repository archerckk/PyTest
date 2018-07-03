from selenium import webdriver

driver=webdriver.Chrome()

first_url='http://www.baidu.com'
driver.get(first_url)
print('当前网页为：%s'%first_url)

second_url='http://news.baidu.com'
driver.get(second_url)
print('当前网页为:%s'%second_url)

driver.back()
print('返回到网页：%s'%first_url)

driver.forward()
print('前进到网页：%s'%second_url)

driver.refresh()
print('刷新当前网页')
driver.quit()