i=0
target=0
x=0
while i<=100:
    if x % 2 == 1 and x % 3 == 2 and x % 5 == 4 and x % 6 == 5:
        target=1#这试了次写了两个==号……这看半天看不出来
    else:
        x=7*(i+1)
    i+=1
if target==1:
    print("阶梯数为：", x)#不用使用格式化跟强转的一种数字跟字符串组合输出方式
else:
    print('所求的阶梯数不在范围内')



