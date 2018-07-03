from selenium import webdriver
from time import sleep,ctime
from selenium.common.exceptions import NoSuchElementException

driver=webdriver.Chrome()


'显示等待'
# driver.get('http://www.baidu.com')
# print(ctime())
#
# for i in range(10):
#     try:
#         element = driver.find_element_by_id('kw22')
#         if element.is_displayed():
#             break
#     except:pass
#     sleep(1)
# else:
#     print('timeout')
#
# print(ctime())

'隐式等待'

driver.implicitly_wait(10)
driver.get('http://www.baidu.com')

try:
    print(ctime())
    driver.find_element_by_id('kw22')
except NoSuchElementException as e:
    print(e)
finally:
    print(ctime())


driver.quit()