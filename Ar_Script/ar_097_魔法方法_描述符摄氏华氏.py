class Cel:

    def __init__(self,value=26.0):
        self.value=float(value)

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value=value

class Hua:

    def __get__(self, instance, owner):
        return  instance.cel*1.8+32

    def __set__(self, instance, value):
       instance.cel=(value-32)/1.8

class Tempiture:
    cel=Cel()
    hua=Hua()

temp=Tempiture()
print(temp.hua)
temp.hua=100
print(temp.hua)