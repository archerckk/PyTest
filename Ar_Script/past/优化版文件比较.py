import easygui

def compare_differ(file1,file2):
    differ=[]
    count=0
    with open(file1)as f1,open(file2)as f2:
        for f1_line in f1:
              f2_line=f2.readline()
              count+=1
              if f1_line!=f2_line:
                  differ.append(count)
    return differ


file1=input('请输入你要比较的第一个文件名：')
file2=input('请输入你要比较的第二个文件名：')

differ=compare_differ(file1,file2)

if len(differ)==0:
    print('两个文件完全一样！')
else:
    for i in differ:
        print('第%d行不一样'%i)


