# def sava_file(boy,girl,count):
#     boy_file=open('boy%d.txt'%count,'w')
#     girl_file=open('girl%d.txt'%count,'w')
#
#     boy_file.writelines(boy)
#     girl_file.writelines(girl)
#
#     boy_file.close()
#     girl_file.close()
#
# def split_file():
#     f=open(r'/home/chenzhibin/PycharmProjects/test/jiayu/record.txt')
#     boy=[]
#     girl=[]
#     count=1
#     for i in f:
#
#         if i[:6]!='======':
#             (person, content) = i.split(':',1)
#             if person=='小甲鱼':
#                 boy.append(content)
#             if person=='小客服':
#                 girl.append(content)
#         else:
#             sava_file(boy,girl,count)
#             boy=[]
#             girl=[]
#             count+=1
#
#     sava_file(boy,girl,count)
#     f.close()
#
# split_file()






#复习

def save_file(boy,girl,count):
    f1=open('boy%d.txt'%count,'w')
    f2=open('girl%d.txt'%count,'w')


    f1.writelines(boy,)
    f2.writelines(girl)

    f1.close()
    f2.close()

def spliteFile():
    f=open('record.txt',encoding='utf-8')
    boy=[]
    girl=[]
    count=1

    for each_line in f:
        if each_line[:6]!='======':
            (start,end)=each_line.split(':',1)
            if start=='小甲鱼':
                boy.append(each_line)
            elif start=='小客服':
                girl.append(each_line)
        else:
            save_file(boy,girl,count)
            count+=1
            boy=[]
            girl=[]

    save_file(boy,girl,count)
    f.close()

spliteFile()