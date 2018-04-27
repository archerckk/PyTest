import easygui as g
import sys
from Ar_Script import ar_063_easygui_猜数字游戏 as gnum
from Ar_Script.past import game_TurtleFish_New as tf
from Ar_Script import ar_074_类和对象_猜拳游戏 as gfin
from Ar_Script import ar_075_类和对象_乌龟与鱼群 as fs


class GameBox:
    def __init__(self):
        self.choices = 0

    def gameStart(self,decide):
        self.choices=decide

        while 1:
            msg = '请选择你要玩的游戏：'
            title = '游戏选择'
            choice = ['猜数字游戏', '乌龟与鱼', '疯狂猜猜猜', '乌龟与鱼加强版']
            self.choices = g.indexbox(msg, title, choice)
            if self.choices == 0:
                guessNum=gnum.GuessNum()
                guessNum.gameStart()
                continue
            elif self.choices == 1:
                turtle = tf.Turtle()
                fish = tf.Fish()
                shark = tf.Shark()
                game = tf.Game()
                game.game_start(turtle, fish, shark)
                continue
            elif self.choices==2:
                player=gfin.Player()
                compuer=gfin.Computer()
                game=gfin.Game(player,compuer)
                game.gameStart()
                continue
            elif self.choices==3:
                turtle = fs.Turtle()
                fishlist = []
                game2 = fs.Game(turtle, fishlist)
                game2.gameStart()
            else:
                judge=g.ccbox('是否退出游戏','提示',choices=(['是','否']))
                if judge:
                    continue
                else:
                    sys.exit()


gameBox = GameBox()
decide=0
gameBox.gameStart(decide)
