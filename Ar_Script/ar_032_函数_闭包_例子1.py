'''
这是一个闭包的例子：
当test=funX()的时候，只要test变量没有被重新赋值，outside()就没有被释放，也就是说局部变量x就没有被重新初始化。
所以当全局变量不适用的时候，可以考虑使用闭包更稳定和安全
'''

def outside():
    x=5
    def inside():
        nonlocal x
        x+=1
        return x
    return inside

test=outside()
print(test())
print(test())
print(test())
