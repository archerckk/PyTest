import os
import re
import time
import csv
import openpyxl
from openpyxl.styles import numbers
import subprocess
import easygui as g


def get_activity_name():
    msg = '请选择你要检查的apk安装包'
    title = '文件选择'
    default = "*.apk"
    add_time = "_{}".format(time.localtime()[5])

    filePath = g.fileopenbox(msg=msg, title=title, default=default)

    fileNewName = filePath.split('.apk')[0].strip() + add_time + '.apk'
    os.rename(filePath, fileNewName)

    print('选择的apk路径为：', fileNewName)

    command = 'aapt dumpsys badging "%s" ' % fileNewName

    handle = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    time.sleep(2)

    reg_packageName = re.compile(r"package: name='(.+?)'")
    reg_launchableActivity = re.compile(r"launchable-activity: name='(.+?)'")

    log = str(handle.stdout.read())
    position = log.index('targetSdkVersion:')

    print('\n', log[0:position + 21], '\n')  # 截取到targetSDK Version部分包信息

    try:
        packageName = reg_packageName.search(log).group(1)
        lanuchableActivity = reg_launchableActivity.search(log).group(1).strip()
        print('选择的apk包名为：', packageName)
        print('选择的apk登录名为：', packageName+'/'+lanuchableActivity)
        return fileNewName, packageName, lanuchableActivity
    except Exception as err:
        print(err)


# app启动
class App(object):

    def __init__(self):
        self.content = ''
        self.runtime = 0
        self.beforeStart = 0
        self.afterStart = 0
        self.info=get_activity_name()

    def startApp(self):
        cmd = 'adb shell am start -W -n {}'.format(self.info[1]+"/"+self.info[2])
        self.content = os.popen(cmd).readlines()
        return self.content

    def stopApp(self):
        cmd = 'adb shell am force-stop {}'.format(self.info[1])
        os.popen(cmd)

    def backApp(self):
        cmd = 'adb shell input keyevent 3'
        os.popen(cmd)

    def beforeAppStart(self):
        self.beforeStart = time.perf_counter()
        print(self.beforeStart)
        return self.beforeStart

    def afterAppStart(self):
        self.afterStart = time.perf_counter()
        print(self.afterStart)
        return self.afterStart

    def getTime(self):
        for line in self.content:
            if "ThisTime" in line:
                self.runtime = line.split(':')[1].strip()
                break
        return self.runtime


class Control(object):

    def __init__(self, count):
        self.app = App()
        self.count = count
        self.allData = [('runTime', 'calTime', 'currentTime')]

    def testOnce(self):
        before = self.app.beforeAppStart()
        self.app.startApp()
        after = self.app.afterAppStart()
        result = after - before
        time.sleep(5)
        runtime = self.app.getTime()
        # self.app.stopApp()
        self.app.backApp()
        currentTime = self.getCurrntTime()
        self.allData.append((runtime, result, currentTime))
        time.sleep(3)

    def run(self):
        for i in range(self.count):
            self.testOnce()

    def getCurrntTime(self):
        currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return currentTime

    def saveData(self):
        csvFile=open('testData.csv','w',newline='')
        writer=csv.writer(csvFile)
        writer.writerows(self.allData)
        csvFile.close()

        # wb = openpyxl.Workbook()
        # ws = wb.active
        # for i in range(1, self.count + 1):
        #     # 设置单元格的格式为数字，去掉单元格的前后空格
        #     ws['A{}'.format(i)].number_format = numbers.FORMAT_NUMBER
        #     ws['B{}'.format(i)].number_format = numbers.FORMAT_NUMBER
        #     ws['A{}'.format(i)] = self.allData[i - 1][0].strip()
        #     ws['B{}'.format(i)] = self.allData[i - 1][1]
        #     ws['c{}'.format(i)] = self.allData[i - 1][2].strip()
        # wb.save('testData.xlsx')


if __name__ == '__main__':
    control = Control(5)
    control.run()
    control.saveData()
