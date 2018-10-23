from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://www.baidu.com/baidu?tn=monline_3_dg&ie=utf-8&wd=京东物流订单号查询')
driver.find_element_by_css_selector("[class='c-input op_express_delivery_input_nu']").send_keys('VB49031481111')
# driver.find_element_by_class_name('c-input op_express_delivery_input_nu')#测试代码
driver.find_element_by_css_selector("[class='c-btn c-btn-primary c-gap-left-small op_express_delivery_submit']").click()
text = driver.find_element_by_xpath('//div[@class="op_express_delivery_timeline_title"]/div[2]').text
print(text)
driver.quit()
