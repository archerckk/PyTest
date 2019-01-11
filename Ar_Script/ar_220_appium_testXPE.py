from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
import unittest
import os
import time


class SearchTest(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['automationName'] = 'Appium'
        desired_caps['deviceName'] = '98891936513437444f'
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '8.0'
        desired_caps['noReset'] = True
        desired_caps["appPackage"] = "com.picstudio.photoeditorplus"
        desired_caps["appActivity"] = "com.picstudio.photoeditorplus.camera.MainActivity"

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        sleep(5)

        '按4下返回键退出订阅页'
        # for i in range(2):
        #     self.driver.press_keycode(4)
        #     sleep(1)

    def test_case(self):
        driver=self.driver
        img_folder=os.curdir+os.sep+'result'
        cur_time=time.strftime('%Y_%m_%d_%H_%M_%S',time.localtime())
        screen_shot=img_folder+os.sep+cur_time+'_'+'拼图截图保存.png'


        # for i in range(4):
        #     driver.press_keycode(4)
        #     sleep(1)
        '点击主页collage icon'
        collage=driver.find_element_by_xpath("//*[@resource-id='com.picstudio.photoeditorplus:id/tc'][@text='COLLAGE']")
        collage.click()

        '处理进入相册的全屏广告'
        if 'android.webkit.WebView' in driver.page_source:
            driver.press_keycode(4)
            sleep(2)
            driver.press_keycode(4)

        '在相册选择同一张照片3张'

        pic_out=driver.find_element_by_xpath("//*[@resource-id='com.picstudio.photoeditorplus:id/a4h'][@text='Start']/../..")
        pic_frame=pic_out.find_element_by_class_name('android.widget.FrameLayout')
        pic_tmp=pic_frame.find_element_by_class_name('android.widget.RelativeLayout')
        pic_list=pic_tmp.find_element_by_class_name('android.widget.ListView')
        pic_list_position=pic_list.rect

        origin_album=pic_list.find_element_by_xpath("//*[@class='android.widget.LinearLayout'][@index=0]")
        origin_album_position=origin_album.rect
        print(origin_album_position)

        origin_pic=pic_list.find_element_by_xpath("//*[@class='android.widget.LinearLayout'][@index=1]")
        origin_pic_position=origin_pic.rect
        print(origin_pic_position)
        origin_pic_x=(origin_pic_position['width']-18)/3/2

        origin_pic_y=(origin_pic_position['y']+(origin_pic_position['height']/2))

        target_x=origin_pic_x+((origin_pic_position['width']-18)/3)*1
        target_y=origin_pic_y+origin_pic_position['height']*0


        print(target_x,target_y)
        for i in range(3):
            driver.tap([(target_x,target_y)])
            sleep(0.5)

        '点击开始拼图'
        start=driver.find_element_by_xpath("//*[@resource-id='com.picstudio.photoeditorplus:id/a4h'][@text='Start']")
        start.click()
        sleep(3)

        '切换到拼图tab'
        change=driver.find_element_by_xpath("//*[@resource-id='com.picstudio.photoeditorplus:id/f3'][@index=2][@class='android.widget.ImageView']")
        change.click()
        sleep(0.5)
        '保存图片'
        # out_side_change=driver.find_element_by_xpath("//*[@resource-id='com.picstudio.photoeditorplus:id/f3'][@index=2]/..")
        #
        # confirm=out_side_change.find_element_by_xpath("//*[@class='android.widget.ImageView'][4]")

        confirm=driver.find_element_by_xpath("//*[@resource-id='com.picstudio.photoeditorplus:id/gc']")
        confirm.click()
        sleep(5)
        '按返回键关闭广告'
        if 'android.webkit.WebView' in driver.page_source:
            driver.press_keycode(4)
            sleep(2)

        if 'Not Really'in driver.page_source:
            driver.press_keycode(4)
            sleep(2)

        if 'Save to album' not in driver.page_source:
            assert print('拼图保存失败')
        else:
            print('测试通过，正确保存拼图')

        '保存截图'
        driver.save_screenshot(screen_shot)
        sleep(3)

    # def test_case2(self):
    #     driver=self.driver
    #     camera = driver.find_element_by_xpath('//*[@resource-id="com.picstudio.photoeditorplus:id/l_"][@index=2]')
    #     max_size = driver.get_window_size()
    #     x=max_size['width']
    #     y=max_size['height']
    #     t=100
    #     while "View all" not in driver.page_source:
    #         x1=int(x*0.5)
    #         y1=int(y*0.75)
    #         y2=int(y*0.25)
    #         t=100
    #
    #         driver.swipe(x1,y1,x1,y2,t)
    #         sleep(0.1)
    #
    #     '测试代码'
    #     x1=int(x*0.5)
    #     y1=int(y*0.25)
    #     y2=int(y*0.75)
    #     driver.swipe(x1, y1, x1, y2, t)
    #     sleep(2)
    #     if 'android.widget.ImageButton' not in driver.page_source:
    #         print('测试通过，滑动到底部并且没有拍照按钮展示')
    #         sleep(3)
    #     else:
    #
    #         assert print('bug,滑动到底部还有拍照按钮显示')

    # def test_case3(self):
        # driver=self.driver
        # cut=driver.find_element_by_xpath("//*[@resource-id='com.picstudio.photoeditorplus:id/tc']")







    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()