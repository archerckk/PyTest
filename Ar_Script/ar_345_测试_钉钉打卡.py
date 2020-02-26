from appium import webdriver
import json
import time
import os
import random
from tool.logger import Loger
import logging

'''
1、工作日上班打卡已验证
2、工作日下班打卡已验证

'''


def clear():
    cmd = 'adb shell am force-stop com.android.vending'
    cmd2 = 'adb shell input keyevent KEYCODE_HOME'
    os.popen(cmd)
    os.popen(cmd2)


class AutoClick(object):

    def __init__(self):
        with open('./resources/phone.json')as f:
            desired_caps = json.load(f)['sanxingC8_dingding']

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        self.window = self.driver.get_window_size()
        self.width = self.window['width']
        self.height = self.window['height']
        self.work = True
        self.off = True

    def prepare_click(self):
        '从钉钉主界面到考勤打卡的点击动作'
        self.check_work_icon=False
        self.check_work=False
        account_xpath='//*[@text="请输入密码"][@class="android.widget.EditText"]'
        login_xpath='//*[@text="登录"][@class="android.widget.TextView"]'

        #假如账号退出了登录账号
        if '你好' in self.driver.page_source:
            self.driver.find_element_by_xpath(account_xpath).send_keys('a3203589')
            self.driver.find_element_by_xpath(login_xpath).click()
            time.sleep(5)

        #点击首页的工作按钮
        work_icon_xpath='//*[@resource-id="com.alibaba.android.rimet:id/home_bottom_tab_button_work"]/android.widget.FrameLayout[1]'
        if self.driver.find_elements_by_xpath(work_icon_xpath):
            self.driver.find_element_by_xpath(work_icon_xpath).click()
            logging.debug('点击首页工作icon成功')
            self.check_work_icon=True
        time.sleep(10)

        # 兼容8.1系统手机
        context=self.driver.contexts
        print(context)
        self.driver.switch_to.context(context[0])
        time.sleep(3)
        print(self.driver.current_context)

        check_work_xpath = '//*[@content-desc="考勤打卡"][@class="android.view.View"]/..'

        print(self.driver.find_elements_by_xpath(check_work_xpath))

        # 点击考勤打卡按钮
        check_work_xpath = '//*[@content-desc="考勤打卡"][@class="android.view.View"]/..'
        if self.driver.find_elements_by_xpath(check_work_xpath):
            self.driver.find_element_by_xpath(check_work_xpath).click()
            logging.debug('点击考勤打卡执行完成')
            self.check_work=True

        if self.check_work and self.check_work_icon:
            logging.debug('前置步骤执行成功')
        else:
            logging.debug('前置步骤执行失败')

        return self.check_work,self.check_work_icon
        # 点击工作tab
        # work_tab_x1_rate=0.45
        # work_tab_x2_rate=0.54
        # work_tab_y1_rate=0.93
        # work_tab_y2_rate=0.98
        # self.driver.tap([(self.width*work_tab_x1_rate,self.height*work_tab_y1_rate),(self.width*work_tab_x2_rate,self.height*work_tab_y2_rate)],100)

        # 考勤打卡坐标点击
        # on_work_tab_x1_rate = 0.77
        # on_work_tab_x2_rate = 0.67
        # on_work_tab_y1_rate = 0.92
        # on_work_tab_y2_rate = 0.75
        # self.driver.tap([(self.width*on_work_tab_x1_rate,self.height*on_work_tab_y1_rate),(self.width*on_work_tab_x2_rate,self.height*on_work_tab_y2_rate)],100)

    def on_work(self):
        '上班打卡'
        try:
            cant_off_work_xpath = '//*[@content-desc="外勤打卡"]/..'
            if self.driver.find_element_by_xpath(cant_off_work_xpath).is_displayed():
                logging.debug('不在打卡范围，不触发点击事件')
        except Exception:
            off_work_xpath = '(//android.view.View[@content-desc="下班打卡"])'
            off_work_weekend_xpath = '(//android.view.View[@content-desc="下班打卡"])[2]'

            if self.driver.find_elements_by_xpath(off_work_xpath):
                logging.debug('工作日上班打卡已执行')
                self.work = False
                pass
            elif self.driver.find_elements_by_xpath(off_work_weekend_xpath):
                logging.debug('加班上班打卡已执行')
                self.work = False
                pass
            else:
                on_work_xpath = '(//android.view.View[@content-desc="上班打卡"])'
                on_work_weekend_xpath = '(//android.view.View[@content-desc="上班打卡"])[2]'
                if self.driver.find_elements_by_xpath(on_work_xpath):
                    self.driver.find_element_by_xpath(on_work_xpath).click()
                else:
                    self.driver.find_element_by_xpath(on_work_weekend_xpath).click()

        time.sleep(3)
        if '上班打卡成功' in self.driver.page_source:
            logging.debug('上班打卡成功')

    def off_work(self):
        '下班打卡'
        try:
            cant_off_work_xpath = '//*[@content-desc="无法打卡"]/..'
            if self.driver.find_element_by_xpath(cant_off_work_xpath).is_displayed():
                logging.debug('现在无法打卡，不触发点击事件')
        except Exception:
            on_work_xpath = '(//android.view.View[@content-desc="上班打卡"])'
            off_work_xpath = '(//android.view.View[@content-desc="下班打卡"])'
            on_work_weekend_xpath = '(//android.view.View[@content-desc="上班打卡"])[2]'
            off_work_weekend_xpath = '(//android.view.View[@content-desc="下班打卡"])[2]'

            if '外勤打卡' in self.driver.page_source:
                logging.debug('外勤打卡状态，无法点击下班卡')
            elif self.driver.find_elements_by_xpath(on_work_xpath):
                logging.debug('工作日上班卡还没有打，无法点击下班卡')
            elif self.driver.find_elements_by_xpath(on_work_weekend_xpath):
                logging.debug('加班上班卡还没有打，无法点击下班卡')
            else:
                if self.driver.find_elements_by_xpath(off_work_weekend_xpath):
                    logging.debug('执行加班下班打卡')
                    # self.driver.find_elements_by_xpath(off_work_weekend_xpath).click()
                elif self.driver.find_elements_by_xpath(off_work_xpath):
                    logging.debug('执行工作日下班打卡')
                    # self.driver.find_element_by_xpath(off_work_xpath).click()
                else:
                    logging.debug('下班卡已打卡完成')

        time.sleep(3)
        if '下班打卡成功' in self.driver.page_source:
            logging.debug('下班打卡点击成功')

    def quit(self):
        self.driver.quit()


if __name__ == '__main__':
    log=Loger('dingding_work')

    on_work_time = int(input('请输入上班打卡具体小时：'))
    off_work_time = int(input('请输入下班打卡具体小时：'))
    shutdown_time =int(input('请输入关机具体小时：'))
    minute_check=int(input('是否启用分钟检查(0/1)：'))

    randminute_on=random.randint(0,30)
    randminute_off=random.randint(0,21)

    while True:
        startTime = time.localtime()
        if startTime[3] == on_work_time:
            if startTime[4]==randminute_on:
                clear()
                ak = AutoClick()
                check_work,check_work_icon=ak.prepare_click()

                if check_work and check_work_icon:
                    time.sleep(6)
                    ak.on_work()
                ak.quit()

        elif startTime[3] == off_work_time:
            if minute_check:
                if startTime[4]==randminute_off:
                    clear()
                    ak = AutoClick()
                    check_work, check_work_icon = ak.prepare_click()
                    if check_work and check_work_icon:
                        time.sleep(6)
                        ak.off_work()
                    ak.quit()
            else:
                clear()
                ak = AutoClick()
                check_work, check_work_icon = ak.prepare_click()
                if check_work and check_work_icon:
                    time.sleep(6)
                    ak.off_work()
                ak.quit()

        elif startTime[3]==shutdown_time:
            command='shutdown -s -t 10'
            os.popen(command)

        else:
            continue

