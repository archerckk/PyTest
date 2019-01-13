print()
'''
属性：长和宽
方法：1.设置长和宽 2.计算并且打印面积

'''

class Juxing:
    length=5
    weight=4

    def getOption(self):
        print('这个矩形的长是%.2f，宽是%.2f'%(self.length,self.weight))

    def setOption(self):
        print('请输入矩形的长和宽……')
        self.length=float(input('长：'))
        self.weight=float(input('宽：'))

    def getArea(self):
        return  (self.length*self.weight)

# juxing=Juxing()
# juxing.getOption()
# juxing.setOption()
# print(juxing.getArea())