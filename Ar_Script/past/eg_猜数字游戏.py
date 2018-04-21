import easygui as g
import random

target=random.randint(1,10)
g.msgbox('欢迎进入猜数字小游戏')
msg='请输入1-10之中的数字'
title='猜数字游戏'
guess=g.integerbox(msg=msg,title=title,lowerbound=1,upperbound=10)
times=3
while True:
    if guess==target and times==3:
        g.msgbox('这是作弊的嘛，第一次就猜中了')
        g.msgbox('作为奖励，给你亲一下吧')
        break
    elif guess==target:
        g.msgbox('好厉害！！，居然猜中了')
        g.msgbox('然而并没有奖品，哈哈^_^')
        break
    else:
        times-=1
        if guess>target:
            g.msgbox('你猜的数字大了，你还有%d次机会'%times)
        elif guess<target:
            g.msgbox('你猜的数字小了，你还有%d次机会'%times)
        guess = g.integerbox(msg=msg, title=title, lowerbound=1, upperbound=10)
        if times==1:
            g.msgbox('真遗憾，你的3次机会已经用完了')
            break
g.msgbox('游戏结束')

