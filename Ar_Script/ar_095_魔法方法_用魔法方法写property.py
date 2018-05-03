class MyProperty:
    def __init__(self, fget=None, fset=None, fdel=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __get__(self, instance, owner):
        return self.fget(instance)

    # get是访问值，所以要返回值

    def __set__(self, instance, value):
        self.fset(instance, value)

    # set的话是要处理值，并不是要返回值

    def __delete__(self, instance):
        self.fdel(instance)
        # del同set


class C:
    def __init__(self):
        self._x = None

    def getX(self):
        return self._x

    def setX(self, value):
        self._x = value

    def delX(self):
        del self._x

    x = MyProperty(getX, setX, delX)


c=C()
c.x=90
print(c.x)