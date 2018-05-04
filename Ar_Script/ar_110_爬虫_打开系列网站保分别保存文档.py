import urllib.request as r
'''
1.先打开文档里面的内，将里面的网站拿出来
2.分别打开网站里面的内容，将内容分别保存到txt文档里面
'''
f=open('resources/url.txt')
count=0
for i in f:
    response=r.urlopen(i)
    html=response.read()
    html=html.decode('utf-8')
    count+=1
    '解决新建文件默认为GBK，写入文件失败的问题'
    with open('result/url%d.txt'%count,'w',encoding='utf-8')as f:
        f.write(html)

