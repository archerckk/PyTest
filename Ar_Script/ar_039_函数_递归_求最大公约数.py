print()
'''
1 使用递归编写一个函数，利用欧几里得算法求最大公约数，
例如gcd(x,y)返回为参数x和参数y的最大公约数
'''

def gcd(x,y):
    if y:
        return (gcd(y,x%y))
    #变量之间的顺序变换可以用，参数位置移动来表示值的替换
    else:
        return x

print(gcd(4,8))