def getage(n):
    '''有5个人坐在一起，问第五个人多少岁？他说比第四个人大2岁。问第四个人岁数，他说比第三个人大2岁。
    问第三个人，又说比第二个人大2岁。问第二个人，说比第一个人大两岁。最后一个为10岁，请问第五个人多大？
    '''
    if n==1:
        return 10
    else:
        return getage(n-1)+2
print(getage(10))
