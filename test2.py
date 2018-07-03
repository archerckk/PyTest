from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import re
import sys
sys.getdefaultencoding()
from Ar_Script import ar_073_类和对象_点和直线
from selenium import webdriver


# import test

# def ab():
#     print('y')
# test.cd()
# a=ar.Const()
# a.NAME='abc'
# print(a.NAME)

# # list1=[1,2,3,4,5]
# for i in list(map(lambda x:x+1,range(1,6))):
#     print(i)

# '爬虫第三讲，课后练习1答案'
# def search_baike():
#     keyword='斗破苍穹'
#     keyword=urllib.parse.urlencode({'word':keyword})
#     head = {}
#     head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0'
#     url='https://baike.baidu.com/search/word?%s'%keyword
#     print(url)
#     req=urllib.request.Request(url,headers=head)
#     '自己顺序搞错了，第二个参数并不是headers，然后传个字典进去当然就是报错了'
#     response=urllib.request.urlopen(req)
#     html=response.read()
#     soup=BeautifulSoup(html,'html.parser')
#
#     for each in soup.find_all(href=re.compile('view')):
#         content=''.join([each.text])
#         url2=''.join(['https://baike.baidu.com',each['href']])
#
#         response2=urllib.request.urlopen(url2)
#         html2=response2.read()
#         soup2=BeautifulSoup(html2,'html.parser')
#
#         if soup2.h2:
#             content=''.join([content,soup2.h2.text])
#         content=''.join([content,'-->',url2])
#         print(content)
#
#
#
# if __name__ == '__main__':
#     search_baike()

test1=ar_073_类和对象_点和直线.Point(1,2)
print(test1.getX())

driver=webdriver.Chrome()
driver.switch_to.default_content()