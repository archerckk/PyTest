#encoding=utf-8
import os

'''
1.遍历一个目录下面的文件
2.将视频文件的文件名拿出来
3.统计数量
4.写入到一个txt文档
5.总数量，还有总大小放在最后面展示
'''

def countNumSize(filePath,target):
    os.chdir(filePath)
    allFile=os.walk(os.getcwd())
    target_file_list=[]
    sizeDict={}
    count=0
    sumSize=0

    for i in allFile:
        for each_file in i[2]:
            ext=os.path.splitext(each_file)
            if ext[1] in target:
                each_file=os.path.join(i[0],each_file)
                target_file_list.append(each_file)

    for i in target_file_list:
        size=os.path.getsize(i)
        sumSize+=size
        sizeDict[i]="【%dBytes】"%size
        # print(i)

    for i in sizeDict.items():
        count+=1
        f.write(i[0]+i[1]+os.linesep)
    f.write('\n总共有目标类型文件%d个，总共大小为：【%d KB】'%(count,sumSize/1028))
    f.close()


scriptPath=os.getcwd()+os.sep+'result'+os.sep+'typeList.txt'
f=open(scriptPath,'w')

os.chdir('../')
filePath=os.getcwd()
target=['.py']
countNumSize(filePath,target)