from time import ctime,sleep
import threading

def music(arg,time):
    for i in range(time):
        print('我正在听%s %s'%(arg,ctime()))
        sleep(2)

def movie(arg,time):
    for i in range(time):
        print('我正在看%s %s'%(arg,ctime()))
        sleep(5)

threads=[]

t1=threading.Thread(target=music,args=('一千年以后',2))
threads.append(t1)

t2=threading.Thread(target=movie,args=('熊出没',2))
threads.append(t2)

if __name__ == '__main__':

    '启动线程'
    for i in threads:
        i.start()

    '守护线程'
    for i in threads:
        i.join()

    print('all end:%s'%ctime())