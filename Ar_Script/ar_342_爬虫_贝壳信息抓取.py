import requests
from bs4 import BeautifulSoup
import time
import sqlite3
import re
"""
1、抓取网页内容
2、分析网页内容，保存自己需要的数据
3、建立数据表
4、将数据入库
"""




def url_open(url):
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
    }
    response=requests.get(url,headers=headers)
    return response

def get_data(response):
    # print(response.text)
    soup=BeautifulSoup(response.text,'html.parser')

    '脚本执行时间获取'
    current_time=time.strftime('%Y-%m-%d %X',time.localtime())
    print(current_time)

    '楼盘名字&房屋类型获取'
    div=soup.find_all(name='div',class_='resblock-name')
    area_type = soup.find_all('span', attrs={'style':re.compile(r'background:(FB9252)|(59A5EB)|(B199FF)|(FB9252);')})
    area_name_list=[i.a['title'] for i in div]
    area_type_list=[i.text for i in area_type]

    #测试代码
    # for i in area_name_list:
    #     print(i)
    #
    # for i in area_type_list:
    #     print(i)

    length = len(area_name_list)
    area_name_list=['{}({})'.format(area_name_list[i],area_type_list[i]) for i in range(length)]

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

    # '总价信息获取'
    # total_price=soup.find_all(name='div',class_='second')
    # total_price_list=[i.text for i in total_price]
    # for i in total_price_list:
    #     print(i)

    '初始化数据库&建立游标'
    connect=sqlite3.connect('beike.db')
    c=connect.cursor()


    for i in range(length):
        sql="INSERT INTO price(area_name,price,location,create_time)values('{}','{}','{}','{}')".format(
            area_name_list[i],
            average_price_list[i],
            location_list[i],
            current_time)
        # print(sql)
        c.execute(sql)
    print('插入数据成功')
    connect.commit()
    print('提交数据成功\n')
    connect.close()


if __name__ == '__main__':
    for i in range (1,4):
        url = 'https://qy.fang.ke.com/loupan/chengxishangmaoqu-xincheng-henghe/pg{}/#qingchengqu'.format(i)
        response=url_open(url)

        # #本地测试代码
        # with open('bs4.html','wb')as f:
        #     for chunk in response.iter_content(chunk_size=128):
        #         f.write(chunk)

        get_data(response)
        time.sleep(20)