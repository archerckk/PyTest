def shuixianhua():
    print('100到1000以内的水仙花数为：',end='')
    for i in range(100,1000):
        a=i//100
        b=i%100//10
        c=i%100%10
        sum=a**3+b**3+c**3
        if sum==i:
            print(i,' ',end='')
        else:
            pass

shuixianhua()