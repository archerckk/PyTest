import  os
'统计当前目录下每个文件类型的文件数，打印文件类型对应的：文件个数'

'''
1.拿到当前的目录的所有文件名称（包括文件夹）
2.判断上述列表里面的文件是否为文件夹
    文件夹则【文件夹类型】+1
    其他则对应的文件类型+1
3.打印对应的类型的数量结果
'''

def countFileType(filePath):
    fileList=os.listdir(filePath)
    resultDict={}

    '自己昨晚想到的解决思路是先初始化，然后再+=赋值'
    # for i in fileList:
    #     if os.path.isdir(i):
    #         resultDict['文件夹']=0
    #     else:
    #         resultDict[os.path.splitext(i)[1]]=0

    '自己将setdefault 跟 复制等同了，其实键本身有值的话，它是不会重新赋值的'
    for i in fileList:
        if os.path.isdir(i):
            # resultDict[]
            resultDict.setdefault('文件夹',0)
            resultDict['文件夹']+=1
        else:
            '对于要多次使用的调用结果，用一个变量接收会省去很多重复代码'
            # ext = os.path.splitext(i)[1]
            resultDict.setdefault(os.path.splitext(i)[1],0)
            resultDict[os.path.splitext(i)[1]]+=1

    for i in resultDict.keys():
        print('该文件夹下共有类型为【%s】%d个'%(i,resultDict[i]))

countFileType(os.curdir+os.sep+'past')