'''
如果一个3位数等于其各位数字的立方和，则称这个数为水仙花数。
例如153=1^3+5^3+3^3，因此153是一个水仙花数。
编写一个程序找出100到999以内所有的水仙花数
'''

def shuixianhua():
    for i in range(100,1000):
        bai=i//100
        shi=i%100//10
        ge=i%100%10
        if i==bai**3+shi**3+ge**3:
            print(i,end=' ')

shuixianhua()

