import urllib.request
from bs4 import BeautifulSoup
import re

url='http://www.66ip.cn/areaindex_1/1.html'
req=urllib.request.Request(url)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.65 Safari/537.36')
response=urllib.request.urlopen(req)
html=response.read()
soup=BeautifulSoup(html,'html.parser')
ip_dict={}
ipList=[]
portList=[]
for i in soup.find_all('td',text=re.compile(r'(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])')):
# for i in soup.find_all('td'):
    ipList.append(i.text)

for i in soup.find_all('td',text=re.compile(r'^[1-9]\d*$')):
    portList.append(i.text)

for i in range(len(ipList)):
    ip_dict[ipList[i]]=portList[i]

for i in ip_dict:
    print(i,':',ip_dict[i])


