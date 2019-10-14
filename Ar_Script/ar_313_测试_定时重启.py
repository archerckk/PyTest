import os
import time

while True:
    startTime=time.localtime()
    if startTime[3]==9:
        os.popen('shutdown -r -t 10')
    else:
        continue
