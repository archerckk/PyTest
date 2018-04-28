class PlugIn(object):
    def __init__(self):
        self._exported_methods = []

    def plugin(self, owner):
        for f in self._exported_methods:
            owner.__dict__[f.__name__] = f
        '遍历自身方法列表,将自身方法列表的方法名字添加到对象的方法字典里面'
    def plugout(self, owner):
        for f in self._exported_methods:
            del owner.__dict__[f.__name__]
        '遍历自身的方法列表,删除添加对象已经添加的插件方法'

class AFeature(PlugIn):
    def __init__(self):
        super(AFeature, self).__init__()
        self._exported_methods.append(self.get_a_value)

    def get_a_value(self):
        print('a feature.')


class BFeature(PlugIn):
    def __init__(self):
        super(BFeature, self).__init__()
        self._exported_methods.extend([self.get_b_value,self.get_c_value])

    def get_b_value(self):
        print('b feature.')

    def get_c_value(self):
        print('c feature.')



class Combine: pass


c = Combine()
AFeature().plugin(c)
BFeature().plugin(c)

c.get_a_value()
c.get_b_value()
c.get_c_value()
