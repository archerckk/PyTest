from selenium import webdriver
import time

driver=webdriver.Chrome()
url='https://bugly.qq.com/v2/workbench/apps'
driver.get(url)
time.sleep(3)

driver.switch_to.frame('ptlogin_iframe')
login=driver.find_element_by_id('switcher_plogin').click()
err_file=0
start=time.time()

time.sleep(1)
driver.find_element_by_id('u').send_keys('644326394')
driver.find_element_by_id('p').send_keys('archer3203589')
driver.find_element_by_id('login_button').click()

driver.implicitly_wait(10)

time.sleep(3)
# driver.maximize_window()
td_list=driver.find_elements_by_xpath('//table[@class="_2GYnFmdn3vK6enKXmFAHlm"]/tbody/tr/td[4]/div[@class="_2rvEJCOJkSOAnedi51Lh59"]/a')
length=len(td_list)
if length==0:
    print('获取产品信息列表失败')
else:
    print("总共需要添加的产品数为：{}".format(length))

for i in range(length):
    tmp_list=driver.find_elements_by_xpath('//table[@class="_2GYnFmdn3vK6enKXmFAHlm"]/tbody/tr/td[4]/div[@class="_2rvEJCOJkSOAnedi51Lh59"]/a')

    print("添加到第{}个产品".format(i+1))

    driver.implicitly_wait(1)
    try:
        tmp_list[i].click()

        driver.implicitly_wait(10)

        # 点击邀请成员按钮
        driver.find_element_by_xpath('//div[@class="_2fpeF363eRJEYpWKWIkdiD"]/div/a').click()

        driver.find_element_by_xpath('//textarea[@id="invitation"]').send_keys('827428621')

        driver.find_element_by_xpath('//div[@class="_2p7MRFnMyxEZ-QTDCZj6yj"]/span').click()
        driver.find_element_by_xpath(
            '//div[@class="_2l5iy6-nPK2wBjuXLwu2md"]/div[@class="btn btn_blue _3A4-QJzKA7VLAsRmrbN3a_ false"]').click()

        time.sleep(1)

    except Exception as e:
        print("添加第{}个产品失败,错误信息为：{}\n".format(i+1,e))
        err_file+=1
        driver.get(url)
        continue

    driver.get(url)
    driver.implicitly_wait(60)

print("添加成功：{}个产品，失败：{}个产品,执行时间为{}".format(length-err_file,err_file,time.time()-start))
driver.quit()