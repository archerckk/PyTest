class Demo:

    def __init__(self):
        self.judge=True
        self.count=0
        # if self.__init__():
        #     self.count+=1


    def __del__(self):

        self.count-=1



d=Demo()
c=Demo()

print(c.count)