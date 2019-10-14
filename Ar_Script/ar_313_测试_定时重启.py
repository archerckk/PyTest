import os
import time


result=int(input('请输入重启的时间：'))
while True:
    startTime=time.localtime()
    if startTime[3]==result:
        os.popen('shutdown -r -t 10')
    else:
        continue
