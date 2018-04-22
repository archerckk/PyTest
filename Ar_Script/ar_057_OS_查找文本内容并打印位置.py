import os
'''
用户输入关键字，查找当前文件内（包含文件夹的）所有包含关键字的文本文件(.txt后缀)
显示该文件所在的位置及关键字中的具体位置（第几行第几个字符）
'''

'''
1.定义一个变量接收关键字
2.确认是否打印关键字的判断
3.拿到包含关键字的所有txt文档
    遍历所有的文件，拿到TXT后缀的文档
    打开文档查看里面的内容是否包含关键字
    有关键字的txt文档添加到一个列表
4.对有关键字出现的文档找到关键字出现的行数
    用字典来保存行数对应的位置
5.将字典的内容打印出来  
'''


def printResult(resultDict):
    keys=resultDict.keys()
    keys=sorted(keys)

    for i in keys:
        print('关键字出现在第%d行，第%s个位置'%(i,str(resultDict[i])))


def countPostion(lines,target):
    pos=[]
    result = lines.find(target)
    while result!=-1:
        pos.append(result + 1)
        result=lines.find(target, result + 1)
    '程序一直在执行没有结果的时候，一定要检查while循环是否没有出口'
    'result忘记重新赋值了，所以一直它的值没有重新变化'
    return pos


def findContentDict(txt_file,target):
    resultDict={}
    count=0
    f=open(txt_file)

    for lines in f:
        count+=1
        if target in lines:
            pos=countPostion(lines,target)
            resultDict.setdefault(count,pos)

    f.close()
    return resultDict


def findFile(target,choice):
    allFile=os.walk(os.getcwd())
    txt_file_list=[]

    for i in allFile:
        for file in i[2]:
            ext=os.path.splitext(file)
            if ext[1]=='.txt':
                txtFile=i[0]+os.sep+file
                txt_file_list.append(txtFile)

    for i in txt_file_list:
        contentDict=findContentDict(i,target)
        if contentDict:
            print('=' * 80)
            print('在文件【%s】中找到关键字【%s】'%(i,target))
            printResult(contentDict)

target='小甲鱼'
choice='yes'
findFile(target,choice)