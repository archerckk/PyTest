import pickle

def save_file(boy,girl,count):
    boy_file=open('boy%s.pkl'%count,'wb')
    girl_file=open('girl%s.pkl'%count,'wb')
    pickle._dump(boy,boy_file)
    pickle._dump(girl,girl_file)
    boy_file.close()
    girl_file.close()


def split_file():
    f=open('record.txt')
    boy=[]
    girl=[]
    count=1

    for i in f:
        if i[:6]!='======':
            (start,end)=i.split(':',1)
            if start=='小甲鱼':
                boy.append(end)
            if start=='小客服':
                girl.append(end)
        else:

            save_file(boy,girl,count)
            boy=[]
            girl=[]
            count += 1
    save_file(boy,girl,count)
    f.close()

def get_data(file):
    pick_f=open(file,'rb')
    content=pickle.load(pick_f)
    for i in content:
        print(i)


split_file()
get_data('boy3.pkl')