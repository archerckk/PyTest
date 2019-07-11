#encoding=utf-8

"""
1. 已知字符串 a = "aAsmr3idd4bgs7Dlsf9eAF",要求如下
1.1 请将a字符串的大写改为小写，小写改为大写。
1.2 请将a字符串的数字取出，并输出成一个新的字符串。
1.3 请统计a字符串出现的每个字母的出现次数（忽略大小写，a与A是同一个字母），并输出成一个字典。 例 {'a':4,'b':2}
1.4 请去除a字符串多次出现的字母，仅留最先出现的一个。例 'abcabb'，经过去除后，输出 'abc'
1.5 请将a字符串反转并输出。例：'abc'的反转是'cba'
1.6 去除a字符串内的数字后，请将该字符串里的单词重新排序（a-z），并且重新输出一个排序后的字符 串。（保留大小写,a与A的顺序关系为：A在a前面。例：AaBb）
1.7 请判断 'boy'里出现的每一个字母，是否都出现在a字符串里。如果出现，则输出True，否则，则输 出False.
1.8 要求如1.7，此时的单词判断，由'boy'改为四个，分别是 'boy','girl','bird','dirty'，请判断如上这4个字符串里的每个字母，是否都出现在a字符串里。
1.9 输出a字符串出现频率最高的字母
"""
a = "aAsmr3idd4bgs7Dlsf9eAF"
#1.1
print('练习结果展示：')
print(a.swapcase())


#1.2
x=''
for i in a:
    if i.isdigit():
        x+=i

#[i for i in a if i.isdigit()]
print('练习2结果展示')
print(x.join([i for i in a if i.isdigit()]))



#1.3
a=a.lower()
countDict={}
for i in a:
    if i.isalpha()and i not in countDict:
        countDict[i]=1
    elif i.isalpha()and i in countDict:
        countDict[i]+=1
    else:
        continue
print(countDict)

'集合解法'
# dict([(i,a.count(i))for i in set(a))



#1.4
b=a.lower()
print(b)
tmpList=[]
for i in a:
    if i not in tmpList :
        tmpList.append(i)
    else:
        continue

print(''.join(tmpList))
'参考解法'
# b=list(a)
# b=list(set(a))
# b=b.sort(key=list(a).index)
# print(''.join(b))




#1.5
print('练习1.5结果演示')
b=list(reversed(a))
c=''
c=c.join(b)
print(c)
print()

'参考解法'
print(a[::-1])


#1.6 去除a字符串内的数字后，请将该字符串里的单词重新排序（a-z），并且重新输出一个排序后的字符 串。（保留大小写,a与A的顺序关系为：A在a前面。例：AaBb）
a = list("aAsmr3idd4bgs7Dlsf9eAF")
stripNum=a[:]
for i in stripNum:#去除a字符串内的数字
    if i.isdigit():
        stripNum.remove(i)

stripNum.sort()
print('1.6的结果展示为')
print(''.join(stripNum))

"精简版"
b=list("aAsmr3idd4bgs7Dlsf9eAF")
stripNum2=b[:]
stripNum2=[stripNum2.remove(i) for i in stripNum if i.isdigit()]
print(stripNum2)
stripNum2.sort()
print('精简版答案展示')
print(''.join(stripNum2))

"参考解法"
"""
1.要有小写字母从a-z的排序
2.大小写不同，但值不同的字母，大小在小写的前面
3.放两个列表然后对比插入
"""
an="aAsmr3idd4bgs7Dlsf9eAF"
xiao= sorted([i for i in an if i.islower()])
da=sorted([i for i in an if i.isupper()])
for i in da:
    lower_i=i.lower()
    if lower_i in xiao:
        xiao.insert(xiao.index(lower_i),i)
print('参考答案：打印')
print(''.join(xiao))


#1.7 请判断 'boy'里出现的每一个字母，是否都出现在a字符串里。如果出现，则输出True，否则，则输 出False.
resultList=[]
for i in 'girl':
    if i in stripNum:
        resultList.append('True')
    else:
        resultList.append('False')
if 'False' in resultList:
    print('False')
else:
    print('True')

'参考答案'
cc=set(b)
search='b'
cc.update(search)
print(len(cc)==len(set(b)))
"不用遍历可以节省性能"


#1.8 要求如1.7，此时的单词判断，由'boy'改为四个，分别是 'boy','girl','bird','dirty'，请判断如上这4个字符串里的每个字母，是否都出现在a字符串里。
resultList=[]
checkList=['boy','girl','bird','dirty']
print('1.8结果展示')

for i in checkList:
    for j in i:
        if j in stripNum:
            resultList.append('True')
        else:
            resultList.append('False')
    if 'False' in resultList:
        print('False')
    else:
        print('True')
    resultList=[]
'参考答案'
print(len())



#1.9 输出a字符串出现频率最高的字母
max=0
target=[]
for i in countDict.items():
    if i[1]>max:
        max=i[1]

for i in countDict.items():
    if i[1]==max:
        target.append(i[0])

print('1.9结果展示')
print('出现次数最高的的字母为：',end='')
for i in target:
    print(i,end=' ')

"""
2.在python命令行里，输入import this 以后出现的文档，统计该文档中，"be" "is" "than" 的出现次数。
"""

text="""
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

targetDict={'be':0,'is':0,'than':0}
wordList=text.split(' ')

print("\n练习2结果展示")
for i in wordList:
    if i in targetDict.keys():
        targetDict[i]+=1
print(targetDict)


"3.一文件的字节数为 102324123499123，请计算该文件按照kb与mb计算得到的大小。"
targetNum=102324123499123
kbNum=targetNum/1024
mbNum=kbNum/1024
print("\n练习3结果展示")
print(kbNum,mbNum)


"4.已知  a =  [1,2,3,6,8,9,10,14,17],请将该list转换为字符串，例如 '123689101417'."
a = [1, 2, 3, 6, 8, 9, 10, 14, 17]
str1=''
print("\n练习4结果展示")
str1=str1.join([str(x) for x in a])
print(str1)