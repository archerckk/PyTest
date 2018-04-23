import random
'''
1.用户用有三次输入数字的机会（范围：0-9）
2.用户输入目标数字提示"你真是神算子，第一次就猜对了！"
3.用户输入数字不等与目标数字
    大了提示大了，同时计算上下次数
    小了提示小了，同时计算剩下次数
4.机会用完提示"机会用完了！笨！这都猜不到！"
5.对于异常情况要用try 异常处理机制处理
'''
#
def guessNum():
    times=3
    target=random.randint(1,10)
    toast='请输入你要猜的数字（1到9）:'
    while 1:
        try:
            guess=int(input(toast))
            if guess==target and times==3:
                print("\n你真是神算子，第一次就猜对了！")
                break
            else:
                times -= 1
                if guess>target and times>0:
                    toast='\n你猜大了！你还有%d次机会！请再猜：'%times
                if guess<target and times>0:
                    toast='\n你猜小了！你还有%d次机会！请再猜：'%times
                if times==0:
                    print('\n机会用完了！笨！这都猜不到！')
                    break
        except ValueError:
                toast='\n你输入了非数字字符！请重新输入：'

                '这个错误也是醉了，自己一直想着让游戏继续，其实这种错误执行不了的话，可以选择让游戏结束的'
        except EOFError:
                print('异常操作！！！游戏结束！')
                break

guessNum()


