# coding=utf-8
from ar_220_appium_testXPE import *
import unittest
from HTMLTestRunnerCN import HTMLTestReportCN
import time
import os


now=time.strftime("%Y_%m_%d_%H_%M_%S",time.localtime())
file_name=os.getcwd()+os.sep+'result'+os.sep+now+'report.html'
file=open(file_name,'wb')

suite=unittest.TestSuite()
# suite.addTest(Test_Case('test_case1'))
# suite.addTest(Test_Case('test_case2'))
suite.addTest(Test_Case('test_case3'))
#
# runner=unittest.TextTestRunner()
# runner.run(suite)

runner=HTMLTestReportCN(
    stream=file,
    title='XPE性能测试报告',
    description='XPE性能测试用例执行情况：'
)
runner.run(suite)
file.close()