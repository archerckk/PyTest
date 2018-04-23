import random
import sys
import easygui as g

def guessNum():
    times=3
    target=random.randint(1,10)
    toast='请输入你要猜的数字（1到9）'
    while 1:
        try:
            guess=g.integerbox(toast,lowerbound=1,upperbound=9)
            # guess=int(input(toast))
            if guess==target and times==3:
                msg="你真是神算子，第一次就猜对了！"
                g.msgbox(msg,'提示')
                sys.exit()
            else:
                times -= 1
                if guess>target and times>0:
                    toast='你猜大了！你还有%d次机会！请再猜：'%times
                if guess<target and times>0:
                    toast='你猜小了！你还有%d次机会！请再猜：'%times
                if times==0:
                    msg='机会用完了！笨！这都猜不到！'
                    g.msgbox(msg,'提示')
                    break
        except ValueError:
                toast='你输入了非数字字符！请重新输入：'

                '这个错误也是醉了，自己一直想着让游戏继续，其实这种错误执行不了的话，可以选择让游戏结束的'
        except EOFError:
                print('异常操作！！！游戏结束！')
                sys.exit()

guessNum()