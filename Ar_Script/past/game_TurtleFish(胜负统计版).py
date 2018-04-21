import random as r
import easygui as g

#定义有效的移动范围
legal_x=[0,10]
legal_y=[0,10]

class Turtle:

    def __init__(self):
        self.x=r.randint(0,10)
        self.y=r.randint(0,10)
        self.hp=100

    def move(self):
        #定义随机移动的步数
        step_x=r.choice([1,2,-1,-2])
        step_y=r.choice([1,2,-1,-2])
        new_x=self.x+step_x
        new_y=self.y+step_y

        #判断乌龟决定移动的方向和步数
        if step_x in [1,2]:
            print('乌龟决定向右移动，移动的步数为%s'%step_x)
        elif step_x in [-1,-2]:
            print('乌龟决定向左移动，移动的步数为%s'%(-1*step_x))

        if step_y in [1, 2]:
            print('乌龟决定向上移动，移动的步数为%s' % step_y)
        elif step_y in [-1, -2]:
            print('乌龟决定向下移动，移动的步数为%s' % (-1*step_y))


        #计算x轴的坐标移动
        if new_x<legal_x[0]:
            self.x=legal_x[0]-(new_x-legal_x[0])
            print('超出左边界，重新调整位置')
        elif new_x>legal_x[1]:
            self.x = legal_x[1] - (new_x - legal_x[1])
            print('超出右边界，重新调整位置')
        else:
            self.x=new_x
            print('正常移动')

        # 计算y轴的坐标移动
        if new_y < legal_y[0]:
            self.y = legal_y[0] - (new_y - legal_y[0])
            print('超出上边界，重新调整位置')
        elif new_y > legal_y[1]:
            self.y = legal_y[1] - (new_y - legal_y[1])
            print('超出下边界，重新调整位置')
        else:
            self.y = new_y
            print('正常移动')

        #移动后乌龟的体力要-1
        self.hp-=1
        print('移动后，体力-1，现在的体力为：%d' % self.hp)

        print('乌龟现在的位置为：【%s,%s】'%(self.x,self.y))

        return (self.x,self.y)

    def eat(self):
        self.hp+=20
        if self.hp>=100:
            print('乌龟发动吃鱼技能，吃掉小鱼一条，乌龟的体力恢复到最大值。剩余的鱼儿数量为：%d'%len(fish_list))
        else:
            print('乌龟发动吃鱼技能，吃掉小鱼一条，恢复20体力，现在的体力为：%d,剩余的鱼儿数量为：%d'%(self.hp,len(fish_list)))

class Fish:

    def __init__(self):
        self.x=r.randint(0,10)
        self.y=r.randint(0,10)

    def move(self):
        #定义随机移动的步数
        step_x=r.choice([1,-1])
        step_y=r.choice([1,-1])
        new_x=self.x+step_x
        new_y=self.y+step_y

        #判断乌龟决定移动的方向和步数
        # if step_x in [1]:
        #     print('鱼决定向右移动，移动的步数为%s'%step_x)
        # elif step_x in [-1]:
        #     print('鱼决定向左移动，移动的步数为%s'%step_x)
        #
        # if step_y in [1]:
        #     print('鱼决定向上移动，移动的步数为%s' % step_y)
        # elif step_y in [-1]:
        #     print('鱼决定向下移动，移动的步数为%s' % step_y)


        #计算x轴的坐标移动
        if new_x<legal_x[0]:
            self.x=legal_x[0]-(new_x-legal_x[0])
            # print('超出左边界')
        elif new_x>legal_x[1]:
            self.x = legal_x[1] - (new_x - legal_x[1])
            # print('超出右边界，')
        else:
            self.x=new_x
            # print('正常移动')

        # 计算y轴的坐标移动
        if new_y < legal_y[0]:
            self.y = legal_y[0] - (new_y - legal_y[0])

        elif new_y > legal_y[1]:
            self.y = legal_y[1] - (new_y - legal_y[1])

        else:
            self.y = new_y


        return (self.x,self.y)

    def show_position(self):
        print('鱼儿现在的坐标为：【%s,%s】'%(self.x,self.y))



class Shark(Fish):

    def show_position(self):
        print('鲨鱼宝宝现在的坐标为：【%s,%s】'%(self.x,self.y))

    def eat(self):
        g.msgbox('鲨鱼宝宝发动吃货技能，将乌龟吃掉啦！！鲨鱼宝宝获得胜利！！')

#对象的初始化，将所有的对象都先放置好
turtle = Turtle()
fish_list = []
shark_list = []
shark = Shark()
shark_list.append(shark)
for i in range(10):
    fish_new = Fish()
    fish_list.append(fish_new)

print('乌龟的初始位置为：【%s,%s】' % (turtle.x, turtle.y))


def cal_result():
    # win=0
    # lose=0
    target=0
    def cal_in():
        # nonlocal win
        # nonlocal lose
        nonlocal target
        meet_times = 0
        judge_in = False


        # while 1:
        while 1 :

            if not turtle.hp:
                g.msgbox('乌龟的体力值为0，已经游不动了，鱼儿阵营获得胜利')
                target=1

                break
            if not len(fish_list):
                g.msgbox('鱼儿都被乌龟吃光了，还成功躲开了鲨鱼的追捕，乌龟获得胜利！！')
                target=0
                break
            if judge_in:
                break

            turtle_pos=turtle.move()


            for each_fish in fish_list[:]:
                if each_fish.move()==turtle_pos:
                    turtle.eat()
                    fish_list.remove(each_fish)

            for each_shark in shark_list[:]:
                shark.show_position()
                if each_shark.move()==turtle_pos:
                    print('乌龟已经被鲨鱼宝宝捉到一次，再被捉到就要被吃掉啦！！！')
                    meet_times+=1
                if each_shark.move()==turtle_pos and meet_times==1:
                    each_shark.eat()
                    judge_in=True
                    target = 2
                    break


        return target
    return cal_in

contiue=True
get_result=cal_result()

win=0
lose=0
choices = ['乌龟', '鱼儿', '鲨鱼']

while 1:
    if contiue:
        guess = g.indexbox(msg='请选择你觉得会获胜的动物:', title='你的选择', choices=choices)
        result=get_result()
        if guess == result:
            g.msgbox('你猜中了，胜场数+1')
            win += 1
        elif guess != result:
            g.msgbox('你猜错了，负场数+1')
            lose += 1
        g.msgbox('你现在的战绩是：\n胜：%d场\t\t负：%d场' % (win, lose))
        contiue = g.ccbox('你是否继续游戏', '提示', choices=['是', '否'])
    else:
        g.msgbox('你的最终战绩是：\n胜：%d场\t\t负：%d场' %(win, lose))
        g.msgbox('游戏结束')
        break



