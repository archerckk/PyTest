import urllib.request as r
response=r.urlopen('http://www.fishc.com')
html=response.read(300)
print(html)
# html=html.decode('utf-8')
# # print(html)
# for i in html[:300]:
#     print(i,end='')



