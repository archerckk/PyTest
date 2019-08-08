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

for i in keyList2:
    print(i,dict1[i])