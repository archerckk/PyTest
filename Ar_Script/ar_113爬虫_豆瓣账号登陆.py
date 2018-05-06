import re
import urllib.request
import http.cookiejar
import urllib.parse

loginUrl='https://www.douban.com/accounts/login'
cookie=http.cookiejar.CookieJar()
opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))

data={
    'form_email':'archerckk@163.com',
    'form_password':'archer3203589',
    'source':'index_nav'
}

data={}
data['form_email']='archerckk@163.com'
data['form_password']='archer3203589'
data['source']='index_nav'

'从首页提交登陆'
response=opener.open(loginUrl,urllib.parse.urlencode(data).encode('utf-8'))
if response.geturl() == "http://www.douban.com/":
    print('登录成功！')