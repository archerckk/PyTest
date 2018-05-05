import urllib.request as r
import urllib.parse as p
import json
url='http://fanyi.baidu.com/v2transapi'
data={}
data['from']=	'en'
data['query']	='I+love+FishC'
data['sign']	='273972.52485'
data['simple_means_flag']=	'3'
data['sign']=	'2483e5f6202f67c6fd60ef14c3161e5a'
data['to']	='zh'
data['token']=	'6723970838a41189bd07d32739707032'
data['transtype']	='translang'

data=p.urlencode(data).encode('utf-8')


response=r.urlopen(url,data)
# print(r.urlopen(url,data).getcode())
# '获取请求的状态码'
html=response.read().decode('utf-8')
target=json.loads(html)
print(html)