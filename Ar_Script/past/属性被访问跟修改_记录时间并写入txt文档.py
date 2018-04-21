import time

"""
1.需要用time模块记录访问的时间
2.获取跟修改都要要调用这个方法
3.用列表的形式存放起来，写入一个指定的文件，并且关闭
"""

class Mydes:
    def __init__(self,value=None,name=None):
        self.val=value
        self.name=name
        self.filename='record_new.txt'

    def __get__(self, instance, owner):

        with open(self.filename,'a',encoding='utf-8')as f:
            f.write('%s变量于北京时间%s 被读取%s=%s\n'%(self.name,time.ctime(),
                                              self.name,str(self.val)))

        return self.val
    def __set__(self, instance, value):
        self.val=value
        with open(self.filename,'a',encoding='utf-8')as f:
            f.write('%s变量于北京时间%s 被读取%s=%s\n'%(self.name,time.ctime(),
                                              self.name,str(self.val)))

class Test:
    x=Mydes(10,'X')
    y=Mydes(12,'Y')

test=Test()