class A:

    def __init__(self):
        self.x=10

a=A()

print(hasattr(a,'x'))
print(getattr(a,'x'))
setattr(a,'x',20)
print(a.x)
del a.x
print(hasattr(a,'x'))


class B:

    def __init__(self):
        self.__x=10

    def get(self):
        return self.__x

    def setattr(self,value):
        self.__x=value
        '不用设置返回值'

    def delete(self):
        del self.__x
    x=property(get,setattr,delete)

b=B()
print(b.x)
b.x=20
print(b.x)
b.delete()
print(hasattr(b,'x'))


'修饰符写法'
class C:
    def __init__(self, size=10):
        self.size = size

    @property
    def x(self):
        return self.size

    @x.setter
    def x(self, value):
        self.size = value

    @x.deleter
    def x(self):
        del self.size

c=C()
c.x=50
print(c.x)