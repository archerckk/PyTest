#先是普通版本求斐波那契数列
def fei(n):
    n1 = 1
    n2 = 1
    n3 = 1
    #真正地理解了一下这个n3为什么是等于1了
    #它其实在下面的循环走不进去的时候是有作用的
    if n < 1:
        print('你要计算的位置过小')
    while (n - 2) > 0:
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        n -= 1
    return n3

print(fei(2))

#递归版本
def feiD(n):
    if n<1:
        print('输入有误')
        return -1
    #这是要考虑输入不对的情况的，自己有这个想法但是就是没有去写
    if n==1 or n==2:
        return 1
    else:
        return feiD(n-1)+feiD(n-2)

print(feiD(11))