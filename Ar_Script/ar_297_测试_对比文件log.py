#encoding=utf-8
import os

with open('./resources/start_choice.txt')as fileLog:
    log=fileLog.read()

xingzuoList=[]
with open(r'./resources/xingzuo.txt')as xingzuo:
    for i in xingzuo:
        i=i.upper().strip('\n').strip()
        xingzuoList.append(i)
xingzuoDict=dict(map(lambda x:(x,0),xingzuoList))

for i in xingzuoDict.keys():
    if i in log:
        xingzuoDict[i]=True
    else:
        xingzuoDict[i]=False

for i in xingzuoDict.items():
    print(i[0],i[1])

# # xingzuoDict={}
# for i in xingzuoList:
#     xingzuo