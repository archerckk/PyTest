print()
'''
lambda表达式的作用
	Python写一些执行脚本时，使用lambda就可以省下定义函数过程，
	比如说我们只是需要写个简单的脚本来管理服务器时间，我们就不需要专门
	定义一个函数然后再写调用，使用lambda就可以使得代码更加精简。
	
	对于一些比较抽象并且整个程序执行下来只需要调用一两次的函数，有时候给函数起个名字
	也是比较头疼的问题，使用lambda就不需要考虑命名的问题了。
	
	简化代码的可读性，由于普通的屌丝函数阅读经常要跳到开头def定义部分，
	使用lambda函数可以省去这样的步骤。
'''

a = lambda x: x ** 2 + 1
print(a(5))


# lambda函数的高阶用法，你猜会打印什么？

def make_repeat(n):
    return lambda s: s * n


double = make_repeat(2)
print(double(8))
print(double('FishC'))

'''
1.filer()用法
第一个参数为None对象或者函数
第一个参数为可迭代的对象
直接返回为True的值，生成一个可迭代的对象，可以用list()变成一个列表
'''
# 将0-9当中x%2不为0的数筛选出来
tmp = list(filter(lambda x: x % 2, range(10)))
print(tmp)

# 利用filter()和lambda表达式快速求出100以内所有3的倍数
result = list(filter(lambda x: not x % 3, range(100)))
print(result)

# 复习一下列表推导
result2 = [x for x in range(100) if not x % 3]
print(result2)

'''
2.map()用法
第一个参数为None对象或者函数
第一个参数为可迭代的对象
将序列里面所有的元素都加工一遍，返回一个新序列
'''
tmp2 = list(map(lambda x: x ** 3, range(10)))
print(tmp2)

# map高阶用法
b = list(map(lambda x, y, z: [x, y, z], [1, 3, 5, 7, 9], [2, 4, 6, 8, 10], ["a", "b", "c", "d", "e"]))
print(b)
