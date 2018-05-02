class Countlist(list):
    def __init__(self,*args):
        super().__init__(*args)
        self.count=[]
        for i in args:
            self.count.append(0)

    def __len__(self):
        return len(self.count)

    def __getitem__(self, key):
        self.count[key]+=1
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        self.count[key] += 1
        super().__setitem__(key, value)

    def __delitem__(self, key):
        del self.count[key]
        super().__delitem__(key)

    def counter(self, key):
        return self.count[key]

    def append(self,args):
        self.count.append(0)
        return super().append(args)

    def insert(self, index, object):
        self.count[index]+=1
        return super().insert(index,object)

    def pop(self, index= -1):
        self.count.pop(index)
        return super().pop(index)

    def remove(self, value):
        '数值的层面的计算一直在基类里面，所以这里面拿的位置是super().index'
        key = super().index(value)
        del self.count[key]
        super().remove(value)

    def clear(self):
        self.count.clear()
        super().clear()

    def reverse(self):
        self.count.reverse()
        super().reverse()