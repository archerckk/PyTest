def fei(n):
    n1=1
    n2=1
    n3=2
    if n<-1:
        print('你要计算的位置过小')
    while (n-2)>0:
        n3=n1+n2
        n1=n2
        n2=n3
        n-=1
    return n3

print(fei(12))