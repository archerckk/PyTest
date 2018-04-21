import easygui as g
import random as r

class GuessNum:

    def __init__(self):
        self.guess=0
        self.times=3
        self.target=r.randint(1,10)

    def game_start(self):
        guess_msg = '请输入1-10之内的数字：'
        guess_title = '猜猜猜'

        while 1:
            if self.times>0:
                self.guess = g.integerbox(guess_msg, guess_title, lowerbound=1, upperbound=10)
                try:
                    if self.guess==self.target and self.times==3:
                        g.msgbox('真厉害！，第一次就猜中了，你这么厉害：发一个红包给我吧！！')
                        g.msgbox('游戏结束')
                        break
                    elif self.guess==self.target:
                        g.msgbox('真厉害！，竟然猜中了，我让你亲一下好了！！')
                        g.msgbox('游戏结束！')
                        break
                    else:
                        self.times -= 1
                        if self.guess>self.target:
                            g.msgbox('不好意思，你猜的数字大了！！您还有%d次机会'%self.times)
                        elif self.guess<self.target:
                            g.msgbox('不好意思，你猜的数字小了！！您还有%d次机会'%self.times)
                except TypeError:
                    g.msgbox('游戏中断')
                    break
            else:
                g.msgbox('游戏结束')
                break


# guessNum=GuessNum()
# guessNum.game_start()