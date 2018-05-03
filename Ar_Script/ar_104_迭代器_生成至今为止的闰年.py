'要拿到迄今为止的所有年份，将年份都进行判断，存放在迭代器里面，然后再用循环迭代打印出来'

import datetime as dt


class LeapYear:
    def __init__(self):
        self.now = dt.date.today().year

    def isLeapYear(self, year):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True
        else:
            return False

    def __iter__(self):
        return self

    def __next__(self):
        while not self.isLeapYear(self.now):
            self.now -= 1

        temp = self.now
        self.now -= 1

        return temp

ly=LeapYear()
for i in ly:
    if i>2000:
        print(i)
    else:
        break
#
# class RunY:
#
#     def __init__(self,year):
#         self.year=year
#         self.count=0
#         self.result=0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.count+=1
#         if (self.count %4==0 and self.count%100!=0)or (self.count%400==0):
#                 self.result=self.count
#
#         return self.result
#
#
# runy=RunY(2018)
# for i in runy:
#     if i>2000:
#         print(i)
#     else:
#         break


class Test:

    def __init__(self,limit):
        self.count=2018
        self.limit=limit

    def __iter__(self):
        return self

    def __next__(self):

        while self.count%2:
            self.count -= 1

        tmp=self.count
        self.count-=1

        if self.count<self.limit:
            raise StopIteration
        return tmp


test=Test(1500)
for i in test:
    print(i)
