import pytest
import allure
from Ar_Script.Meetu_Ui_Test.Pages.base_page import *
import json
from appium import webdriver
import time
import os
import openpyxl
from Ar_Script.Meetu_Ui_Test.common.get_info import get_meminfo_data,saveData,get_cpu_data,get_activity_name
from Ar_Script.Meetu_Ui_Test.common.app_command import *
import logging
import random
import subprocess


def test_app_cpu_home_stay_cost():
    package_info=get_activity_name()
    os.popen('adb shell am start {}/{}'.format(package_info[1],package_info[2]))
    time.sleep(5)
    os.popen('adb shell input keyevent 4 ')
    result=[('测试时间','cpu百分比')]
    result.extend(get_cpu_data(package_info[1]))
    data_save=Data_Save(result,'cpu_test','test_result.xlsx',(0,1),(0,'C1'))
    data_save.save_data()

#
# class Test_Performance:
#
#     # @classmethod
#     # def setup_class(self):
#     #     os.popen('adb shell pm clear {}'.format('com.meetu.android'))
#     #     print('执行清理数据')
#
#     def setup(self):
#         os.chdir(os.curdir)
#         with open('..\config\phone.json')as f:
#             desired_caps = json.load(f)['sanxingC8_meetu']
#
#
#         self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
#         self.package_info=('',desired_caps['appPackage'],desired_caps['appActivity'])
#         self.account_page = Account_login_page(self.driver)
#         self.start_page = StarPage(self.driver)
#         self.home_page=Home_page(self.driver)
#
#         self.hot_start_control=Control(self.package_info,count=16,driver=self.driver)
#         self.cold_start_control=Control(self.package_info,count=16,driver=self.driver,mode=1)
#
#         self.loger=Loger()
#         # self.windows_size = self.driver.get_window_size()
#         # self.height = self.windows_size['height']
#         # self.width = self.windows_size['width']
#
#         self.driver.implicitly_wait(30)
#
#     def teardown(self):
#         self.driver.quit()
#
#
#
#
#     @allure.story('重复启动app内存测试')
#     @pytest.mark.parametrize('package,activity',[('com.meetu.android',"com.meetu.android.SplashActivity")])
#     def test_meminfo(self,package,activity):
#         account='archerckk@163.com'
#         psw='123456'
#         meminfo_list=[]
#
#
#         #登录app
#         self.start_page.click_account_login()
#         self.account_page.account_input(account)
#         self.account_page.psw_input(psw)
#         self.account_page.click_login()
#
#         #处理权限允许弹窗
#         self.home_page.permission_allow()
#
#         #处理引导动画
#         self.home_page.close_guide()
#
#         for i in range(15):
#             self.driver.keyevent(4)
#             self.driver.start_activity(package,activity)
#             if self.home_page.loading_finish_judge():
#                 result=get_meminfo_data(package)
#                 meminfo_list.append(result)
#
#         logging.debug(meminfo_list)
#         saveData(meminfo_list,file_attr='meetU_v{}'.format("test"))
#
#
#     @allure.story('启动时间测试')
#     @pytest.mark.parametrize('package_info',[('','com.meetu.android',"com.meetu.android.SplashActivity")])
#     def test_app_start_time(self,package_info):
#         self.hot_start_control.run()
#         self.hot_start_control.saveData('热启动_v33')
#
#         self.cold_start_control.run()
#         self.cold_start_control.saveData('冷启动_v33')
#
#     @allure.story('cpu 空闲状态消耗信息记录')
#     def test_app_cpu_home_stay_cost(self):
#         print(get_cpu_data_t(self.package_info[1]))
#         # self.driver.keyevent(4)
#         # result=[('测试时间','cpu百分比')]
#         # result.extend(get_cpu_data_t(self.package_info[1]))
#         # data_save=Data_Save(result,'cpu_test','test_result.xlsx',(0,1),(0,'C1'))
#         # data_save.save_data()

if __name__ == '__main__':
    # pytest.main(['-s','performance_data_test.py'])
    # print(get_cpu_data('com.real'))
    test_app_cpu_home_stay_cost()