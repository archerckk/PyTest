from bs4 import BeautifulSoup as bs
import urllib.request

url='https://baike.baidu.com/item/网络爬虫'
response=urllib.request.urlopen(url)
content=response.read().decode('utf-8')
result=bs(content)
print(result)
