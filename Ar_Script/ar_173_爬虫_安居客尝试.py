import requests


headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'}
url='https://qingyuan.anjuke.com/sale/?kw=时代倾城&from=xlts_rm'
res=requests.get(url=url,headers=headers)
with open('result/安居客.txt','w',encoding='utf-8')as f:
    f.write(res.text)