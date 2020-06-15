from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import re
import sys
sys.getdefaultencoding()
from Ar_Script import ar_073_类和对象_点和直线
from selenium import webdriver
import json
import time

# import test

# def ab():
#     print("y")
# test.cd()
# a=ar.Const()
# a.NAME="abc"
# print(a.NAME)

# # list1=[1,2,3,4,5]
# for i in list(map(lambda x:x+1,range(1,6))):
#     print(i)

# "爬虫第三讲，课后练习1答案"
# def search_baike():
#     keyword="斗破苍穹"
#     keyword=urllib.parse.urlencode({"word":keyword})
#     head = {}
#     head["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0"
#     url="https://baike.baidu.com/search/word?%s"%keyword
#     print(url)
#     req=urllib.request.Request(url,headers=head)
#     "自己顺序搞错了，第二个参数并不是headers，然后传个字典进去当然就是报错了"
#     response=urllib.request.urlopen(req)
#     html=response.read()
#     soup=BeautifulSoup(html,"html.parser")
#
#     for each in soup.find_all(href=re.compile("view")):
#         content="".join([each.text])
#         url2="".join(["https://baike.baidu.com",each["href"]])
#
#         response2=urllib.request.urlopen(url2)
#         html2=response2.read()
#         soup2=BeautifulSoup(html2,"html.parser")
#
#         if soup2.h2:
#             content="".join([content,soup2.h2.text])
#         content="".join([content,"-->",url2])
#         print(content)
#
#
#
# if __name__ == "__main__":
#     search_baike()

# test1=ar_073_类和对象_点和直线.Point(1,2)
# print(test1.getX())
#
# driver=webdriver.Chrome()
# driver.switch_to.default_content()


test_json=[
    {
        "name":"tom",
        "power":100,
        "hp":100
    },
    {
        "name": "li lei",
        "power": 100,
        "hp": 100
    }
]

test_string="""[
    {
        "name":"tom",
        "power":100,
        "hp":100
    },
    {
        "name": "li lei",
        "power": 100,
        "hp": 100
    }
]
"""
#将json对象保存到文件当中
# with open("Answer/test_result.json","w")as f:
#     json.dump(test_json,fp=f)

#json文件内容读取出来
# with open("Answer/test_result.json","r")as f:
#     print(json.load(f))

#文件对象转化为字符串
a=json.dumps(test_json)
# print(a=json.dumps(test_json, indent=4, sort_keys=True))

# print(type(a))
#
# b=json.loads(test_string)
# print("b的类型为:",type(b))
# print(b)
#
# def test_selenium():
#     driver=webdriver.Chrome()
#     driver.get("https://www.baidu.com")
#     time.sleep(3)
#     driver.quit()
#
# # test_selenium()
#
#
class Test_demo(object):

    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_title(self):
        self.driver.get('https://testerhome.com/')
        time.sleep(3)

        self.driver.find_element_by_link_text('社团').click()
        time.sleep(3)

        self.driver.find_element_by_link_text('霍格沃兹测试学院').click()

        time.sleep(5)

        info_list_loc="//div[contains(@class,'title media-heading')]"
        info_list=self.driver.find_elements_by_xpath(info_list_loc)
        print(info_list[0])#元素是可以正常打印的
        # info_list[0].find_element_by_class_name('a').click()#报错
        print(info_list[0].is_enabled())
        time.sleep(5)
        info_list[0].click()
        time.sleep(2)


        # info_list_loc = "div.media-heading"
        # info_list = self.driver.find_elements_by_css_selector(info_list_loc)
        # # self.driver.find_element_by_class_name()
        # print(info_list[0])  # 元素是可以正常打印的
        # info_list[0].click()  # 报错
        # time.sleep(2)


# driver=webdriver.Chrome()
# driver.implicitly_wait(5)
# driver.maximize_window()
# driver.get('https://testerhome.com/')
# time.sleep(3)
# driver.find_element_by_link_text('社团').click()
# time.sleep(3)
# driver.find_element_by_link_text('霍格沃兹测试学院').click()
# time.sleep(3)
# info_list_loc="div.media-heading"
# info_list=driver.find_elements_by_css_selector(info_list_loc)
# # self.driver.find_element_by_class_name()
# print(info_list[0])#元素是可以正常打印的
# info_list[0].click()#报错
# time.sleep(2)