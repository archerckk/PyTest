'按要求编写描述符Mydes：当类的属性被访问、修改或设置时，分别做出提醒'

class Mydes:
    def __init__(self,value,name):
        self.value=value
        self.name=name


    def __get__(self, instance, owner):
        print('正在获取属性:%s'%self.name)
        return self.value

    def __set__(self, instance, value):
        print('正在修改属性：%s'%self.name)
        self.value=value

    def __delete__(self, instance):
        print('正在删除属性：%s\n该变量无法删除'%self.name)

class Test:
    x=Mydes(10,'x')