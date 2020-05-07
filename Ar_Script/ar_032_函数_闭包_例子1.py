'''
这是一个闭包的例子：
当test=funX()的时候，只要test变量没有被重新赋值，outside()就没有被释放，也就是说局部变量x就没有被重新初始化。
所以当全局变量不适用的时候，可以考虑使用闭包更稳定和安全
2018年4月15日20:36:23
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


"""
闭包计算器例子
"""
print('='*40)
def calculatror(option):

    if option==1:
        def add(x,y):
            return x+y
        return add
    elif option==2:
        def mulus(x,y):
            return x-y
        return mulus
    elif option==3:
        def multiply(x,y):
            return x*y
        return multiply
    elif option==4:
        def divisopn(x,y):
            return x+y
        return divisopn
    else:
        print('参数有误')
        return None

add=calculatror(1)
print(add(3, 4))
print(add(99,1))
multiply=calculatror(3)
print(multiply(3,4))

"""
闭包练习
实现y=x+1，y=2x+2
"""

def fun1():
    def cal(x):
        return x+1
    return cal

def fun2():
    def cal(x):
        return 2*x+2
    return cal

cal1=fun1()
print(cal1(5))

cal2=fun2()
print(cal2(5))