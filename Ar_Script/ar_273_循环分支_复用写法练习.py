'''
处理一个列表，将基数和偶数分辨出来
并且存储到一个字典
再打印出来
'''
numberList=[1,2,3,4,5,6,7,8,9]
typeStr=['偶数','基数']
numberNew=[dict(zip(numberList,list('偶数')))if i%2==0 else  dict(zip(numberList,list('基数')))for i in numberList]
print(numberNew)

'if条件语句符合写法例子'
numberNew2=[i**2 for i in numberList if i%2==0 ]

'if条件语句 else复合写法例子'
numberNew3=[i**2 if i%2==0 else i-1  for i in numberList ]
dict1={}
''
dictList=map(lambda i:str(i)+':'+'偶数' if i%2==0 else str(i)+':'+'基数' ,numberList)
dictList2=map(lambda i:dict1.update(dict1[i],'偶数') if i%2==0 else dict1.setdefault(str(i),'基数') ,numberList)

'enumerate转变字典用法'
result=dict(enumerate(typeStr))
for i in dictList:
    print(i)


# print(dict1)