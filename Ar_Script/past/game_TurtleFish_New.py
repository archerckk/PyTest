import easygui as g
import random as r

legal_x = [0, 5]
legal_y = [0, 5]


class Turtle:
    def __init__(self):
        self.hp = 10
        self.x = r.randint(legal_x[0], legal_x[1])
        self.y = r.randint(legal_y[0], legal_y[1])
        # self.x = 0
        # self.y = 0
        g.msgbox('乌龟的初始位置为：【%s,%s】' % (self.x, self.y))

    def move(self):
        step_x = r.choice([-1, -2, -3, 1, 2, 3])
        step_y = r.choice([-1, -2, -3, 1, 2, 3])
        new_x = self.x + step_x
        new_y = self.y + step_y

        # 计算x轴的坐标，超出左右边界需要调整
        if new_x < legal_x[0]:
            self.x = legal_x[0] - (new_x - legal_x[0])
        elif new_x > legal_x[1]:
            self.x = legal_x[1] - (new_x - legal_x[1])
        else:
            self.x = new_x

        # 计算y轴的坐标，超出左右边界需要调整
        if new_y < legal_y[0]:
            self.y = legal_y[0] - (new_y - legal_y[0])
        elif new_y > legal_y[1]:
            self.y = legal_y[1] - (new_y - legal_y[1])
        else:
            self.y = new_y

        # 移动后乌龟体力值-1
        self.hp -= 0.5

        return (self.x, self.y)

    def stay(self):
        self.x = self.x
        self.y = self.y
        self.hp -=5

        return (self.x, self.y)

    def eat(self):
        # self.hp += 20
        # if self.hp >= 100:
        #     self.hp = 100
        #     g.msgbox('乌龟吃掉了一条鱼儿，乌龟体力恢复到最大值')
        # else:
        #     g.msgbox('乌龟吃掉了一条鱼儿，乌龟体力恢复20点体力值，现在的体力为：%d' % self.hp)
        g.msgbox('游戏胜利！！！闪电龟并不是浪得虚名的，渣渣鱼儿哪里跑！！！')


class Fish:
    def __init__(self):
        self.x = r.randint(legal_x[0], legal_x[1])
        self.y = r.randint(legal_y[0], legal_y[1])

    def move(self):
        step_x = r.choice([-1, 1])
        step_y = r.choice([-1, 1])
        new_x = self.x + step_x
        new_y = self.y + step_y

        # 计算x轴的坐标，超出左右边界需要调整
        if new_x < legal_x[0]:
            self.x = legal_x[0] - (new_x - legal_x[0])
        elif new_x > legal_x[1]:
            self.x = legal_x[1] - (new_x - legal_x[1])
        else:
            self.x = new_x

        # 计算y轴的坐标，超出左右边界需要调整
        if new_y < legal_y[0]:
            self.y = legal_y[0] - (new_y - legal_y[0])
        elif new_y > legal_y[1]:
            self.y = legal_y[1] - (new_y - legal_y[1])
        else:
            self.y = new_y

        return (self.x, self.y)


class Shark(Fish):
    def eat(self):
        g.msgbox('游戏失败！！出师未捷身先死，竟然被鲨鱼吃掉了T_T')


class Game:
    def __init__(self):
        self.judge = 0
        self.stop = True

    def game_move(self, Turtle, Fish, Shark):
        msg = '请选择：'
        title = '你的选择'
        choice = ['开始暴走', '守株待鱼']
        self.judge = g.indexbox(msg, title, choice)
        if self.judge == 0:
            Turtle.move()
            # g.msgbox(msg='乌龟现在的位置为：【%s,%s】' % (Turtle.x, Turtle.y))
        else:
            Turtle.stay()
        # g.msgbox(msg='乌龟现在的位置为：【%s,%s】' % (Turtle.x, Turtle.y))
        Fish.move()
        Shark.move()

    def game_judge(self, Turtle, Fish, Shark):
        pos_t=(Turtle.x,Turtle.y)
        pos_f = (Fish.x, Fish.y)
        pos_s = (Shark.x, Shark.y)


        if pos_t==pos_f:
            Turtle.eat()
            self.stop = False
        elif pos_s==pos_t:
            Shark.eat()
            self.stop = False
        elif Turtle.hp<=0:
            g.msgbox(' 游戏失败！！！又多了一直过劳而死的乌龟，真是长使英雄泪满襟……')
            self.stop = False
        elif self.judge==None:
            g.msgbox('游戏进行中不能中断，默认选择【守株待鱼】\n乌龟现在的位置为：【%s,%s】 剩余体力值为：'
                     '%.1f\n鱼现在的位置为：【%s,%s】\n鲨鱼现在的位置为：【%s,%s】' %
                     (Turtle.x, Turtle.y, Turtle.hp, Fish.x, Fish.y, Shark.x, Shark.y))
        else:
            g.msgbox('乌龟现在的位置为：【%s,%s】 剩余体力值为：%.1f\n鱼现在的位置为：【%s,%s】\n鲨鱼现在的位置为：【%s,%s】' %
                     (Turtle.x, Turtle.y, Turtle.hp,Fish.x, Fish.y, Shark.x, Shark.y))


    def game_start(self,Turtle, Fish, Shark):
        while self.stop:
           self.game_move(Turtle, Fish, Shark)
           self.game_judge(Turtle, Fish, Shark)


# turtle = Turtle()
# fish = Fish()
# shark = Shark()
# game = Game()
# game.game_start(turtle,fish,shark)
