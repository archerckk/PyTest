#汉诺塔游戏的解法

def han(n,x,y,z):
    if n==1:
        print(x,'-->',z)
    else:
        han(n-1,x,z,y)
        '将前n-1个盘子借助z从x移动到y上'
        print(x,'-->',z)
        '将最底下一个盘子从x，移动到z上'
        han(n-1,y,x,z)
        '将y上的n-1个盘子借助x移动到z上'

han(3,'x','y','z')