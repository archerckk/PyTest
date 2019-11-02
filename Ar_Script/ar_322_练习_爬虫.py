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

try:
    body=requests.get(url)
except requests.exceptions.ConnectionError:
    raise requests.exceptions.ConnectionError

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

def jd_search(keyword):
    url="https://search.jd.com/Search?keyword={}&enc=utf-8#filter".format(keyword)
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'}

    try:
        response=requests.get(url,headers=headers)
    except requests.exceptions.ConnectionError:
        return '网络存在异常，无法访问'

    response.encoding = response.apparent_encoding
    html_text=response.text

    if "抱歉，没有找到" in html_text:
        return "没有找到该商品的信息"

    soup=BeautifulSoup(html_text,'html.parser')

    #图片匹配规则
    pic_result = soup.find_all("div", class_='p-img')
    reg_pic = re.compile(r'.+source-data-lazy-img="(.+)" width=')

    #标题匹配规则
    title_result=soup.find_all('div',class_='p-name')

    #价格匹配规则
    price_result=soup.find_all('div',class_='p-price')

    item_list=[]


    #图片列表获取
    pic_list=[ reg_pic.match(str(i.a.img)).group(1)for i in pic_result]
    # pic_list = [i.img['source-data-lazy-img'] for i in pic_result]

    #标题列表获取
    title_list=[i.a.em.text  for i in title_result ]

    #价格列表获取
    price_list=[ i.strong.i.text for i in price_result]

    #url列表获取

    url_list=[ i.a['href'] for i in pic_result]

    length=len(pic_result)
    for i in range(length):
        tmp_dict=dict()
        tmp_dict['pic']=pic_list[i]
        tmp_dict['title']=title_list[i]
        tmp_dict['price']=price_list[i]
        tmp_dict['url']=url_list[i]

        item_list.append(tmp_dict)
    return item_list

print()

keyword = input('请输入你要查找的商品：')
result = jd_search(keyword)
if isinstance(result,str):
    print(result)
else:
    for i in result:
        print(i)


