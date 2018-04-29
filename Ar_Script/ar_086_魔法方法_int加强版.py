'''
 定义一个类继承预int类型，并实现一个特殊的功能：当传入的参数是字符串的时候，
 返回该字符串所有字符的的ASSII码的和（使用ord（）获得一个字符的ASCII码的值）
'''

'''
1.对传入参数进行判断，是字符串的话，用ord函数拿到对应的ASSII码再加总
'''
class Nint(int):

    def __new__(cls, args):
        sum=0
        if isinstance(args,str):
            for i in args:
                code=ord(i)
                sum+=code
            args=sum
        return int.__new__(cls,args)

print(Nint(123))


