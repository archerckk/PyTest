class Mydes:
    def __init__(self,value=None,name=None):
        self.val=value
        self.name=name

    def __get__(self, instance, owner):
        print('正在获取变量：',self.name)
        return self.val

    def __set__(self, instance, value):
         print('正在修改变量：',self.name)
         self.val=value

    def __delete__(self, instance):
        return '正在删除变量：x\n噢，该变量无法删除！'

class Test:
    x=Mydes(10,'x')

test=Test()

y=test.x
# test.x=8
print(test.x)