print()
'阶乘的普通函数算法'
def jiecheng(x):
    result=1
    for i in range(1,x+1):
        result*=i
    return result
print(jiecheng(5))

#递归版本
def test2(n):
    if n==1:
        return 1
    else:
        return n*test2(n-1)

print(test2(5))