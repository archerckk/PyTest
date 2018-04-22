print()
'实现“全部替换功能”'

'''
1.打开需要替换内容的文件
2.输入需要替换的单词或字符
3.输入新的单词或字符
4.统计文件中共有多少个需要替换的单词
    0个的话，提示’没有目标字符‘终止程序
    不为0则，打印对应的数量
5.确认是否替换
    是，内容替换
    否，取消操作
'''

def replace(fileName,old,new):
    f=open('resources/%s'%fileName)
    findStr=''
    toast = ''
    # content=[]
    # count=0

    for i in f:
        findStr+=i

    count=findStr.count(old)

    #参考处理(先将数目统计好，同时把内容替换好存进去一个列表)：
    # for i in f:
    #     if old in i:
    #         count+=i.count(old)
    #         i=i.replace(old,new)
    #     content.append(i)



    if count==0:
        print('目标字符不存在，程序结束')
    else:
        print('文件【%s】中共有%d个【%s】'%(fileName,count,old))
        print('你确定要把所有的【%s】替换为【%s】吗？\n【YES/NO】：'%(old,new),end='')
        while 1:
            chose=input(toast)
            if chose not in ['YES','yes','NO','no']:
                toast='你输入的选择有误！请重新输入：'

            if chose in ['YES','yes']:
                findStr=findStr.replace(old,new)
                f=open('resources/%s'%fileName,'w')
                f.writelines(findStr)
                f.close()
                break
            if chose in ['NO','no']:
                print('取消替换，程序结束')
                f.close()
                break

        #参考处理，这样的话代码输入只有一次输入的机会，其实从脚本的角度来讲，也是可以的，自己总想着体验好一些（职业病）：
        # j = input()
        # if j == 'YES':
        #     f = open('resources/%s' % fileName, 'w')
        #     f.writelines(content)
        #     f.close()
        # else:
        #     f.close()
        #     return None

fileName='replace.txt'
old=input('请输入需要替换的单词或字符：')
new=input('输入新的单词或字符:')
replace(fileName,old,new)