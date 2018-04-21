class Ticket():
    def __init__(self,weekend=False,child=False):
        self.price=100
        #假如是周末，加收20%，非周末不加收
        if weekend:
            self.extra=1.2
        else:
            self.extra=1
        #假如是小孩，打五折，成人不打折
        if child:
            self.discount=0.5
        else:
            self.discount=1
    def calPrice(self,num):
        return self.price*self.extra*self.discount*num

adult=Ticket()
children=Ticket(child=True)
adult.price=adult.calPrice(2)
children.price=children.calPrice(1)

print('在平常的时间里，两张成人票加一张儿童票的价格为：%2.f'%(children.price+adult.price))