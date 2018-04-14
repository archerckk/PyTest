'''
爱因斯坦曾经提出过这样一道有趣的数学题：有一个长阶梯，若每步上2阶，最后剩下1阶；
若每步上3阶，最后剩2阶；若每步上5阶，最后剩下4阶；若每步上6阶，
最后剩5阶；只有每步上7阶，最后刚好一阶也不剩。请问该阶梯至少有多少阶
'''

#第三次写
step=0
target=0
for i in range(1,100):
    if step%2==1 and step%3==2 and step%5==4 and step%6==5 :
        target=1
    else:
        step=7*i

if target:
    print("阶梯数为：", step)
else:
    print('在该范围查找不到')

#参考答案
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