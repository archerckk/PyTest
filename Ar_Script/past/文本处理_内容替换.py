def replace(file,old_word,new_word):
    f=open(file)
    content=[]
    count=0

    #统计关键字出现的次数，并且将新的内容存放入列表
    for i in f:
        if old_word in i:
            count+=i.count(old_word)
            i=i.replace(old_word,new_word,count)
        content.append(i)

    print('文件%s中共有%d个【%s】'%(file,count,old_word))
    print('你确定要把所有的【%s】替换为【%s】吗？'%(old_word,new_word))
    judge=input('【YES/NO】：')
    f=open(file,'w')
    if judge=='YES':
        f.writelines(content)
        f.close()
    else:
        f.close()
        return None


file=input('请输入文件名：')
old_word=input('请输入需要替换替换的单词或字符：')
new_word=input('请输入新的单词或字符：')

replace(file,old_word,new_word)