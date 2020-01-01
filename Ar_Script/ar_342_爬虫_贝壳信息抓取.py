import requests
from bs4 import BeautifulSoup

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
    location_list=[i.i.text()]
    # for i in location:


    print(location)

    # print(ul_content)
    # ul_content._find_all('a',class_='name')


if __name__ == '__main__':
    response=url_open(url)
    get_data(response)