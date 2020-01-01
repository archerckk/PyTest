import requests
from bs4 import BeautifulSoup
import datetime
import re

"""
1、抓取网页内容
2、分析网页内容，保存自己需要的数据
3、建立数据表
4、将数据入库
"""

url='https://qy.fang.ke.com/loupan/chengxishangmaoqu-xincheng-henghe/rs/#qingchengqu'


def url_open(url):
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
    }
    response=requests.get(url,headers=headers)
    return response

def get_data(response):
    # print(response.text)
    soup=BeautifulSoup(response.text,'html.parser')
    ul_content = soup.find('ul', class_='resblock-list-wrapper')

    '楼盘名字获取'
    div=soup.find_all(name='div',class_='resblock-name')
    area_name_list=[i.a['title'] for i in div]
    for i in area_name_list:
        print(i)

    '位置信息获取'
    location=soup.find_all(name='a',class_='resblock-location')
    location_list=[i.text.strip('\n') for i in location]
    print(len(location_list))
    for i in location_list:
        print(i)

    '均价信息获取'
    average_price=soup.find_all(name='span',class_='number')
    average_price_list=[i.text for i in average_price]
    for i in average_price_list:
        print(i)
    # print(ul_content)
    # ul_content._find_all('a',class_='name')
    '总价信息获取'
    total_price=soup.find_all(name='div',class_='second')
    total_price_list=[i.text for i in total_price]
    for i in total_price_list:
        print(i)

    '总页数获取'
    reg=re.compile(r'<a href="javascript:;" data-page="\d">(\d)</a>')
    tmp=reg.findall(response.text)
    print(response.text)

    # total_page=soup.find(name='div',class_='page-container clearfix')
    # total_page=soup.find_all(name='a',)
    # print(total_page)
    # print(total_page)
    # num=total_page.count('a href=')
    # print(num)
if __name__ == '__main__':
    response=url_open(url)
    get_data(response)