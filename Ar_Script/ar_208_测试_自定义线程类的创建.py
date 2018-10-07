from time import ctime,sleep
import threading

class Mythread(threading.Thread):

    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.func=func
        self.args=args
        self.name=name

    def run(self):
        self.func(*self.args)

def super_player(func,times):
    for i in range(3):
        print('正在播放%s %s'%(func,ctime()))
        sleep(times)


threads=[]
file_dict={'断点.mp3':3,'蜡笔小新.mp4':2,'你还要我怎么样.mp3':4}
times=range(len(file_dict))

for file,time in file_dict.items():
    t=Mythread(super_player,(file,time),super_player.__name__)
    threads.append(t)

if __name__ == '__main__':
    for time in times:
        threads[time].start()

    for time in times:
        threads[time].join()

    print('All end :%s'%ctime())


