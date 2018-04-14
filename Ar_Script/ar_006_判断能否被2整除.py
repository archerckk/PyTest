#方法1 利用两个相除的结果是否相等
a=4
if a/2 == a//2:
    print('a能被2整除')
else:
    print('a不能被2整除')

if isinstance(a/2,float):
    print('a不能被2整除')
else:
    print('a能被2整除')