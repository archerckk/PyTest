from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
import unittest
import os
import time
from ar_221_测试_获取meminfo import get_meminfo


class SearchTest_Main(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['automationName'] = 'Appium'
        # desired_caps['deviceName'] = '68cac4b1'
        # desired_caps['deviceName'] = '5LM0215C28005216'
        desired_caps['deviceName'] ='LGD8587de68c9'
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.0.1'
        desired_caps['noReset'] = True
        desired_caps["appPackage"] = "com.picstudio.photoeditorplus"
        desired_caps["appActivity"] = "com.picstudio.photoeditorplus.camera.MainActivity"

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        sleep(5)

        '按4下返回键退出订阅页'
        # for i in range(2):
        #     self.driver.press_keycode(4)
        #     sleep(0.5)

    def tearDown(self):
        self.driver.quit()




class Test_Case(SearchTest_Main):
    def test_case1(self):
        """
        保存一张3个拼图的图片
        :return: 
        """
        driver = self.driver
        img_folder = os.curdir + os.sep + 'result'
        cur_time = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())
        screen_shot = img_folder + os.sep + cur_time + '_' + '拼图截图保存.png'

        # for i in range(4):
        #     driver.press_keycode(4)
        #     sleep(1)
        '点击主页collage icon'
        # icon_str="//*[@resource-id='com.picstudio.photoeditorplus:id/ql'][@text='X Photo Editor'][@class='android.widget.TextView']"
        # icon=driver.find_element_by_xpath(icon_str)
        # print(icon.rect)

        # '主页截图测试代码'
        # driver.save_screenshot(screen_shot)
        # driver.get_screenshot_as_file(screen_shot)
        # sleep(2)

        '获取手机的系统版本信息'
        version_command="adb shell getprop ro.build.version.release"
        android_version=os.popen(version_command).readlines()[0].split('\n')[0]

        Collage_list=['4.4.4','5.0.1']
        if android_version in Collage_list:
            collage = driver.find_element_by_xpath(
            "//*[@resource-id='com.picstudio.photoeditorplus:id/tc'][@text='Collage']")
            collage.click()
        elif android_version=='7.0':
            collage = driver.find_element_by_xpath(
                "//*[@resource-id='com.picstudio.photoeditorplus:id/tc'][@text='COLLAGE']")
            collage.click()

        '处理进入相册的全屏广告'
        if 'android.webkit.WebView' in driver.page_source:
            driver.press_keycode(4)
            sleep(2)
            driver.press_keycode(4)

        '在相册选择同一张照片3张'

        pic_out = driver.find_element_by_xpath(
            "//*[@resource-id='com.picstudio.photoeditorplus:id/a4h'][@text='Start']/../..")
        pic_frame = pic_out.find_element_by_class_name('android.widget.FrameLayout')
        pic_tmp = pic_frame.find_element_by_class_name('android.widget.RelativeLayout')
        pic_list = pic_tmp.find_element_by_class_name('android.widget.ListView')
        pic_list_position = pic_list.rect

        origin_album = pic_list.find_element_by_xpath("//*[@class='android.widget.LinearLayout'][@index=0]")
        origin_album_position = origin_album.rect

        origin_pic = pic_list.find_element_by_xpath("//*[@class='android.widget.LinearLayout'][@index=1]")
        origin_pic_position = origin_pic.rect

        origin_pic_x = (origin_pic_position['width'] - 18) / 3 / 2
        origin_pic_y = (origin_pic_position['y'] + (origin_pic_position['height'] / 2))

        target_x = origin_pic_x + ((origin_pic_position['width'] - 18) / 3) * 1
        target_y = origin_pic_y + origin_pic_position['height'] * 0

        for i in range(3):
            driver.tap([(target_x, target_y)])
            sleep(0.5)

        '点击开始拼图'
        start = driver.find_element_by_xpath("//*[@resource-id='com.picstudio.photoeditorplus:id/a4h'][@text='Start']")
        start.click()
        driver.implicitly_wait(15)
        # sleep(10)

        '切换到拼图tab'
        change = driver.find_element_by_xpath(
            "//*[@resource-id='com.picstudio.photoeditorplus:id/f3'][@index=2][@class='android.widget.ImageView'][@instance=4]")
        change.click()
        sleep(0.5)
        '保存图片'
        # out_side_change=driver.find_element_by_xpath("//*[@resource-id='com.picstudio.photoeditorplus:id/f3'][@index=2]/..")
        #
        # confirm=out_side_change.find_element_by_xpath("//*[@class='android.widget.ImageView'][4]")

        # confirm = driver.find_element_by_xpath(
        #     # "//*[@resource-id='com.picstudio.photoeditorplus:id/gc']")
        confirm=driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ImageView[2]')

        confirm.click()
        sleep(5)


        '按返回键关闭广告'
        if 'android.webkit.WebView' in driver.page_source:
            driver.press_keycode(4)
            sleep(2)

        if 'Not Really' in driver.page_source:
            driver.press_keycode(4)
            sleep(2)

        if 'Save to album' not in driver.page_source:
            assert print('拼图保存失败')
        else:
            print('测试通过，正确保存拼图')
            '保存截图'
            driver.save_screenshot(screen_shot)
            # driver.get_screenshot_as_file(screen_shot)
            sleep(3)
            print('截图保存为%s'%screen_shot)
    # @unittest.skip('跳过测试不执行')
    def test_case2(self):
        """
        将界面滑动到最底部然后检查是否有拍照按钮显示在界面上面
        :return: 
        """
        driver = self.driver
        # camera = driver.find_element_by_xpath('//*[@resource-id="com.picstudio.photoeditorplus:id/l_"][@index=2][class="android.widget.ImageButton"]')
        max_size = driver.get_window_size()
        x = max_size['width']
        y = max_size['height']
        t = 500
        while "View all" not in driver.page_source:
            x1 = int(x * 0.5)
            y1 = int(y * 0.75)
            y2 = int(y * 0.25)
            t = 500

            driver.swipe(x1, y1, x1, y2, t)
            sleep(0.5)

        '测试代码'
        # x1=int(x*0.5)
        # y1=int(y*0.25)
        # y2=int(y*0.75)
        # driver.swipe(x1, y1, x1, y2, t)
        # sleep(2)
        if 'android.widget.ImageButton' not in driver.page_source:
            print('测试通过，滑动到底部并且没有拍照按钮展示')
            sleep(3)
        else:

            assert print('bug,滑动到底部还有拍照按钮显示')

    def test_case3(self):
        '多次点击进入商店回退到主页之后内存数值的变化情况'
        driver=self.driver
        origin_meminfo=get_meminfo()
        print(origin_meminfo)

        for i in range(15):
            cut=driver.find_element_by_xpath(
                "//*[@resource-id='com.picstudio.photoeditorplus:id/tc']"
                "[@text='Effects']")
            cut.click()

            '进入商店（相册）广告处理'
            if "com.picstudio.photoeditorplus:id/ad_cormImage" in driver.page_source:
                driver.press_keycode(3)
            elif 'android.webkit.WebView' in driver.page_source:
                driver.press_keycode(3)


            tab_makeover=driver.find_element_by_xpath(
                "//*[@resource-id='com.picstudio.photoeditorplus:id/c9']"
                "[@instance=4]"
            )
            tab_makeover.click()
            driver.implicitly_wait(3)

            tab_filters = driver.find_element_by_xpath(
                "//*[@resource-id='com.picstudio.photoeditorplus:id/c9']"
                "[@instance=5]"
            )
            tab_filters.click()
            driver.implicitly_wait(3)

            tab_hot = driver.find_element_by_xpath(
                "//*[@resource-id='com.picstudio.photoeditorplus:id/c9']"
                "[@instance=3]"
            )
            tab_hot.click()
            sleep(3)

            driver.find_element_by_xpath(
                "//*[@resource-id='com.picstudio.photoeditorplus:id/ni']"
                "[@instance=0]"
            ).click()
            # driver.press_keycode(3)
            sleep(2)

        sleep(5)
        result_meminfo=get_meminfo()
        print(result_meminfo)






