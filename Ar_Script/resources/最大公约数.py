def gcd(x,y):
    while y:
        t=x%y
        x=y
        y=t
    return x
x=int(input('请输入x的值：'))
y=int(input('请输入y的值：'))

print('%d和%d的最大公约数为：%d'%(x,y,gcd(x,y)))