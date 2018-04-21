def compare(file1,file2):
    file_content1=open(file1)
    file_content2=open(file2)
    count=0
    differ = []
    for i in file_content1:
        j=file_content2.readline()
        count+=1

        if i!=j:
            differ.append(count)

    file_content1.close()
    file_content2.close()
    return differ


file1=input('请输入文件1：')
file2=input('请输入文件2：')
differ=compare(file1,file2)

length=len(differ)
if length==0:
    print('两个文件完全一样')
else:
    for i in differ:
        print('第%d行不一样'%i)