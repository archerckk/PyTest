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
        choice_x=r.choice([1,2,-1,-2])
        if choice_x in[1,2]:
            print('乌龟决定向右移动%d步'%choice_x)
        elif choice_x in [-1,-2]:
            print('乌龟决定向左移动%d步'%(-1*choice_x))
        choice_y = r.choice([1, 2, -1, -2])
        if choice_y in[1,2]:
            print('乌龟决定向上移动%d步'%choice_y)
        elif choice_y in [-1,-2]:
            print('乌龟决定向下移动%d步'%(-1*choice_y))
        new_x=self.x+choice_x
        new_y=self.y+choice_y

        if new_x<leagal_x[0]:
            self.x=leagal_x[0]-(new_x-leagal_x[0])
            print('乌龟，超出最小边界，重新调整位置！！')
        elif new_x>leagal_x[1]:
            self.x=leagal_x[1]-(new_x-leagal_x[1])
            print('乌龟，超出最大边界，重新调整位置！！')
        else:
            self.x=new_x
            if choice_x in [1, 2]:
                print('乌龟，正常向右移动%d步' % choice_x)
            elif choice_x in [-1, -2]:
                print('乌龟，正常向左移动%d步' % (-1 * choice_x))

        # 计算y坐标的移动
        if new_y < leagal_y[0]:
            self.y = leagal_y[0] - (new_y - leagal_y[0])
            print('乌龟超出最低边界，重新调整位置！！')
        elif new_y > leagal_y[1]:
            self.y = leagal_y[1] - (new_y- leagal_y[1])
            print('乌龟超出最高边界，重新调整位置！！')
        else:
            self.y = new_y
            if choice_y in [1, 2]:
                print('乌龟，正常向上移动%d步' % choice_y)
            elif choice_y in [-1, -2]:
                print('乌龟，正常向下移动%d步' % (-1 * choice_y))

        #记得移动后体力要减一，不然乌龟就一直吃了
        self.hp-=1
        print('移动后，体力-1，现在的体力为：%d'%self.hp)
        #返回新的坐标
        return (self.x,self.y)

    def showPosition(self):
        print('乌龟现在的位置为：%s'%([self.x,self.y]))

    def eat(self):
        self.hp+=20
        print('发动吃鱼技能，鱼儿被吃掉咯！！！吃掉鱼儿一条，恢复体力20,现在的体力为：%d'%self.hp)
        if self.hp>100:
            self.hp=100
            print('乌龟体力恢复到最大值')

class Fish:
    def __init__(self):
        #初始化随机的起始位置
        self.x=r.randint(leagal_x[0],leagal_x[1])
        self.y = r.randint(leagal_y[0], leagal_y[1])

    def move(self):
        choice_x=r.choice([1,-1])
        choice_y = r.choice([1, -1])

        new_x=self.x+choice_x
        new_y=self.y+choice_y

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



        return (self.x,self.y)

    def showPosition(self):
        print('鱼现在的位置为：%s'%([self.x,self.y]))

class Goldfish(Fish):
    pass

class Carp(Fish):
    pass

class Salmon(Fish):
    pass

class Shark(Fish):

    def __init__(self):
        super().__init__()
        self.hungry=True

    def eat(self):
        if self.hungry:
            print("鲨鱼宝宝启动吃货技能,乌龟已经被吃掉，鱼儿获得胜利！！\n游戏结束！！")
            self.hungry=False
        else:
            print('鲨鱼宝宝已经吃饱了')

    def showPosition(self):
        print('鲨鱼现在的位置为：%s' % ([self.x, self.y]))

#实例化乌龟类
turtle=Turtle()
fish=[]
shark=[Shark()]
judge=False

for each_fish in  range(10):
    small_fish=r.choice([Salmon(),Carp(),Goldfish()])
    big_fish=Shark()
    fish.append(r.choice([small_fish,big_fish]))

print('乌龟的初始位置为%s：'%([turtle.x,turtle.y]))
while 1:
    if not turtle.hp:
        print('乌龟体力已经为0，鱼儿获得胜利!!!\n游戏结束！！！')
        break
    if not len(fish):
        print('鱼儿都被乌龟吃完咯，乌龟获得胜利!!!\n游戏结束！！！')
        break
    if judge:
        break
    pos = turtle.move()
    turtle.showPosition()


    for each_fish in fish[:]:
        if each_fish.move()==pos:
            print('乌龟的坐标为：%s,鱼的坐标为：%s'%([turtle.x,turtle.y],[each_fish.x,each_fish.y]))
            turtle.eat()
            fish.remove(each_fish)
            #这里用pop()得出来的结果也是正确的
            print('剩余的鱼儿数量为：%d'%(len(fish)))

    for each_shark in shark[:]:
        each_shark.showPosition()
        if each_shark.move()==pos:
            print('乌龟的坐标为：%s,鲨鱼的坐标为：%s'%([turtle.x,turtle.y],[each_shark.x,each_shark.y]))
            each_shark.eat()
            judge=True
            break
