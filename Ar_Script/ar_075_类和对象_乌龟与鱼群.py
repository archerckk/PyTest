import random as r
import easygui as g
import sys
'''
1.假设游戏场景为范围（x，y）为0<=x<=10 ,0<=y<=10——Y
2.游戏生成1只乌龟和3条鱼——Y
3.他们的移动方向是随机——Y
4.乌龟的最大移动能力是2（它可以随机选择1还是2移动），鱼儿最大移动能力是1——Y
5.当移动到场景边缘，自动向反向移动——Y
6.体力初始化体力为100——Y
7.乌龟每移动一次，体力消耗1——Y
8.当乌龟和鱼的坐标重叠，乌龟吃掉鱼，乌龟体力增加20——Y
9.鱼暂时不计算体力——Y
10.当乌龟体力值为0（挂掉）或者鱼儿的数量为0游戏结束——Y
'''


legal_x=[0,5]
legal_y=[0,5]

class Turtle:

    def __init__(self):
        self.hp=100
        self.pos=[r.randint(0,10),r.randint(0,10)]

    def move(self):

            '乌龟移动减少体力'
            self.hp -= 1
            # msgX='-1代表左移动，1代表右移动'
            # msgY='-1代表下移动，1代表上移动'
            # title='移动方向选择'
            # choices=['-1','1']
            # direction_x = g.buttonbox(msgX,title,choices)
            # direction_y = g.buttonbox(msgY, title, choices)

            direction_x = r.choice([-1, 1])
            direction_y = r.choice([-1, 1])
            step=r.randint(1,2)

            try:
                newX=self.pos[0]+int(direction_x)*step
                newY=self.pos[1]+int(direction_y)*step

                if newX<legal_x[0]:
                    self.pos[0]=legal_x[0]-(newX-legal_x[0])
                elif newX>legal_x[1]:
                    self.pos[0]=legal_x[1]-(newX-legal_x[1])
                else:
                    self.pos[0]=newX

                if newY<legal_y[0]:
                    self.pos[1]=legal_y[0]-(newY-legal_y[0])
                elif newY>legal_y[1]:
                    self.pos[1]=legal_y[1]-(newY-legal_y[1])
                else:
                    self.pos[1]=newY
            except TypeError:
                sys.exit()
            return self.pos

    def eat(self):
        newHp=self.hp+20
        if newHp<100:
            print('吃掉小鱼一条,体力增加20,现在的体力为：%d'%(newHp))
        else:
            newHp=100
            print('吃掉小鱼一条,达到最大体力100')

        self.hp=newHp
        return self.hp


class Fish:

    def __init__(self):
        self.num=1
        self.pos = [r.randint(0, 10), r.randint(0, 10)]

    def move(self):
        direction_x=r.choice([-1,1])
        direction_y=r.choice([-1,1])
        step=1
        newX=self.pos[0]+direction_x*step
        newY=self.pos[1]+direction_y*step

        if newX<legal_x[0]:
            self.pos[0]=legal_x[0]-(newX-legal_x[0])
        elif newX>legal_x[1]:
            self.pos[0]=legal_x[1]-(newX-legal_x[1])
        else:
            self.pos[0]=newX

        if newY<legal_y[0]:
            self.pos[1]=legal_y[0]-(newY-legal_y[0])
        elif newY>legal_y[1]:
            self.pos[1]=legal_y[1]-(newY-legal_y[1])
        else:
            self.pos[1]=newY


        return self.pos


class Game:
    def __init__(self):
        self.turtle=Turtle()
        self.times=10
        self.win=0
        self.lost=0
        self.fishlist=[]
        for i in range(3):
            fish = Fish()
            self.fishlist.append(fish)

    def gameStart(self):
        # while 1:
        #     if self.times == 0:
        #         g.msgbox('你的战绩为：\n胜:%d场  负：%d场' % (win, lost))
        #         break
        while True:
            if not len(self.fishlist):
                print("胜利！鱼儿都吃完了，游戏结束！")
                self.times-=1
                self.win+=1
                break
            if not self.turtle.hp:
                print("失败！乌龟体力耗尽，挂掉了！")
                self.times -= 1
                self.lost+=1
                break

            pos = self.turtle.move()
            print('\n乌龟现在的所在位置为：', self.turtle.pos[0], self.turtle.pos[1])
            print('乌龟剩余体力为：',self.turtle.hp)

            # 在迭代器中删除列表元素是非常危险的，经常会出现意想不到的问题，因为迭代器是直接引用列表的数据进行引用
            # 这里我们把列表拷贝给迭代器，然后对原列表进行删除操作就不会有问题了^_^
            for each_fish in self.fishlist[:]:
                if each_fish.move() == pos:
                    # 鱼儿被吃掉了
                    self.turtle.eat()
                    self.fishlist.remove(each_fish)
                    # print('所剩下的鱼儿数量：%d'%(len(fish)))
                    # print('乌龟坐在位置：',turtle.x, turtle.y)
                    print('被吃鱼儿所在位置：', each_fish.pos[0], each_fish.pos[1])
                    print("有一条鱼儿被吃掉了...")
                    # print('所剩下的鱼儿数量：%d' % (len(fish)))
                else:
                    print('其他鱼儿的位置：', each_fish.pos[0], each_fish.pos[1])
            print('剩余鱼儿数量为：',len(self.fishlist))


    # def result(self):
    #     while 1:
    #         if self.times==0:
    #             g.msgbox('你的战绩为：\n胜:%d场  负：%d场' % (self.win, self.lost))
    #         else:
    #             # self.__init__()
    #             self.gameStart()



'参考配置'
game=Game()
# game.result()
# game.gameStart()