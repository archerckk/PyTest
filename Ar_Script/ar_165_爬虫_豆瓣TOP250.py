import requests
from bs4 import BeautifulSoup as bs

def url_open(url):
    header= {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'}

    res=requests.get(url,header)

    return res


def main():
    host='https://movie.douban.com/top250'
    res=url_open(host)
    soup=bs(res.text,'html.parser')
    print(soup)
    # print(soup.prettify())



main()