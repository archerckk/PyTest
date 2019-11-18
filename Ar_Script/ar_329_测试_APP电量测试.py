import time,csv,os,json
from appium import webdriver

class Control(object):

    def __init__(self,count):
        self.count=count
        self.battery=0
        self.current_time=0

        with open('resources/motog5.json','r')as f:
            desired_caps=json.load(f)
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.result=[('测试时间','电量值')]

    def operate(self):
        self.driver.get('http://www.baidu.com')
        # tmp_list=['selenium','appium','python','test home','51test']
        tmp_list = ['selenium', 'appium']
        for i in tmp_list:
            self.driver.find_element_by_id('index-kw').send_keys(i)
            self.driver.find_element_by_id('index-bn').click()
            self.driver.implicitly_wait(5)
            self.driver.back()
            self.driver.implicitly_wait(5)

    def get_time(self):
        self.current_time=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        return self.current_time

    def get_battery(self):
        cmd = 'adb shell dumpsys battery'
        content = os.popen(cmd)
        for lines in content:
            if 'level' in lines:
                self.battery = lines.split(':')[1]
                break
        return self.battery


    def test_once(self):
        self.battery=self.get_battery()
        current_time=self.get_time()
        self.result.append((current_time,self.battery))

        self.operate()

        self.battery = self.get_battery()
        current_time = self.get_time()
        self.result.append((current_time, self.battery))

    def run(self,count):
        cmd='adb shell dumpsys battery unplug'
        os.popen(cmd)
        count=int(count*10/5)
        for i in range(count):
            self.test_once()
            time.sleep(5)


    def save_data(self):
        csv_data=open('power.csv','w',newline='')
        writer=csv.writer(csv_data)
        writer.writerows(self.result)
        csv_data.close()


cl=Control(1)
cl.run(cl.count)
cl.save_data()
