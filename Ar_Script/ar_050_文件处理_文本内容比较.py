print()
'''
编写一个程序，比较用户输入的两个文件，如果不同，显示所有不同处行号与第一个不同字符的位置
如：
    两个文件共有【1】处不同：
    第4行不一样
'''

'''
1.首先需要拿输入两个要比较的文件名
2.拿到对应文件的内容
3.比较内容并进行计数
4.打印统计的结果
'''

def compare(file1,file2):
    f1=open('result/%s'%file1)
    f2=open('result/%s'%file2)
    count=0
    differ=[]

    for i in f1:
        count+=1
        if f2.readline()!=i:
            differ.append(count)

    if len(differ)==0:
        print('两个文件完全一样')
    else:
        print('两个文件共有【%d】处不同！'%len(differ))

    for i in differ:
        print('第%d行不一样！！'%i)

file1=input('请输入第1个文件名：')
file2=input('请输入第2个文件名：')
compare(file1,file2)

