import urllib.request
from urllib.error import URLError

try:
    url='http://www.baiduxxxxxxx.com'
    response=urllib.request.urlopen(url)
except URLError as e:
    if hasattr(e,'reason'):
        print('Error:',e.reason)
    if hasattr(e,'code'):
        print('code:',e.code)
