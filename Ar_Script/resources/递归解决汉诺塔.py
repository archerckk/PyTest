def han(n,x,y,z):
    if n==1:
        print(x, '-->', z)
    else:
        han(n-1,x,z,y)#将前n-1个盘子通过z移动到y上面
        print(x,'-->',z)
        han(n-1,y,x,z)

n=int(input('请输入你要输入的层数：'))
han(n,'x','y','z')