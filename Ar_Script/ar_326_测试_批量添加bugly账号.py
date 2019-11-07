from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup

driver=webdriver.Chrome()
driver.get('https://bugly.qq.com/v2/workbench/apps')
time.sleep(3)
driver.switch_to.frame('ptlogin_iframe')
login=driver.find_element_by_id('switcher_plogin').click()

time.sleep(1)
driver.find_element_by_id('u').send_keys('644326394')
driver.find_element_by_id('p').send_keys('archer3203589')
driver.find_element_by_id('login_button').click()

time.sleep(3)
# content=driver.page_source
# print(content)
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'}
# r=requests.get(url,headers=headers)
# with open('resources/bugly_page.txt','wb')as f:
#     for i in r.iter_content(128):
#         f.write(i)



tbody=driver.find_elements_by_tag_name('tbody')
# tr_list=tbody.find_elements_by_tag_name('tr')
for i in tbody:
    print(i)



time.sleep(2)



driver.quit()