from appium import webdriver
import json
import time

with open('./resources/phone.json')as f:
    desired_caps = json.load(f)['sanxingc8_prison']

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.implicitly_wait(20)
print('等待完成')
while True:
    driver.tap(positions=[(441,49)])
