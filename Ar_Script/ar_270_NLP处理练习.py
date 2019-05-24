import re

"""
1、读取文件
2、去掉所有的标点符号和换行符，并把所有大写变成小写；
3、合并相同的词，统计每个词出现的频率，并按照词频从大到小排序；
4、将结果安航输出到文件out.txt
"""

def parser(text):
    '去掉所有的换行符和标点符号'
    text=re.sub(r'[^\w ]','',text)

    '将所有大写变成小写'
    text=text.lower()

    '将字符串用空格分隔开来'
    text=text.split(' ')

    '过滤掉那些空字符串'
    text=filter(None,text)

    '统计字符串频次'
    dict_org={}
    for word in text:
        if word not in dict_org:
            dict_org[word]=0
        dict_org[word]+=1

    '排序字典的频次顺序'
    dictNew=sorted(dict_org.items(),key=lambda x:x[1],reverse=True)

    return dictNew

tmpList=[]
# with open('resources/testNLP')as f:
#     text=f.read()

with open('resources/testNLP')as f:
    for i in f:
        print(i)
        tmpList.append(str(i))
text=''.join(tmpList)
dictFinal=parser(text)
# print(dictFinal)

for word,freq in dictFinal:
    print('{} {} \n'.format(word,freq))