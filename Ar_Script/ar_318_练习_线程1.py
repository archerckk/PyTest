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


"""
有10个刷卡机，代表建立10个线程，每个刷卡机每次扣除用户一块钱进入总账中，每个刷卡机每天一共被刷100次。账户原有500块。所以当天最后的总账应该为1500

用多线程的方式来解决，提示需要用到这节课的内容
"""

"""
思路：
声明一个变量原来的账户的余额为：500
新建10个线程，代表10个刷卡机
每个刷卡机每次扣除1块钱，累计会刷100次
"""

accountMoney=500
post_list=[]
lock=threading.Lock()

def sum():
    '刷卡机扣钱的方法'
    global accountMoney
    lock.acquire()
    for i in range(100):
        accountMoney+=1
    lock.release()


#新建10个线程，代表10个刷卡机
for i in range(10):
    th=threading.Thread(target=sum)
    post_list.append(th)

lock=threading.Lock()

for post in post_list:
    post.start()

for post in post_list:
    post.join()

print("所有刷卡机的运行完成之后的总额为：",accountMoney)



"""
定义一个生成器函数，函数里只能用yield，要求输出结果：

step 1
step 2 x=haha
step 3 y=haha

提示步骤：建立生成器对象，并且用对象的next()和send()方法来输出结果。send()方法传入的参数是"haha"

"""
def yield_test():
    x=yield 'step 1'

    x = yield 'step 2 x={}'.format(x)

    x = yield 'step 3 y={}'.format(x)


y=yield_test()
print(y.__next__())
print(y.send('haha'))
print(y.send('haha'))

#习题二：用生成器yield实现斐波拉切数列。

def feibonaqie(num):
    result_list=[1,1]
    a=1
    b=1
    c=1


    while num>0:
        c=a+b
        a=b
        b=c
        yield c
        num-=1
    # return result_list


def feibo2(num):
    '参考答案'
    x,y=1,1
    while x<num:
        yield x
        x,y=y,x+y

def feibo_public(num):
    result=[]
    x,y=1,1
    while x<num:
        result.append(x)
        x,y=y,x+y
    return result


# for i in feibonaqie(13):
#     print(i,end=' ')
#
# print()
# for i in feibo2(14):
#     print(i,end=' ')


result=feibo_public(100)
for i in result:
    print(i,end=' ')