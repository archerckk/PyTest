'''定义一个类，当实例化该类的时候，自动判断传入了多少个参数，并显示出来：'''

class CountArg:

    def __init__(self,*args):
        length=len(args)
        if length==0:
            print('没传入参数')
        else:
            print('一共传入了%d个参数,它们分别是：'%length,end='')
            for i in args:
               print(i,end=',')

d=CountArg()
c=CountArg(1,2,3)