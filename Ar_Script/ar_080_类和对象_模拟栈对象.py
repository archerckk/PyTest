class Stack:

    def __init__(self):
        self.x=[]


    def isEmpty(self):
        if len(self.x):
            return False
        else:
            return True

    def push(self,factor):
        self.x.insert(0,factor)

    def pop(self,factor):
        self.x.remove(self.x[0])

    def top(self):
        return self.x[0]

    def bottom(self):
        return self.x[len(self.x)-1]

stack=Stack()