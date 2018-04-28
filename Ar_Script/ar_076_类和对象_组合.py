class Turtle:

    def __init__(self,num):
        self.num=num


class Fish:

    def __init__(self,num):
        self.num=num

class Pool:

    def __init__(self):
        self.turtle=Turtle(20)
        self.fish=Fish(29)

    def pirintNum(self):
        print('现在水池里面有%d只乌龟，%d条鱼'%(self.turtle.num,self.fish.num))



pool=Pool()
pool.pirintNum()
