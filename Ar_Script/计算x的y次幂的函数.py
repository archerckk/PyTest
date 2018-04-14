def power(x,y):
    '''这是一个计算x的y次幂的函数'''
    result=x**y

    return result

x=int(input('请输入你要求的底数：'))
y=int(input('你输入你要求的次方:'))
print('%d的%d次方为%d'%(x,y,power(x,y)))


# def power(x, y):
#     result = 1
#
#     for i in range(y):
#         result *= x
#
#     return result
#
# print(power(-2, -2))