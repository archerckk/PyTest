from tornado import httpclient
from tornado.httpclient import HTTPRequest
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'cookie':'BAIDUID=A6BFF1A7E05BED2918B8D33A9B008269:FG=1; BIDUPSID=A6BFF1A7E05BED2918B8D33A9B008269; PSTM=1576498220; BD_UPN=12314753; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; H_PS_PSSID=; BDRCVFR[p00bQTK6bcD]=mk3SLVN4HKm; delPer=0; BD_CK_SAM=1; PSINO=6; H_PS_645EC=5a6epgbXrKIMB9TkdK6O7bvCDPQ1AamRPUQdW4BWLL4zNI56%2Bj43FwQhsX37fD7LXFeMEBoT; COOKIE_SESSION=11020_0_6_2_11_3_0_0_4_3_19_3_65964_0_0_0_1576641112_0_1576652128%7C6%230_0_1576652128%7C1'
}

client=httpclient.HTTPClient()

key_word='python'

# response=requests.get('https://www.baidu.com/s?wd={}&tn=99323164_hao_pg'.format(key_word),headers=headers)
# print(response.text)

request=HTTPRequest(url='https://www.baidu.com/s?wd={}&tn=99323164_hao_pg'.format(key_word),headers=headers)
# key_word=input('请输入你要搜索的关键字：')

response=client.fetch(request)

print(response.body)