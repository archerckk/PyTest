#encoding='utf-8'

import threading
import requests
import bs4




#习题一：已知列表 info = [1,2,3,4,55,233]

#生成6个线程对象,每次线程输出一个值，最后输出："the end"。
thread_list=[]
for i in range(6):
    th=threading.Thread(target=print(i))
    th.start()
    thread_list.append(th)

for thread in thread_list:
    thread.join()

print('the end')


#习题二：已知列表 urlinfo = ['http://www.baidu.com','http://www.163.com','http://www.163.com'] 用多线程的方式分别打开列表里的URL，并且输出对应的网页标题和内容。

def url_open(url):
    body=requests.get(url)
    content=body.text
    soup=bs4.BeautifulSoup(content,'html.parser')
    title=soup.title.text
    # print(content)
    print('网站标题为：',title)


urlinfo = ['http://www.qq.com', 'http://www.163.com', 'http://www.sohu.com']
num=len(urlinfo)
th_list2=[]
for i in range(num):
    th=threading.Thread(target=url_open,args=[urlinfo[i]])
    th.start()
    th_list2.append(th)

for i in th_list2:
    i.join()

print('the func2 run end')



#习题三：已知列表 urlinfo = ['http://www.sohu.com','http://www.163.com','http://www.sina.com'] 用多线程的方式分别打开列表里的URL，输出网页的http状态码。
def get_http_code(url):
    body = requests.get(url)
    print("{}网页访问的状态码为：{}".format(url,body.status_code))

urlinfo2 = ['http://www.sohu.com','http://www.163.com','http://www.sina.com']
num=len(urlinfo2)

th_list3=[]
for i in range(num):
    th=threading.Thread(target=get_http_code,args=[urlinfo2[i]])
    th.start()
    th_list3.append(th)

for i in th_list3:
    i.join()

print('get url code run end')
