#尝试
def power(x,y):
    if y==0:
        return 1
    else:
        return x*power(x,y-1)

print(power(2,3))

#参考答案
# def power(x, y):
#     if y:
#         return x * power(x, y - 1)
#     else:
#         return 1
#
#
# print(power(2, -2))

'''
其实参考答案也不是完美的，它也是不支持负数的乘方计算的
递归在这类简单的问题上面确实有它的局限啊
'''

