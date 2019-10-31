#encoding=utf-8
import requests
from bs4 import BeautifulSoup
import re

"""
作业1：

url :"http://money.163.com/special/002534NU/house2010.html"
抓取第一页的新闻信息，并按照以下规格输出。

[

  {'title':'生鲜电商为何难盈利？','created_at':'2013-05-03 08:43','url':'http://money.163.com/13/0503/08/8TUHSEEI00254ITK.html'}

  {'title':'生鲜电商为何难盈利？','created_at':'2013-05-03 08:43','url':'http://money.163.com/13/0503/08/8TUHSEEI00254ITK.html'}


]
"""

"""
1、先将网页的整体内容抓取下来
2、分析网页的内容，将要保留的东西保存到对应的数据结构
"""
url="http://money.163.com/special/002534NU/house2010.html"

result_list=[]

body=requests.get(url)
html_content=body.text
soup=BeautifulSoup(html_content,'html.parser')


reg_link=re.compile(r'<a href="(.+)">(.+)</a>',re.DOTALL)
reg_time=re.compile(r'<span class="time">(.+)</span>')
result=re.findall(reg_link,html_content)


div_list=soup.find_all('div',class_='list_item clearfix')
for i in div_list:
    dict_item = {}
    link=reg_link.match(str(i.h2.a)).group(1)
    title=reg_link.match(str(i.h2.a)).group(2)
    time_value=reg_time.match(str(i.p.span)).group(1)

    dict_item['title']=title
    dict_item['time']=time_value
    dict_item['url']=link

    result_list.append(dict_item)

for i in result_list:
    print(i)



"""
作业2：

url: "http://search.jd.com/Search?keyword=%E5%B9%BC%E7%8C%AB%E7%8C%AB%E7%B2%AE&enc=utf-8#filter"


print jd_search(keyword)

[dict,dict,dict]
dict {pic:'',title:'',price:'',url:''}




"""