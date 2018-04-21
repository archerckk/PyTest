def fei(n):
    if n<1:
        return '你输入的位数过小'
    if n==1 or n==2:
        return 1
    if n-2>0:
        n3=fei(n-1)+fei(n-2)
        return n3

print(fei(20))
