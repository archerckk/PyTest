import random

class Turtle:
    moveStep=random.randint(1,2)
    movedirection=0
    min_x=0
    max_x=10
    min_y=0
    max_y=10
    position=[0,0]
    hp=1005

    #随机生成乌龟的移动方向
    def getDirection(self):
        self.movedirection=random.randint(-1,1)
        if self.movedirection==-1:
            print('乌龟决定往回游,移动的步数为：%d'%self.moveStep)
        else:
            print('乌龟决定向前游,移动的步数为：%d' % self.moveStep)
        while self.movedirection==0:
            self.movedirection = random.randint(-1, 1)
        return self.movedirection

    def getRandomStep(self):
        self.moveStep=random.randint(1,2)

    #当乌龟达到场景边缘，会自动反方向移动
    def autoReturn(self):
        while self.position[0]==self.min_x and self.position[1]==self.max_y:
            self.position[0]+=self.moveStep
            self.position[1]+=self.moveStep
            print("到达边界，开始反方向移动，现在乌龟的位置为：%s" % self.position)
        while self.position[0] == self.max_x and self.position[1] == self.max_y:
            self.position[0]-=self.moveStep
            self.position[1] -= self.moveStep
            print("到达边界，开始反方向移动，现在乌龟的位置为：%s" % self.position)
        # while self.position==self.min_y:
        #     self.position[1]+=self.moveStep
        #     print("到达边界，开始反方向移动，现在乌龟的位置为：%s" % self.position)
        # while self.position==self.max_y:
        #     self.position[1]-=self.moveStep
        #     print("到达边界，开始反方向移动，现在乌龟的位置为：%s" % self.position)

    #乌龟的移动控制，假如一次性的移动数值超出边界，要将乌龟的定位返回到场景范围内
    def move(self):
        while self.movedirection == -1:
            tmp_x = self.position[0]
            tmp_y = self.position[1]
            tmp_x -= self.moveStep
            tmp_y -= self.moveStep
            if tmp_x < self.min_x and tmp_y < self.min_y:
                self.position[0] = self.min_x - tmp_x
                self.position[1] = self.min_y - tmp_y
            else:
                self.position[0] = tmp_x
                self.position[1] = tmp_y
            return self.position

        while self.movedirection == 1:
            tmp2_x = self.position[0]
            tmp2_y = self.position[1]
            tmp2_x += self.moveStep
            tmp2_y += self.moveStep
            if tmp2_x > self.max_x and tmp2_y > self.max_y:
                self.position[0] = tmp2_x - (tmp2_x - self.max_x)
                self.position[1] = tmp2_y - (tmp2_y - self.max_y)
            else:
                self.position[0] = tmp2_x
                self.position[1] = tmp2_y
            return self.position

    #计算乌龟的HP
    def countHp(self):
        # if self.move():
        #     self.hp-=1
        return self.hp


class Fish:
    moveStep = 1
    movedirection = 0
    min_x = 0
    max_x = 10
    min_y = 0
    max_y = 10
    position = [0, 0]
    num=10

    # 随机生成鱼的移动方向
    def getDirection(self):
        self.movedirection=random.randint(-1,1)
        while self.movedirection==0:
            self.movedirection = random.randint(-1, 1)
        return self.movedirection

    # 当鱼达到场景边缘，会自动反方向移动
    def autoReturn(self):
        while self.position==self.min_x:
            self.position[0]+=self.moveStep
            print("到达边界，自动返回，现在鱼的位置为：%s"%self.position)
        while self.position==self.max_x:
            self.position[0]-=self.moveStep
            print("到达边界，自动返回，现在鱼的位置为：%s" % self.position)
        while self.position==self.min_y:
            self.position[1]+=self.moveStep
            print("到达边界，自动返回，现在鱼的位置为：%s" % self.position)
        while self.position==self.max_y:
            self.position[1]-=self.moveStep
            print("到达边界，自动返回，现在鱼的位置为：%s" % self.position)

turtle=Turtle()
fish=Fish()

print('乌龟的起始坐标为：%s'%turtle.position)
print('鱼的起始坐标为：%s'%fis5h.position)

while 1:
    turtle.getDirection()
    turtle.moveStep
    turtle.move()
    turtle.autoReturn()
    print('乌龟的移动到新坐标：%s'%turtle.position)
    # break