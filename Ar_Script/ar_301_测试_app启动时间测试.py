import os
import time
import csv
import openpyxl

#app启动
class App(object):

    def __init__(self):
        self.content=''
        self.runtime=0

    def startApp(self):
        cmd='adb shell am start -W -n com.android.chrome/com.google.android.apps.chrome.Main'
        self.content=os.popen(cmd).readlines()
        return self.content

    def stopApp(self):
        cmd='adb shell am force-stop com.android.chrome'
        os.popen(cmd)

    def backApp(self):
        cmd='adb shell input keyevent 3'
        os.popen(cmd)

    def getTime(self):
        for line in self.content:
            if "ThisTime" in line:
                self.runtime=line.split(':')[1]
                break
        return self.runtime


class Control(object):

    def __init__(self,count):
        self.app=App()
        self.count=count
        self.allData=['runTime']

    def testOnce(self):
        self.app.startApp()
        time.sleep(5)
        runtime = self.app.getTime()
        # self.app.stopApp()
        self.app.backApp()
        currentTime=self.getCurrntTime()
        self.allData.append(runtime)
        time.sleep(3)

    def run(self):
        for i in range(self.count):
            self.testOnce()

    def getCurrntTime(self):
        currentTime=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        return currentTime

    def saveData(self):
        # csvFile=open('testData.csv','w')
        # writer=csv.writer(csvFile)
        # writer.writerows(self.allData)
        # csvFile.close()

        wb=openpyxl.Workbook()
        ws=wb.active
        ws.append(self.allData)
        wb.save('testData.xlsx')



if __name__ == '__main__':
    control=Control(11)
    control.run()
    control.saveData()