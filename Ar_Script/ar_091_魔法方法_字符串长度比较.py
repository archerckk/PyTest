'''
1 定义一个单词（word）类继承自字符串，重写比较操作符的，当两个word类对象进行比较时，
根据单词的长度来进行比较大小。
加分要求：实例化如果传入的是带空格的字符串，则取第一个空格前的单词作为参数
'''
class Word(int):

    def __new__(cls, args):
        if isinstance(args,str):
            if ' 'in args:
                length=args.find(' ')
            else:
                length = len(args)
            args=length
            return int.__new__(cls,args)

a=Word('a')
b=Word('a 123')
print(a<=b)
