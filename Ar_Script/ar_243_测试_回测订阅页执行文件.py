import os
import time
import unittest
from ar_242_测试_回测订阅页ui问题 import *
from HTMLTestRunnerCN import HTMLTestReportCN

now =time.strftime('%Y_%m_%d_%H_%M_%S',time.localtime())
report_name =os.getcwd( ) +os.sep +'result' +os.sep +now +'report.html'

file =open(report_name ,'wb')

suite =unittest.TestSuite()
suite.addTest(SearchTest("test_sub_ui"))

runner =HTMLTestReportCN(
    stream=file,
    title='A+相机订阅页清数据之后订阅UI显示测试',
    description="用例执行情况："
)

runner.run(suite)
file.close()