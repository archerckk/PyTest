class Demo:

    def __getattr__(self, item):
        self.item='fishc'
        return self.item

    def __init__(self):
        self.x='a'
    #
    # def __setattr__(self, key, value):
    #     self.x=value
    #     demo.__dict__[self.x]=value


demo=Demo()
print(demo.y)
demo.y='123'
print(demo.y)