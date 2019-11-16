import csv,os,time,json
from appium import webdriver

class Control(object):

    def __init__(self,count):
        self.count=count
        self.curent_time=0
        self.flow=0
        self.pid=0
        self.result=[('流量数值(MB)','测试时间')]

        with open('resources/motog5.json','r')as f:
            desired_caps= json.load(f)

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def startApp(self):
        cmd = 'adb shell am start -W -n com.android.chrome/com.google.android.apps.chrome.Main'
        os.popen(cmd)


    def get_pid(self):
        cmd='adb shell ps |findstr com.android.chrome'
        result=os.popen(cmd).readlines()
        for line in result:
            if line.endswith('com.android.chrome\n'):
                line='#'.join(line.split())
                self.pid=line.split('#')[1]

        return self.pid

    def get_flow(self,pid):

        cmd='adb shell cat /proc/{}/net/dev'.format(pid)
        result=os.popen(cmd).readlines()

        for line in result:
            if 'wlan0'in line:
                line="#".join(line.split())
                print(line)
                receive=line.split('#')[1]
                send=line.split('#')[9]
                self.flow=int(receive)+int(send)

        return self.flow/1024/1024

    def getCurrentTime(self):
        self.currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return self.currentTime


    def test_once(self):
        self.pid=self.get_pid()
        first=self.get_flow(self.pid)

        self.test_operate()

        second = self.get_flow(self.pid)
        self.flow=second-first
        self.currentTime = self.getCurrentTime()
        self.result.append((self.flow, self.currentTime))

    def test_operate(self):
        self.driver.get('http://www.baidu.com')
        # tmp_list=['selenium','appium','python','test home','51test']
        tmp_list = ['selenium', 'appium']
        for i in tmp_list:
            self.driver.find_element_by_id('index-kw').send_keys(i)
            self.driver.find_element_by_id('index-bn').click()
            self.driver.implicitly_wait(5)
            self.driver.back()
            self.driver.implicitly_wait(5)

    def run(self,count):
        for i in range(count):
            self.test_once()
        self.driver.quit()


    def save_data(self):
        csvData = open("flowData.csv", 'w', newline='')
        writer = csv.writer(csvData)
        writer.writerows(self.result)
        csvData.close()

if __name__ == '__main__':
    cl=Control(5)
    cl.run(cl.count)
    cl.save_data()