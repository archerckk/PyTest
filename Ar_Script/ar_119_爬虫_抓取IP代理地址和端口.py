import urllib.request
from bs4 import BeautifulSoup
import re
import os

url = 'http://www.66ip.cn/areaindex_1/1.html'
req = urllib.request.Request(url)
req.add_header('User-Agent',
               'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.65 Safari/537.36')
response = urllib.request.urlopen(req)
html = response.read()
soup = BeautifulSoup(html, 'html.parser')
ip_dict = {}
ipList = []
portList = []

'(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])ip正则表达式1'
'将所有的ip地址都找到并且存进列表'
for i in soup.find_all('td',
                       text=re.compile(r'(?:(?:[01]?\d?\d|2[0-4]\d|25[0-5])\.){3}(?:[01]?\d?\d|2[0-4]\d|25[0-5])')):
    ipList.append(i.text)

'将所有的端口都找到并且存进列表'
for i in soup.find_all('td', text=re.compile(r'^[1-9]\d*$')):
    portList.append(i.text)

'将IP地址和端口组合成字典'
for i in range(len(ipList)):
    ip_dict[ipList[i]] = portList[i]

'遍历字典然后将字典内容编辑成可用代理然后写入一个TXT文档'
with open('result/ip_proxy.txt', 'w', encoding='utf-8')as f:
    for i in ip_dict:
        i = i + ':' + ip_dict[i] + '\n'
        f.writelines(i)

'删除txt文档的最后一个换行符'
with open('result/ip_proxy.txt', 'rb+')as f:
    f.seek(-2, os.SEEK_END)
    f.truncate()
