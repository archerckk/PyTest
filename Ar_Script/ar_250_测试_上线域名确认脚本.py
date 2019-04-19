import re
import requests
import os
import time
import signal
import  subprocess

def get_info():
        command='adb shell logcat |findstr nad >log.txt'
        os.system(command)
        time.sleep(3)



# result=subprocess.Popen(command,shell=True,stdout=subprocess.PIPE).stdout
# print(result.read())

result=get_info()
# signal.signal(signal.SIGTERM, get_info())
print('测试成功')
# time.sleep(15)



# signal.signal(signal.SIGINT,get_info())
print(result)
# print(result)