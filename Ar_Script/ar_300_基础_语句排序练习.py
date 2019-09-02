#例题1 通过字典的值查找对应的key

dict1={"a":"test","b":"test","d":'test',"c":"test3"}

targetStr='test'

keyList=[]

for key,value in dict1.items():
    if value=='test':
        keyList.append(key)

print(keyList)

#例题2 排序字典
keyList2=list(dict1.keys())
keyList2.sort()

# for i in keyList2:
    # print(i,dict1[i])


#练习1
ainfo = {'b':'python','a':'haha','c':'hehe','f':'xiaoming'}

vList=sorted(list(ainfo.values()))
# keyList3=[]
# for i in vList:
#     for key,value in ainfo.items():
#         if i==value:
#             keyList3.append(key)
#
# for i in range(len(vList)):
#     print(keyList3[i],vList[i])

ainfo=sorted(ainfo,key=list(ainfo.values()).sort())
print(ainfo)
