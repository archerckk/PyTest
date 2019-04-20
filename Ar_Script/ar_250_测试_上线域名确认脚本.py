import re
import requests
import os
import time
import threading
import signal
import  subprocess
import sys



handle = subprocess.Popen("adb shell  logcat |findstr nad >log.txt " , shell=True)
time.sleep(12)
subprocess.Popen("taskkill /F /T /PID " + str(handle.pid) , shell=True)


print('测试成功')



