import urllib.request
import random as r

url='http://www.whatismyip.com.tw/'

# proxyList=['113.79.75.105:9999','128.199.103.199:8080','37.1.215.57:1490']

'设置代理'
# proxy=urllib.request.ProxyHandler({'http':r.choice(proxyList)})

'添加一个有代理的打开方式'
opener=urllib.request.build_opener()
'给打开方式增加头部信息'
opener.add_handler=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0')]

response=opener.open(url)
result=response.read().decode('utf-8')
print(result)