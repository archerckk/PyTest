#encoding=UTF-8
class Count:

    def __init__(self,func):
        self.func=func
        self.callNum=0

    def __call__(self, *args, **kwargs):
        self.callNum+=1
        print("函数被调用了{}次".format(self.callNum))
        return self.func(*args,**kwargs)

@Count
def call():
    print('Hello World')

call()
call()
call()