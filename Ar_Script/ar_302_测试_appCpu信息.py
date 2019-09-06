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
        desired_caps['deviceName'] = 'ZY2249WM66'
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1.1'
        desired_caps['noReset'] = True
        desired_caps["appPackage"] = "com.android.chrome"
        desired_caps["appActivity"] = "com.google.android.apps.chrome.Main"
        self.driver=webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)



    def getCurrentTime(self):
        self.currentTime=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        return self.currentTime

    def getCpuInfo(self):
        cmd='adb shell dumpsys cpuinfo |findstr com.android.chrome'
        self.cpuInfo=os.popen(cmd).read().split('%')[0]
        print(self.cpuInfo)

        return self.cpuInfo

    def startApp(self):
        cmd = 'adb shell am start -W -n com.android.chrome/com.google.android.apps.chrome.Main'
        os.popen(cmd)

    def testOnce(self):
        urlBar=self.driver.find_element_by_id('com.android.chrome:id/url_bar')
        urlBar.send_keys("wwww.baidu.com")
        self.driver.keyevent(66)
        time.sleep(7)
        search=self.driver.find_element_by_id('index-kw')
        search.send_keys("appium")
        clickSearch=self.driver.find_element_by_id('index-bn')
        clickSearch.click()

    def run(self):
        for count in range(self.count):
            self.startApp()
            time.sleep(2)
            self.getCpuInfo()
            self.testOnce()
            time.sleep(2)
            self.getCpuInfo()
            print()
        self.driver.quit()

if __name__ == '__main__':
    cl=Controler(10)
    cl.run()