#encoding=utf-8



"1.该文本里，有多少个用户。（要求：输出为一个整数。）"
txtFile=open('resources/twitter数据挖掘片段.txt',encoding='utf-8')
numList=[]
nameList=[]
for i in txtFile.readlines():
    try:
        splitList=i.split(',')
        # print(splitList)
        for i in splitList[0]:
            if i.strip('"').isdigit() :
                numList.append(i)

    except UnicodeEncodeError:
        pass

totalNum=len(numList)
print(totalNum)

"2.该文本里，每一个用户的名字。 （要求：输出为一个list。）"
txtFile2=open('resources/twitter数据挖掘片段.txt',encoding='utf-8')

for i in txtFile2.readlines():
    try:
        splitList=i.split(',')
        # print(splitList)
        for i in splitList[2]:
                nameList.append(i)

    except UnicodeEncodeError:
        pass
print(nameList)