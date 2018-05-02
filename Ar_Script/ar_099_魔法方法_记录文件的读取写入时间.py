#encording=gbk
import time as t

'''
用描述符实现属性的访问和修改
对应的日志写入到一个txt那里
'''

class Record:

    def __init__(self,value,name):
        self.value=value
        self.name=name


    def __get__(self, instance, owner):

        with open('result/record.txt','a')as f:
            f.writelines('%s变量 %s 被读取，%s=%s\n'%(self.name,t.asctime(),self.name,self.value))
        return self.value

    def __set__(self, instance, value):
        self.value = value
        with open('result/record.txt','a')as f:
            f.writelines('%s变量 %s 被修改，%s=%s\n'%(self.name,t.asctime(),self.name,self.value))



class Test:
    x=Record(10,'x')
    y=Record(8,'y')

test=Test()
print(test.y)
test.y=10
print(test.y)