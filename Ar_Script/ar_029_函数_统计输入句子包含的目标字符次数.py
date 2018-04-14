'''
编写一个findstr()函数，首先你输入字符串1，然后输入字符串2，统计字符串2在字符串1中
出现的次数
'''

def findStr(str1,str2):
    result=str1.count(str2)
    if result==0:
        print('你所查找的内容并不在目标内容里！')
    else:
        print('查找内容在目标内容中出现了%d次'%result)

str1=input('请输入目标内容：')
str2=input('请输入你要查找的内容：')
findStr(str1,str2)