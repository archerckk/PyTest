import datetime
import os
"""
 一 编写with操作类Fileinfo()，定义__enter__和__exit__方法。完成功能：

 1.1 在__enter__方法里打开Fileinfo(filename)，并且返回filename对应的内容。如果文件不存在等情况，需要捕获异常。

 1.2 在__enter__方法里记录文件打开的当前日期和文件名。并且把记录的信息保持为log.txt。内容格式："2014-4-5 xxx.txt"
"""""
class Fileinfo(object):

    def __init__(self,fileName):
        self.fileName=fileName
        self.f=open(self.fileName)

    def __enter__(self):
        now=datetime.date.today().isoformat()
        with open("fileLog.txt",'w')as f:
            f.write(str(now)+' '+self.fileName)
        try:
            self.f=open(self.fileName)
            return self.f.read()

        except IOError:
            return "文件参数传入错误，打开失败"

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()

#
# with Fileinfo("123")as f:
#     print('正在执行')



"""
 二：用异常方法，处理下面需求：

 info = ['http://xxx.com','http:///xxx.com','http://xxxx.cm'....]任意多的网址

 2.1 定义一个方法get_page(listindex) listindex为下标的索引，类型为整数。 函数调用：任意输入一个整数，返回列表下标对应URL的内容，用try except 分别捕获列表下标越界和url 404 not found 的情况。

 2.2 用logging模块把404的url，记录到当前目录下的urlog.txt。urlog.txt的格式为：2013-04-05 15:50:03,625 ERROR http://wwwx.com 404 not foud、
"""


"""
 三：定义一个方法get_urlcontent(url)。返回url对应内容。

 要求：
 
 1自己定义一个异常类，捕获URL格式不正确的情况，并且用logging模块记录错误信息。

 2 用内置的异常对象捕获url 404 not found的情况。并且print 'url is not found'
"""