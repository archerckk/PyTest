import urllib.request
import re
import random
import requests
from bs4 import BeautifulSoup

def get_Proxy(filename):
    Proxy_list=[]
    with open(filename)as f:
        for i in f:
            Proxy_list.append(i)
    return Proxy_list


def get_url(url):
    req=urllib.request.Request(url)
    # req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.65 Safari/537.36')
    # proxys=get_Proxy('result/ip_proxy.txt')
    # proxy=random.choice(proxys)
    #
    # proxy_support =urllib.request.ProxyHandler({'http':proxy})
    # opener=urllib.request.build_opener(proxy_support)
    # response=opener.open(req)
    # html=response.read().decode('utf-8')

    res=requests.get('http://jandan.net/ooxx/page-62#comments')
    html=BeautifulSoup(res.text)
    # print(html)



    return html

def get_img(url):
    html=get_url(url)
    print(html)
    # img_list=re.findall(re.compile(r'<img src="http://([^"]+\.jpg)"'), html)

    # for i in img_list:
    #     '取到最后一个反斜杠作为分隔符，保存文件名'
    #     print(i)
        # filename=i.split('/')[-1]
        # urllib.request.urlretrieve(i,'result/%s'%filename,None)

    # for i in img_list:
    #     print(i)


if __name__ == '__main__':
    url = 'http://jandan.net/ooxx/page-62#comments'
    get_img(url)