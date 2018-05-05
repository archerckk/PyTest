import re
import urllib.request
import http.cookiejar
import urllib.parse

loginUrl='https://www.douban.com/accounts/login'
cookie=http.cookiejar.CookieJar()
opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))

params={
'form_email':'archerckk@163.com',
'form_password':'archer3203589',
'source':'index_nav'
}

'从首页提交登陆'
response=opener.open(loginUrl,urllib.parse.urlencode(params).encode('utf-8'))