import subprocess
import threading
import time


def test1():
    handle = subprocess.Popen("adb shell  logcat |findstr nad >log.txt " , shell=True)
    time.sleep(15)
    subprocess.Popen("taskkill /F /T /PID %s"% str(handle.pid) , shell=True)
    print('test1执行完成')


def test2():
    handle = subprocess.Popen("adb shell  logcat |findstr Stat >log2.txt " , shell=True)
    time.sleep(15)
    subprocess.Popen("taskkill /F /T /PID %s"% str(handle.pid) , shell=True)
    print('test2执行完成')

threads=[]

t1=threading.Thread(target=test1)
t2=threading.Thread(target=test2)

threads.append(t1)
threads.append(t2)

for t in threads:
    t.start()

for t in threads:
    t.join()

