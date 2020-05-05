from collections import Iterable
from datetime import datetime

#编写一个自定义的迭代器跟迭代对象
class MyItetator(object):

    def __init__(self,index,end):
        self.index=index
        self.end=end
        self.tmp=index

    def __iter__(self):
        return self

    def __next__(self):
        if self.index<self.end:
            self.tmp=self.index
            self.index+=1
        else:
            raise StopIteration()

        return self.tmp

class My_range(object):

    def __init__(self,start,end):
        self.start=start
        self.end=end

    def __iter__(self):
        return MyItetator(self.start,self.end)


iter_actor=My_range(1,10)
print(isinstance(iter_actor,Iterable))

# for i in iter_actor:
#     print(i)
#
# print('='*30)
#
# for i in iter_actor:
#     print(i)


#练习题
"""
用while语句实现以下for 语句相同的功能
for each in range(5):
    print(each)
"""
iterator=iter([0,1,2,3,4])
while True:
    try:
        print(next(iterator))
    except StopIteration:
        break

"""
写一个迭代器，要求输出至今为止的所有闰年
"""
class LeapYear(object):

    def __init__(self):
       self.now=datetime.today().year

    def is_leap_year(self,i):
        if ((i%4==0 and i%100!=0)or(i%400==0)):
           return True
        else:
            return False

    def __iter__(self):
        return self

    def __next__(self):
        while not self.is_leap_year(self.now):
            self.now-=1

        tmp=self.now
        self.now-=1

        if self.now<=0:
            raise StopIteration()

        return tmp

leap_year=LeapYear()
# print(type(leap_year))
for i in leap_year:
    print(i)

"""
写一个MyRev类，功能与reversed()相同（内置函数reversed是返回一个迭代器，是序列seq的逆序宣誓）
"""

class MyRev(object):

    def __init__(self,seq):
        self.seq=seq
        self.tmp=-1

    def __iter__(self):
        return self

    def __next__(self):
        length=len(self.seq)
        result=self.seq[self.tmp]
        self.tmp-=1

        if self.tmp<(-length-1):
            raise StopIteration
        return result

test=MyRev('123456')

# print(len(test))
for i in test:
    print(i,end='')


# '参考答案：'
# alist = range(5)
# it = iter(alist)
#
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         break