from bs4 import BeautifulSoup as bs
import urllib.request
import re

def main():
    # keyword=input('请输入你要查找的内容：')
    keyword='西游记'
    head={}
    head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
    url='https://baike.baidu.com/item/'.encode('utf-8')
    print(url)
    # req=urllib.request.Request(url,headers=head)
    # print(req.get_full_url())
    # response=urllib.request.urlopen(req)
    # print(response.geturl())
    # content=response.read()
    # print(content)
    # soup=bs(content,'html.parser')
    #
    # for each in soup.find_all(href=re.compile('view')):
    #     print(each.text,'-->',''.join(['http://baike.baidu.com',each['href']]))

if __name__ == '__main__':
    main()
