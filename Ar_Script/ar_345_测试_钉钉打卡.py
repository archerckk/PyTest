from appium import webdriver
import json
import time

class AutoClick(object):

    def __init__(self):
        with open('./resources/phone.json')as f:
            desired_caps=json.load(f)['sanxingC8_dingding']

        self.driver=webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def work(self):
        #点击工作tab
        self.driver.find_element_by_xpath('//*[@resource-id="com.alibaba.android.rimet:id/home_bottom_tab_icon"][@instance=8]').click()
        time.sleep(5)
        #点击考勤打卡按钮
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/com.uc.webview.export.WebView/com.uc.webkit.be/android.webkit.WebView/android.view.View/android.view.View[3]/android.view.View[3]/android.view.View[8]/android.view.View[1]/android.view.View[1]/android.view.View').click()
        # time.sleep(5)
        # self.driver.find_element_by_xpath('//*[@class="android.view.View"][@instance=127]').click()



if __name__ == '__main__':
    ak=AutoClick()
    ak.work()

