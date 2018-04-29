class Demo:

    def __init__(self,name):
        self.name=name

    def __call__(self, friend):
        print('我的名字叫：%s'%self.name)
        print('我朋友的名字叫：%s'%friend)

demo=Demo('路飞')
demo('索隆')


class Fac:

    def __init__(self):
        self.num=0

    def __call__(self,num):
        n1=1
        n2=1
        n3=1
        result=[]
        if num<1:
            print('不在计算范围')

        # while (num-2)>0:
        #     n3 = n1 + n2
        #     n1= n2
        #     n2 = n3
        #     self.num = n3
        #     result.append(n3)
        #     num-=1
        # self.num=n3

        for i in range(num):
            result.append(n1)
            n1,n2=n2,n1+n2

        self.num=result[-1]
        print(result)
        return self.num

fac=Fac()
print(fac(12))

