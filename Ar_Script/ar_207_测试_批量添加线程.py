from time import ctime,sleep
import threading

def super_player(func,time):
    for i in range(3):
        print('正在播放%s %s'%(func,ctime()))
        sleep(time)

file_dict={'断点.mp3':3,'蜡笔小新.mp4':2,'你还要我怎么样.mp3':4}
list1=[]

for file,time in file_dict.items():
    t=threading.Thread(target=super_player,args=(file,time))
    list1.append(t)
