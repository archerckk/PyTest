import urllib.request as r
response=r.urlopen('http://www.fishc.com')
html=response.read()
html=html.decode('utf-8')
print(html)
print(type(html))



