import json
from appium import  webdriver

# driver=webdriver()

# def end(level):
#     return '  '*level+'-'
#
# def start(level):
#     return '  '*level+'+'
#
# def find_dict(target,level):
#     keys=iter(target)
#     for i in keys:
#         if type(target[i])is not dict:
#             if type(target[i])is list:
#                 find_dict(target[i])
#             else:
#                 print(end(level) + i + ':' + str(target[i]))
#
#         else:
#             next_level=level+1
#             print(start(level)+i)
#             find_dict(target[i],next_level)
#
#
# def main():
#     target=input()
#     target=json.loads(target)
#     find_dict(target,1)

#coding=utf-8


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.0.1'
desired_caps['deviceName'] = 'LGD8587de68c9'
desired_caps['appPackage'] = 'com.android.calculator2'
desired_caps['appActivity'] = '.Calculator'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.find_element_by_name("1").click()
driver.find_element_by_name("5").click()
driver.find_element_by_name("9").click()
driver.find_element_by_name("delete").click()
driver.find_element_by_name("9").click()
driver.find_element_by_name("5").click()
driver.find_element_by_name("+").click()
driver.find_element_by_name("6").click()
driver.find_element_by_name("=").click()

driver.quit()


# if __name__ == '__main__':
#     main()