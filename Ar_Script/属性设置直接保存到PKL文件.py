import os
import pickle

'''
1.当属性直接被设置的时候，直接保存为属性名.pkl文件
2.当访问的属性不存在时，报错提示该属性不存在
3.删除属性，会同时删除本地的保存的pkl文件
'''

class Mydes:

    saved=[]

    def __init__(self,name=None):
        self.name=name
        self.filename=self.name+'.pkl'

    def __get__(self, instance, owner):
        if self.name not in Mydes.saved:
            raise AttributeError('%s属性不存在'%self.name)

        with open(self.filename,'rb')as f:
            value=pickle.load(f)
        return value

    def __set__(self, instance, value):
        Mydes.saved.append(self.name)
        with open(self.filename,'wb')as f:
            pickle.dump(value,f)

    def __delete__(self, instance):
        Mydes.saved.remove(self.name)
        os.remove(self.filename)

class Test:
    x=Mydes('x')
    y=Mydes('y')

test=Test()