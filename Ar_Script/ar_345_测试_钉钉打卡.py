from appium import webdriver
# from appium.common.exceptions import
import json
import time
import os


class AutoClick(object):

    def __init__(self):
        with open('./resources/phone.json')as f:
            desired_caps=json.load(f)['sanxingLan_dingding']

        self.driver=webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        self.window=self.driver.get_window_size()
        self.width=self.window['width']
        self.height=self.window['height']

    def work(self):

        #点击工作tab
        # work_tab_x1_rate=0.45
        # work_tab_x2_rate=0.54
        # work_tab_y1_rate=0.93
        # work_tab_y2_rate=0.98
        # self.driver.tap([(self.width*work_tab_x1_rate,self.height*work_tab_y1_rate),(self.width*work_tab_x2_rate,self.height*work_tab_y2_rate)],100)

        try:
            self.driver.find_element_by_xpath('//*[@resource-id="com.alibaba.android.rimet:id/home_bottom_tab_button_work"]/android.widget.FrameLayout[1]').click()
            time.sleep(10)


            #坐标点击
            # on_work_tab_x1_rate = 0.77
            # on_work_tab_x2_rate = 0.67
            # on_work_tab_y1_rate = 0.92
            # on_work_tab_y2_rate = 0.75
            # self.driver.tap([(self.width*on_work_tab_x1_rate,self.height*on_work_tab_y1_rate),(self.width*on_work_tab_x2_rate,self.height*on_work_tab_y2_rate)],100)

            # 点击考勤打卡按钮
            self.driver.find_element_by_xpath('//*[@content-desc="考勤打卡"]/..').click()
            print('点击考勤打卡执行完成')
        except Exception as e:
            print(e)
            self.driver.quit()
            assert Exception
        time.sleep(10)

        off_work_tab_x1_rate = 0.33
        off_work_tab_x2_rate = 0.43
        off_work_tab_y1_rate = 0.67
        off_work_tab_y2_rate = 0.63
        self.driver.tap([(self.width*off_work_tab_x1_rate,self.height*off_work_tab_y1_rate),(self.width*off_work_tab_x2_rate,self.height*off_work_tab_y2_rate)])

        # 点击下班打卡
        try:
            cant_off_work_xpath = '//*[@content-desc="无法打卡"]/..'
            if self.driver.find_element_by_xpath(cant_off_work_xpath).is_displayed():
                print('现在无法打卡，不触发点击事件')
        except Exception:
            off_work_xpath = '(//android.view.View[@content-desc="下班打卡"])[2]'
            self.driver.find_element_by_xpath(off_work_xpath).click()

        time.sleep(5)
        if '下班打卡成功'in self.driver.page_source:
                print('下班打卡点击成功')
        # self.driver.find_element_by_android_uiautomator('new UiSelector().className(\"android.widget.TextView\").textContains(\"确定\")')

    def quit(self):
        self.driver.quit()

if __name__ == '__main__':
    cmd='adb shell am force-stop com.android.vending'
    cmd2='adb shell input keyevent KEYCODE_HOME'
    os.popen(cmd)
    os.popen(cmd2)

    ak=AutoClick()
    ak.work()
    ak.quit()
