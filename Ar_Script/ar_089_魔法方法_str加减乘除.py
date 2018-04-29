'''
2 定义一个类Nstr，当该类的实例对象间发生加、减、乘、除运算时，
将改对象的所有字符串的ASCII码之和进行计算
'''
class Nstr(str):

    def __add__(self, other):
        result=getResult(self,other)

        return result[0]+result[1]

    def __sub__(self, other):
        result=getResult(self,other)

        return result[0] - result[1]

    def __mul__(self, other):
        result = getResult(self, other)

        return result[0] * result[1]

    def __truediv__(self, other):
        result = getResult(self, other)

        return result[0] / result[1]

def getResult(a,b):
    result1 = 0
    result2 = 0
    for i in a:
        a = ord(i)
        result1 += a

    for i in b:
        a = ord(i)
        result2 += a
    return [result1,result2]
# a=Nstr('A')
# b=Nstr('A')
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)

'参考答案：'
class Ustr(int):

    def __new__(cls, arg):
        if isinstance(arg,str):
            total=0
            for i in arg:
                total+=ord(i)
            arg=total
        return arg
a=Ustr('A')
b=Ustr('A')
