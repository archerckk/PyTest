import pickle as p
import os

class Mydes:
    '属性的名字注销不是很懂是什么意思'
    save=[]

    def __init__(self,name):
        self.name=name
        self.filepath='result/%s.pkl'%self.name

    def __get__(self, instance, owner):
        with open(self.filepath,'rb')as f:
            return p.load(f)

    def __set__(self, instance, value):
        with open(self.filepath,'wb')as f:
            self.name=value
            p.dump(self.name,f)
        Mydes.save.append(self.name)

    def __delete__(self, instance):
        '没整过文件删除都不知道有os.remove啊23333'
        os.remove(self.filepath)
        Mydes.save.remove(self.name)
        # del self.name

class Test:
    x=Mydes('x')
    y=Mydes('Y')

test=Test()
test.x=15
print(test.x)
del test.x