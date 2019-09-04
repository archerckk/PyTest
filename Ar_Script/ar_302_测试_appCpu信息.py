import os
import time
import openpyxl
from appium import webdriver

"""
1、启动app
2、获取app的cup运行信息文本
3、分析文本获取的cpu的占比
4、持续操作app，记录app的cpu使用情况
5、保存到excel文件里面
"""


class Controler(object):

    def __init__(self,count):
        self.cpuInfo=0
        self.currentTime=0
        self.count=count
        desired_caps = {}
        desired_caps['automationName'] = 'Appium'
        desired_caps['deviceName'] = '98891936513437444f'
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '8.0'
        desired_caps['noReset'] = True
        desired_caps["appPackage"] = "com.cnblogs.xamarinandroid"
        desired_caps["appActivity"] = "md522127645c21675e531a6ac609ef72b2a.SplashScreenActivity"
        self.driver=webdriver.



    def getCurrentTime(self):
        self.currentTime=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        return self.currentTime

    def getCpuInfo(self):
        cmd='adb shell dumpsys cpuinfo |findstr com.android.chrome'
        self.cpuInfo=os.popen(cmd).read().split('%')[0].split('+')[1]
        print(self.cpuInfo)
        return self.cpuInfo

    def startApp(self):
        cmd = 'adb shell am start -W -n com.android.chrome/com.google.android.apps.chrome.Main'
        os.popen(cmd)

    def testOnce(self):

if __name__ == '__main__':
    cl=Controler(1)
    cl.startApp()
    cl.getCpuInfo()
    cl.getCurrentTime()