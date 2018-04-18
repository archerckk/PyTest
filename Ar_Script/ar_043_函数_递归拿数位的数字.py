print()
'''
1 写一个函数get_digits(n)，将参数n分解出每个位的数字并按顺序存放在列表中。
如：get_digits(12345)——[1,2,3,4,5]
'''
result = []

def get_digits(n):
    if n > 0:
        result.insert(0, n % 10)
        get_digits(n // 10)
        '这里只是控制了执行的次数而已，每次的结果直接放在了外面的全局变量'
        '假如放在里面的话会重复的初始化，导致拿不到完整的列表'


get_digits(12345)
print(result)


'普通版本'
def get_digit2(n):
    result=[]
    '普通版本是先走完循环再出来的，不会重复初始化result，所以可以放在里面'
    while n>0:
        result.insert(0,n%10)
        n=n//10
    return result

print(get_digit2(12345))