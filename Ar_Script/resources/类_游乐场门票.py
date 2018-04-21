class Ticket:

    time=[1,2]
    price = 100
    man_num=0
    children_num=0
    total=0

    def getTime(self):
        self.time = int(input('请输入你要游玩的时间：1为【平常时间】，2为【周末】:'))
        if self.time==1:
            return self.time
        if self.time==2:
            return self.time

    def getNum(self):
        self.man_num=int(input('请输入你要购买的成人票数量(如不需要购买请输入【0】)：'))
        self.children_num=int(input('请输入你要购买的儿童票数量(如不需要购买请输入【0】)：'))


    def countPrice(self):
        if self.time==1:
            self.total=(self.price*self.man_num)+(self.price*self.children_num*0.5)
            print('你购买了平常时间的成人票%d张，儿童票%d张，累计%d元'%(self.man_num,self.children_num,self.total))
        if self.time==2:
            self.total=(self.price*self.man_num*1.2)+(self.price*self.children_num*1.2*0.5)
            print('你购买了周末的成人票%d张，儿童票%d张，累计%d元'%(self.man_num,self.children_num,self.total))

test_ticket=Ticket()
test_ticket.getTime()
test_ticket.getNum()
test_ticket.countPrice()