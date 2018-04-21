class Nstr(str):
    def __sub__(self, other):
        return self.replace(other, '')


a=Nstr('abc')
b=Nstr('ab')
print(a-b)
