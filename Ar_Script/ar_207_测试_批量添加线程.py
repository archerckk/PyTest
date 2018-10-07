from time import ctime,sleep
import threading

def super_player(func,time):
    for i in range(3):
        print('正在播放%s %s'%(func,ctime()))
        sleep(time)

file_dict={'断点.mp3':3,'蜡笔小新.mp4':2,'你还要我怎么样.mp3':4}
threads=[]

times=range(len(file_dict))

'将两个参数的值分别从一个字典的键跟值里面拿出来再传参'
for file,time in file_dict.items():
    t=threading.Thread(target=super_player,args=(file,time))
    threads.append(t)

if __name__ == '__main__':
    '定义了函数，可以通过线程来启动，不用专门的调用'
    for time in times:
        threads[time].start()

    for time in times:
        threads[time].join()

    print('All end：%s'%(ctime()))

