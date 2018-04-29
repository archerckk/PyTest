'''
我们都知道在Python中，两个字符串相加会自动拼接字符串，
但遗憾的是两个字符串相减却抛出异常。因此，现在我们要求定义一个Nstr类，
支持字符串的相减操作，A-B，从A中去去除B的子字符串
'''

class Nstr(str):

    def __sub__(self, other):
        if other in self:
            'strip只能针对两边的对象进行去除'
            return self.strip(other)

            # return self.replace(other,'')
        else:
            return None

a=Nstr('abc')
b=Nstr('b')
print(a-b)