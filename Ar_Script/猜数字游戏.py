'''
1.能使用随机数
2.用户猜对了提示信息
3.用户猜错能显示用户猜大了还是猜小了
4.机会一共只有3次
5.用户用完三次机会或者猜对了游戏结束
'''

import random
target=random.randint(1,10)
times=3
while times!=0:
    tmp=input('请输入你要猜的数字：')
    while not tmp.isdigit():
        tmp=input('你的输入有误，请重新输入：')
    guess=int(tmp)
    times-=1
    if target==guess:
        print('好牛叉，这就猜对了')
        break
    else:
        if guess>target:
            print('你猜的数字大了')
        elif guess<target:
            print('你猜的数字小了')
        if times>0:
            print('你还有%d次机会'%times)
        else:
            print('你的3次机会已经用完')
print('游戏结束')

