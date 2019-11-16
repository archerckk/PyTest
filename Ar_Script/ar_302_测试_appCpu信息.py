import os
import time
import openpyxl
from appium import webdriver
import csv
import json

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
        #打开手机的配置的json文件
        with open('./resources/motog5.json','r')as f:
            desired_caps = json.load(f)

        self.driver=webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.test_result=[('cpu占用比率','测试时间')]


    def test_operate(self):
        self.driver.get('http://www.baidu.com')
        # tmp_list=['selenium','appium','python','test home','51test']
        tmp_list=['selenium','appium']
        for i in tmp_list:
            self.driver.find_element_by_id('index-kw').send_keys(i)
            self.driver.find_element_by_id('index-bn').click()
            self.driver.implicitly_wait(5)
            self.driver.back()
            self.driver.implicitly_wait(5)


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
        self.startApp()
        time.sleep(2)
        first_result=self.getCpuInfo()
        current_time = self.getCurrentTime()
        self.test_result.append((first_result,current_time))
        self.test_operate()
        time.sleep(2)

        after_result=self.getCpuInfo()
        current_time2=self.getCurrentTime()
        self.test_result.append((after_result,current_time2))
        print()

    def run(self):
        for count in range(self.count):
            self.testOnce()
        self.driver.quit()
        print('执行完成')

    def saveData(self):
        csvData=open("csvData.csv",'w',newline='')
        writer=csv.writer(csvData)
        writer.writerows(self.test_result)
        csvData.close()

if __name__ == '__main__':
    cl=Controler(5)
    # cl.test_operate()
    cl.run()
    cl.saveData()