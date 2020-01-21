import csv,json,time,os,subprocess
from appium import webdriver


"""
1、先启动app
2、执行top -d 输出到文件，启动测试指定流程
3、关闭os对象
4、分析输出内容
5、将数据写入到csv文件
"""

class Control(object):

    def __init__(self):
        self.result=[("测试时间","VSS(Kb)","RSS(Kb)")]
        self.file_time=time.strftime('%Y_%m_%d_%H_%M_%S',time.localtime())
        with open('resources/phone.json','r')as f:
            self.desired=json.load(f)
        self.top_file=r'G:\Pycharm_Project\Pytest\Ar_Script\resources\top_file.txt'
        self.driver=webdriver.Remote('http://localhost:4723/wd/hub',self.desired['mate8'])

    def startApp(self):
        cmd = 'adb shell am start -W -n com.android.chrome/com.google.android.apps.chrome.Main'
        os.popen(cmd)

    def test_operate(self):
        self.driver.get('http://www.baidu.com')
        tmp_list=['selenium','appium','python','test home','51test']
        # tmp_list = ['selenium', 'appium']
        for i in tmp_list:
            self.driver.find_element_by_id('index-kw').send_keys(i)
            self.driver.find_element_by_id('index-bn').click()
            self.driver.implicitly_wait(5)
            self.driver.back()
            self.driver.implicitly_wait(5)
        self.driver.quit()

    def get_data(self):
        self.startApp()
        cmd='adb shell top -d 5 >"{}"'.format(self.top_file)
        handle=subprocess.Popen(cmd,shell=True)
        self.test_operate()
        subprocess.Popen("taskkill /F /T /PID {}".format(handle.pid))

    def getCurrentTime(self):
        self.currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return self.currentTime

    def analyze(self):
        self.get_data()
        with open(self.top_file,'r')as f:
            content=f.readlines()

        for line in content:
            if 'com.android.chrome\n' in line:
                line='#'.join(line.split())
                VSS=line.split('#')[7].strip('K')
                RSS=line.split('#')[8].strip('K')
                cur_time=self.getCurrentTime()
                self.result.append((cur_time,VSS,RSS))

    def save_data(self):
        csvData = open("meminfo.csv", 'w', newline='')
        writer = csv.writer(csvData)
        writer.writerows(self.result)
        csvData.close()

cl=Control()
cl.analyze()
cl.save_data()