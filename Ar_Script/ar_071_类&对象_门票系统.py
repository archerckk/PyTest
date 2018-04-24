print()
'''
定义一个游乐园门票的类，并尝试计算2个成人+一个小孩的平日票价
平日票价100
周末票价为平日的120%
儿童半票
'''

# class Ticket:
#     price=100
#
#     def calPrice(self):
#         time=int(input('请选择你要去的时间（1周末，2为非周末）：'))
#         adult=int(input('请输入成人人数：'))
#         children=int(input('请输入小孩人数：'))
#         if time==1:
#             self.price=(adult*100+children*100*0.5)*1.2
#         elif time==2:
#             self.price=(adult*100+children*100*0.5)
#         else:
#             print('你的时间选择有误！！')
#         return self.price
#
# ticket=Ticket()
# print(ticket.calPrice())


'参考答案：(面向对象的思维)'

class Ticket:

    def __init__(self,weekend=False,discount=False):
        self.price=100

        if weekend:
            self.cost=1.2
        else:
            self.cost=1

        if discount:
            self.discount=0.5
        else:
            self.discount=1

    def calPrice(self,num):
        total=self.price*self.cost*self.discount*num

        return total

adult=Ticket()
child=Ticket(discount=True)

print('平时2个成人加1个小孩的票价为%d'%(adult.calPrice(2)+child.calPrice(1)))