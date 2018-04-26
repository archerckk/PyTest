import easygui as g
import random as r
from Ar_Script.past import game_NameFormat as nf
from Ar_Script.past import game_FingerGuess as fg
from Ar_Script.past import game_TurtleFish_New as tf
from Ar_Script.past import game_GuessNum as gn


class Game_main:
    def __init__(self):
        self.menu = 0

    def game_start(self,menu):
        msg = '请选择你的游戏：'
        title = '小霸王游戏机'
        choices = ['知你所想', '数字大师', '疯狂猜拳', '乌龟和鱼']

        while 1:
            self.menu = g.indexbox(msg, title, choices)
            if self.menu == 0:
                nf.nameFormat.game_start()
                continue
            elif self.menu == 1:
                guessNum = gn.GuessNum()
                guessNum.game_start()
                continue
            elif self.menu == 2:
                player = fg.Player()
                computer = fg.Computer()
                game = fg.Game()
                game.judge(player, computer)
                continue
            elif self.menu == 3:
                turtle = tf.Turtle()
                fish = tf.Fish()
                shark = tf.Shark()
                game = tf.Game()
                game.game_start(turtle, fish, shark)
                continue
            else:
                judge=g.ccbox('是否结束游戏？','提示',['是','否'])
                if judge:
                    break
                else:
                    self.menu = g.indexbox(msg, title, choices)


gameMain=Game_main()
gameMain.game_start(gameMain.menu)
