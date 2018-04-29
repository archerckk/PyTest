class Demo:
    count=0
    def __init__(self):
        Demo.count+=1



    def __del__(self):

        Demo.count-=1



d=Demo()
c=Demo()

print(Demo.count)
del c
print(Demo.count)