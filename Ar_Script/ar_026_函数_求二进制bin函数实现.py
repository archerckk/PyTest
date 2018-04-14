'''
编写一个将10进制转换为二进制的函数，要求采用除2取余的方式，结果与调用bin()一样返回字符串形式
'''
"""
1.定义一个字符串来接收数据
2.
"""

def ar_bin(num):
    result=''
    tmp=[]
    while num:
        t=num%2
        tmp.insert(0, t)
        num=num//2


    for i in tmp:
        result+=str(i)

    return 'Ob'+result

print(ar_bin(128))



