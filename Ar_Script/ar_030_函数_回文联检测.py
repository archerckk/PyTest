'''
编辑一个函数，判断传入的字符串参数是否为“回文联”
回文联是指顺读和倒读是一样的，如：上海自来水来自海上
'''
def huiwenlian(str1):
    strList=[]
    for i in str1:
        strList.insert(0,i)
    str2=''
    for i in strList:
        str2+=i

    if str1==str2:
        print('是回文联')
    else:
        print('不是回文联')

str1=input('请输入你要检查的内容：')
huiwenlian(str1)