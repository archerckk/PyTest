'''
    编写一个函数，利用欧几里得算法，求最大公约数
    例如gcd(x,y)返回值为参数x和参数y的最大公约数
'''
def gcd(x,y):
    while y:
        t = x % y
        x = y
        y = t

        '''错误演示'''
        return x

print(gcd(1997,615))


# def gcd(x, y):
#     while y:
#         t = x % y
#         x = y
#         y = t
#
#     return x
# print(gcd(4, 7))