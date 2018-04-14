def findStr(x,y):
    if  y not in x:
        print('你锁查找的内容并不在目标字符串当中')

    else:
        times=x.count(y)
        print('你所查找的字符在目标字符串当中出现了%d次' % times)

x=input('请输入目标字符串：')
y=input('请输入需要查找的字符串:')
findStr(x,y)
