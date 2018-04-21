import os
'''
1.遍历一个目录下面的文件
2.将视频文件的文件名拿出来
3.统计数量
4.写入到一个txt文档
5.总数量，还有总大小放在最后面展示
'''

def find_video(fileName,target):
    os.chdir(fileName)
    allFile=os.walk(os.getcwd())
    videoList=[]
    videoDict={}
    sumSize = 0
    for i in  allFile:
        for each_file in i[2]:
            if os.path.splitext(each_file)[1] in target:
                each_file=os.path.join(i[0],each_file)
                fileSize=int(os.path.getsize(each_file)/1024**2)#将文件大小byte转换成m
                videoDict.setdefault(each_file,'【%sM】'%fileSize)
                sumSize+=fileSize
    return (videoDict,sumSize)

    # for i in videoList:
    #     print(i)

fileList=['F:\system.dll','I:\system.dll','H:\动漫\system.dll']
# fileName=input('请输入与你要查找的路径：')
workFile=os.getcwd()
target=['.mp4','.avi','.wmv','.rm','.rmvb','.mpg']
sumSize=0
tmp_list=[]
total=0
for i in fileList:

    sumSize = int(find_video(i, target)[1] / 1024)
    tmp_list.append(sumSize)
    videoDict = find_video(i, target)[0]
    with open(workFile+os.sep+'abc_%s.txt'%i[0],'w',encoding='utf-8')as f:
        for i in videoDict:
            f.write(i+videoDict[i]+'\n')
        f.write('\n\n文件的总数为：%d个,总大小为：%sGB'%(len(videoDict),sumSize))

for i in tmp_list:
    total+=i
print('目录列表之中一共有%sGB的视频文件'%total)