import math
'''
定义一个点(Point)类和直线类(Line)类，使用getlen方法可以获得直线的长度
'''

class Point:

    def __init__(self,x,y):
        self.x=x
        self.y=y

class Line:
    def getlen(self,x1,x2,y1,y2):
        '这个特别复杂的写法，以后还是要想办法分割开来，多用变量接收一部分结构，参考下方的做法'
        self.result=math.sqrt(((x1-x2)**2+(y1-y2)**2))


        return self.result

p1=Point(1,1)
p2=Point(1,3)
line=Line()

print(line.getlen(p1.x,p2.x,p1.y,p2.y))

'参考答案'

class Point:

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def getX(self):
        return self.x

    def getY(self):
        return  self.y


class Line:
    '将两个实例对象作为参数传进去直线的初始化方法里面'
    def __init__(self,p1,p2):
        self.x=p1.getX()-p2.getX()
        self.y=p1.getY()-p2.getY()
        self.line=math.sqrt(self.x**2+self.y**2)

    def getLine(self):
        return self.line


p1=Point(1,4)
p2=Point(4,8)
line=Line(p1,p2)
print(line.getLine())