"""
今天习题：

习题一：

1 用while语句的2种方法输出数字：1到10


2 用for语句和continue 输出结果：1 3 5 7 9


习题二：假设有列表

a = [1,2,3,4,5,6]

1 用for if else 的方法查找数字8是否在列表a里，如果在的话，输出字符串'find'，如果不存在的话，

输出字符串'not find'

2 用while语句操作上面的列表a，输出下面结果：

[2,3,4,5,6,7]

"""

# 练习1  用while语句的2种方法输出数字：1到10
print('练习1方法1结果展示：')
x = 1
while True:
    print(x)
    x += 1
    if x > 10:
        break
print('练习1方法2结果展示：')
x = 1
while x < 11:
    print(x)
    x += 1

# 练习2  用for语句和continue 输出结果：1 3 5 7 9
print('练习2结果展示：')
x = 1
for i in range(1, 10, 2):
    print(i)

print('练习2方法2结果展示：')
for i in range(1, 10):
    if i % 2 == 1:
        print(i)

# 练习3  用for if else 的方法查找数字8是否在列表a里，如果在的话，输出字符串'find'，如果不存在的话，输出字符串'not find'

print('练习3结果展示：')
a = [1, 2, 3, 4, 5, 6]
for i in a:
    if 8 in a:
        print('find')
        break
else:
    print('not find')

# 练习4  2 用while语句操作上面的列表a，输出下面结果：[2,3,4,5,6,7]
print('练习4结果展示：')
a = [1, 2, 3, 4, 5, 6]
while True:
    del a[0]
    a.append(7)
    break
print(a)
