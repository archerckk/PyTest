class Xulie:

    def __init__(self,*args):
        self.values=[x for x in args]
        self.countDict={}.fromkeys(range(len(self.values)),0)
        '将一个字典里面的所有键都初始化为0'

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        self.countDict[key]+=1
        return self.values[key]


x=Xulie(1,2,3,5)
print(x[0])
print(x[0])
print(x.countDict[0])

