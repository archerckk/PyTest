'''
定义一个类继承于int类型，并实现一个特殊功能：当传入的参数是字符串的时候，返回该字符串中所有字符的ASCII码的和
'''

class Nint(int):
    def __new__(cls,parm):
        cls.parm=parm
        if isinstance(parm,int):
            return cls.parm
        elif isinstance(parm,float):
            return int(cls.parm)
        else:
            sum=0
            for i in parm:
                num=ord(i)
                sum+=num
            cls.parm=sum
            return cls.parm

print(Nint('FishC'))