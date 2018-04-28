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
