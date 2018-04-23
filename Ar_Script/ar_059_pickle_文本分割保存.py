import pickle
'''
1.打开目标文档，对面目标文档的内容进行分割
2.分割线上之上的小甲鱼跟小客服开头的分开保存到一个文档，并且文件名跟着编号
3.保存为.txt(以pickle的方式保存)
'''

'获取pkl文件内容的方法'
def get_data(file):
    f=open(file,'rb')
    pkList=pickle.load(f)
    for i in pkList:
        print(i)
    f.close()

'保存pkl文件并且编号的方法'
def sava_file(boy,girl,count):
    f1=open('result/boy%d.pkl'%count,'wb')
    f2=open('result/girl%d.pkl'%count,'wb')
    pickle.dump(boy,f1)
    pickle.dump(girl,f2)
    f1.close()
    f2.close()

'对内容进行分割的方法'
def split_file(file):
    boy=[]
    girl=[]
    count=1
    f=open(file)
    for i in f:
        if i[:6]!='='*6:
            (begin,end)=i.split(':',1)
            if begin=='小甲鱼':
                boy.append(i)
            if begin=='小客服':
                girl.append(i)
        else:
            sava_file(boy,girl,count)
            boy=[]
            girl=[]
            count+=1
    sava_file(boy,girl,count)
    f.close()



file='resources/record.txt'
split_file(file)

targetFile='result/boy3.pkl'
get_data(targetFile)