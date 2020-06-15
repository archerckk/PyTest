import random

#循环分支的练习代码
# target=random.randint(1,100)
# times=5
# while True:
#     if times==0:
#         print('你的次数已经全部用完了')
#         break
#     guess=int(input('请输入你要猜的数字：'))
#
#     if guess>target:
#         print('你猜大了，应该小一点')
#     elif guess<target:
#         print('你猜小了，应该大一点')
#     elif guess==target:
#         print('恭喜你，猜对了')
#         break
#     times-=1

def method(a):
    """
    :param a: 传参用于XXXX
    :return: 返回一个XXX
    """
    a+=1
    return a


print(method(2))