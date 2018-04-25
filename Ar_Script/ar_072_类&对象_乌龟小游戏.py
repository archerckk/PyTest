import random as r
'''
1.假设游戏场景为范围（x，y）为0<=x<=10 ,0<=y<=10——Y
2.游戏生成1只乌龟和10条鱼
3.他们的移动方向是随机——Y
4.乌龟的最大移动能力是2（它可以随机选择1还是2移动），鱼儿最大移动能力是
5.当移动到场景边缘，自动向反向移动——Y
6.体力初始化体力为100——Y
7.乌龟每移动一次，体力消耗1——Y
8.当乌龟和鱼的坐标重叠，乌龟吃掉鱼，乌龟体力增加20
9.鱼暂时不计算体力
10.当乌龟体力值为0（挂掉）或者鱼儿的数量为0游戏结束
'''


legal_x=[0,10]
legal_y=[0,10]

class Turtle:

    def __init__(self):
        self.hp=70
        self.pos=[r.randint(0,10),r.randint(0,10)]

    def move(self,pos):
        self.pos=pos
        def moving():
            nonlocal pos
            '乌龟移动减少体力'
            self.hp -= 1
            direction_x=r.randint(-1,1)
            direction_y=r.randint(-1,1)
            step=r.randint(1,2)
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


    def eat(self):
        newHp=self.hp+20
        if newHp<100:
            print('启动吃货技能,体力增加20,现在的体力为：%d'%(newHp))
        else:
            print('启动吃货技能,达到最大体力100')
        self.hp=newHp
        return self.hp


