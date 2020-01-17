import json
from appium import webdriver
import time
import pytest
import allure
import time

class Test_appium:
    def setup(self):
        with open('./resources/phone.json')as f:
            desired_caps=json.load(f)['sanxingC8_dingding']

        self.driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

    @allure.story('测试点击')
    def test_icon_click(self):
        work_icon = 'resourceId("com.alibaba.android.rimet:id/home_bottom_tab_button_work").className("android.widget.RelativeLayout")'
        check_work_icon='//*[@content-desc="考勤打卡"]/..'
        if self.driver.find_elements_by_android_uiautomator(work_icon):
            self.driver.find_element_by_android_uiautomator(work_icon).click()

            time.sleep(5)

            check_work_icon_result=self.driver.find_elements_by_xpath(check_work_icon)
            assert len(check_work_icon_result)!=0

    @pytest.mark.demo
    @allure.story('测试点击')
    def test_icon_click2(self):
        work_icon = 'resourceId("com.alibaba.android.rimet:id/home_bottom_tab_button_work").className("android.widget.RelativeLayout")'
        check_work_icon = '//*[@content-desc="考勤打卡"]/..'
        if self.driver.find_elements_by_android_uiautomator(work_icon):
            self.driver.find_element_by_android_uiautomator(work_icon).click()

            time.sleep(5)

            check_work_icon_result = self.driver.find_elements_by_xpath(check_work_icon)
            assert len(check_work_icon_result) != 0

    def teardown(self):
        self.driver.quit()


def test_one():
    assert 1==1

# work_icon_xpath='//*[@resource-id="com.alibaba.android.rimet:id/home_bottom_tab_button_work"]/android.widget.FrameLayout[1]'
# if driver.find_elements_by_xpath(work_icon_xpath):
#     driver.find_element_by_xpath(work_icon_xpath).click()
#     print('点击首页工作icon成功')

if __name__ == '__main__':
    # pytest.main('./ar_346_测试_钉钉元素定位.py::Test_appium::test_icon_click2')
    pytest.main(['-m','demo','./ar_346_测试_钉钉元素定位.py'])