import random as r
'''
1.假设游戏场景为范围（x，y）为0<=x<=10 ,0<=y<=10——Y
2.游戏生成1只乌龟和1条鱼——Y
3.他们的移动方向是随机——Y
4.乌龟的最大移动能力是2（它可以随机选择1还是2移动），鱼儿最大移动能力是1——Y
5.当移动到场景边缘，自动向反向移动——Y
6.体力初始化体力为100——Y
7.乌龟每移动一次，体力消耗1——Y
8.当乌龟和鱼的坐标重叠，乌龟对鱼发动攻击，鱼体力减少1，乌龟体力增加20——Y
9.鱼体力为10,每收到一次攻击体力减1——Y
10.当乌龟体力值为0（挂掉）或者鱼儿体力为0游戏结束——Y
'''


legal_x=[0,10]
legal_y=[0,10]

class Turtle:

    def __init__(self):
        self.hp=100
        self.pos=[r.randint(0,10),r.randint(0,10)]

    def move(self,pos):

        def moving():
            nonlocal pos

            '乌龟移动减少体力'
            self.hp -= 1

            direction_x=r.choice([-1,1])
            direction_y=r.choice([-1,1])
            step=r.randint(1,2)
            newX=pos[0]+direction_x*step
            newY=pos[1]+direction_y*step


            '另外的实现方式：r.choice[选项列表]'
            '随机计算方向并移动到新的位置（x, y）'
            # new_x = self.x + r.choice([1, 2, -1, -2])
            # new_y = self.y + r.choice([1, 2, -1, -2])


            if newX<legal_x[0]:
                pos[0]=legal_x[0]-(newX-legal_x[0])
            elif newX>legal_x[1]:
                pos[0]=legal_x[1]-(newX-legal_x[1])
            else:
                pos[0]=newX

            if newY<legal_y[0]:
                pos[1]=legal_y[0]-(newY-legal_y[0])
            elif newY>legal_y[1]:
                pos[1]=legal_y[1]-(newY-legal_y[1])
            else:
                pos[1]=newY

            return pos
        return moving


    def eat(self):
        newHp=self.hp+20
        if newHp<100:
            print('发动攻击,体力增加20,现在的体力为：%d'%(newHp))
        else:
            newHp=100
            print('发动攻击,达到最大体力100')

        self.hp=newHp
        return self.hp


class Fish:

    def __init__(self):
        self.hp=5
        self.pos = [r.randint(0, 10), r.randint(0, 10)]

    def move(self,pos):
        self.pos=pos
        def moving():
            nonlocal pos

            direction_x=r.choice([-1,1])
            direction_y=r.choice([-1,1])
            step=1
            newX=pos[0]+direction_x*step
            newY=pos[1]+direction_y*step

            if newX<legal_x[0]:
                pos[0]=legal_x[0]-(newX-legal_x[0])
            elif newX>legal_x[1]:
                pos[0]=legal_x[1]-(newX-legal_x[1])
            else:
                pos[0]=newX

            if newY<legal_y[0]:
                pos[1]=legal_y[0]-(newY-legal_y[0])
            elif newY>legal_y[1]:
                pos[1]=legal_y[1]-(newY-legal_y[1])
            else:
                pos[1]=newY

            return pos
        return moving

    def randomPos(self,pos):
        self.pos=pos

turtle=Turtle()
fish=Fish()

turtleMove=turtle.move(turtle.pos)
fishMove=fish.move(fish.pos)

'个人配置'
while 1:
    if turtle.hp>0:
        turtleMove()
        print('\n现在乌龟的体力为：%d，坐标为：%s' % (turtle.hp,turtle.pos))
    else:
        print('乌龟已经气绝身亡，游戏结束！')
        break

    fishMove()
    print('现在鱼儿的体力为：%d，坐标为：%s'%(fish.hp,fish.pos))

    if turtle.pos==fish.pos:
        turtle.eat()
        fish.hp-=1
        print('现在鱼儿的数量为：%d'%fish.hp)
    if fish.hp==0:
        print('乌龟已成功将鱼儿干掉了！游戏结束')
        break




