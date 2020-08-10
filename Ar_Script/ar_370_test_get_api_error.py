import requests

with open('api_cookie')as f:
 data=f.read()

headers={

 "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
 "Accept-Encoding": "gzip, deflate",
 "Accept-Language": "zh-CN,zh;q=0.9",
 "Cache-Control": "no-cache",
 "Cookie":"{}".format(data),
 "Host": "www.nene-app.info",
 "Pragma": "no-cache",
 "Proxy-Connection": "keep-alive",
 "Upgrade-Insecure-Requests": "1",
 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
}


res=requests.get('http://www.nene-app.info/admin/user_active_logs_statistics',headers=headers)
print(res.content)