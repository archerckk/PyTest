import time
import ar_075_类和对象_乌龟与鱼群 as g
# def timeslong(func):
#     def call():
#         start = time.clock()
#         print("It's time starting ! ")
#         func()
#         print("It's time ending ! ")
#         end = time.clock()
#         return "It's used : %s ." % (end - start)
#
#     return call
#
# @timeslong
# def f():
#     y = 0
#     for i in range(10):
#         y = y + i + 1
#         print(y)
#     return y

# print(f())



class timeslong:
    count=0
    def __init__(self,func):
        self.f = func
        timeslong.count+=1
    def __call__(self):
        start = time.perf_counter()
        print("It's time starting ! ")
        self.f()
        print("It's time ending ! ")
        end = time.perf_counter()
        return "It's used : %s ." % (end - start)

@timeslong
def f():
    tmp=input()
    # y = 0
    # for i in range(10):
    #     y = y + i + 1
    #     print(y)
    # return y
    # g.game.gameStart()

print(f())
# print(timeslong.count)
