import random

times=3
choice=['正面','反面']
toast='你要猜正面还是方面？1代表正面，2代表反面：'
while True:
    coinResult=random.choice(choice)
    guess=input(toast)
    if guess in ['1','2']:
        if (coinResult=='正面'and guess=='1')or (coinResult=='反面'and guess=='2'):
            print('硬币的随机结果是：{}'.format(coinResult))
            print('你猜对了！！！\n游戏结束！！！')
            break
        else:
            times-=1
            print('硬币的随机结果是：{}'.format(coinResult))
            toast='你还剩下{}次机会！请继续猜：'.format(times)
            if times==0:
                print('你的机会用完了，游戏结束！！！')
                break
    else:
        toast='你的输入有误！请输入1或者2：'
        continue
