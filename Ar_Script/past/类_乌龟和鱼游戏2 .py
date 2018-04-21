import random as r
leagal_x=[0,10]
leagal_y=[0,10]

class Turtle:
    def __init__(self):
        #初始化体力值
        self.hp=100
        #初始化随机的起始位置
        self.x=r.randint(leagal_x[0],leagal_x[1])
        self.y = r.randint(leagal_y[0], leagal_y[1])

    def move(self):
        new_x=self.x+r.choice([1,2,-1,-2])
        new_y=self.y+r.choice([1,2,-1,-2])

        #计算X坐标的移动
        if new_x<leagal_x[0]:
            self.x=leagal_x[0]-(new_x-leagal_x[0])
            print('乌龟决定移动%d步')
        elif new_x>leagal_x[1]:
            self.x=leagal_x[1]-(new_x-leagal_x[1])
            print('x2')
        else:
            self.x=new_x
            print('x3')

        # 计算y坐标的移动
        if new_y < leagal_y[0]:
            self.y = leagal_y[0] - (new_y - leagal_y[0])
            print('y1')
        elif new_y > leagal_y[1]:
            self.y = leagal_y[1] - (new_y- leagal_y[1])
            print('y2')
        else:
            self.y = new_y
            print("y3")

        #记得移动后体力要减一，不然乌龟就一直吃了
        self.hp-=1
        #返回新的坐标
        return (self.x,self.y)

    def showPosition(self):
        print('乌龟现在的位置为：%s'%([self.x,self.y]))

    def eat(self):
        self.hp+=20
        if self.hp>100:
            self.hp=100

class Fish:
    def __init__(self):
        #初始化随机的起始位置
        self.x=r.randint(leagal_x[0],leagal_x[1])
        self.y = r.randint(leagal_y[0], leagal_y[1])

    def move(self):
        new_x=self.x+r.choice([1,-1])
        new_y=self.y+r.choice([1,-1])

        #计算X坐标的移动
        if new_x<leagal_x[0]:
            self.x=leagal_x[0]-(new_x-leagal_x[0])
        elif new_x>leagal_x[1]:
            self.x=leagal_x[1]-(new_x-leagal_x[1])
        else:
            self.x=new_x

        # 计算y坐标的移动
        if new_y < leagal_y[0]:
            self.y = leagal_y[0] - (new_y - leagal_y[0])
        elif new_y > leagal_y[1]:
            self.y = leagal_y[1] - (new_y- leagal_y[1])
        else:
            self.y = new_y

        #返回新的坐标
        return (self.x,self.y)

#实例化乌龟类
turtle=Turtle()
fish=[]
for each_fish in  range(10):
    new_fish=Fish()
    fish.append(new_fish)

while 1:
    if not turtle.hp:
        print('乌龟体力没有咯，挂掉咯，游戏结束！！！')
        break
    if not len(fish):
        print('鱼儿都被乌龟吃完咯，游戏结束！！!')
        break
    pos = turtle.move()
    turtle.showPosition()

    for each_fish in fish[:]:
        if each_fish.move()==pos:
            turtle.eat()
            fish.remove(each_fish)
            #这里用pop()得出来的结果也是正确的
            print('有一条鱼儿被吃掉咯！！！')
