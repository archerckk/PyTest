'''
栈的话是后进先出
'''

class Stack:

    def __init__(self,start=[]):
        self.x=[]
        for i in start:
            self.push(i)
        '很巧妙的将传进来的参数放入到x列表里面了'

    def isEmpty(self):
        if len(self.x):
            return False
        else:
            return True

    '后进先出应该是用append'
    def push(self,factor):
       self.x.append(factor)
        # self.x.insert(0,factor)

    ' 后进先出，所以还是删最后一个，self.x.remove(self.x[0])'
    def pop(self,factor):
        self.x.pop()

        '对于删除，查询要主要对为空的情况进行判断和处理'
        # if not self.stack:
        #     print('警告：栈为空！')
        # else:
        #     return self.stack.pop()


    '可以用-1来表示列表的最后一个元素，不用len（obj）-1'
    def top(self):
        return self.x[-1]

    def bottom(self):
        return self.x[0]

stack=Stack(start=[123,456])
print(stack.isEmpty())


