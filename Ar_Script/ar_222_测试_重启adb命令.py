import os
from time import sleep
# os.popen('adb kill-server')1
# sleep(2)
# os.popen('adb start-server')
# sleep(2)
a=True
while a:
    b='List of devices attached'
    c=os.popen('adb devices').readlines()
    sleep(1)
    if c[1]!='\n':
        print(os.popen('adb devices').readlines())
        a=False
    else:
        print('List of devices attached')