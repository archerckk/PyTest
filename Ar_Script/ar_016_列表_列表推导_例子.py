#打印0-9数字平方后的数字
a=[x**2 for x in range(10)]
print(a)

#将0-9当中的基数的平方，和偶数的平方组成一个元祖，再将这些元祖放在一个列表当中打印出来
b=[(x,y**2)for x in range(10)for y in range(10)if x%2!=0 if y%2==0]
for i in b:
    print(i)

