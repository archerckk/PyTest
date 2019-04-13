import timeit
import os
import time
from appium import webdriver

driver=webdriver()
print(time.ctime())
os.popen('adb shell am start com.in.camera.android/com.in.camera.android.main.HomeActivity ')
driver.im
print(time.ctime())