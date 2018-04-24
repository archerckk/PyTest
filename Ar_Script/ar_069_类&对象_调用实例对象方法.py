print()
'''
属性：姓名（默认姓名为’小甲鱼‘）
方法：打印姓名
方法中对属性的引用形式需要加上self.如：self.name
'''

class Person:
    name='小甲鱼'

    def printName(self):
        print('我的名字叫：%s'%self.name)

person=Person()
person.printName()