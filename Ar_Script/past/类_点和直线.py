import math
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

class Line:
    def getlen(self,Point,Point2):
        result=math.sqrt((Point.x-Point2.x)**2+(Point.y-Point2.y)**2)
        return result


pointA=Point(1,0)
pointB=Point(2,0)
line=Line()

print(line.getlen(pointA,pointB))