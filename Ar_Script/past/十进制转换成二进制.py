def dec_2bin(x):
    result=''
    tmp=[]
    while x:
        t=x//2
        target=x%2
        x=t
        tmp.insert(0,target)

    for i in tmp:
        result+=str(i)
    return result

x=int(input('请输入你要转换的十进制的数字：'))
print('%d转换为二进制的数为：%s'%(x,dec_2bin(x)))