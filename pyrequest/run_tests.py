import time,sys
sys.path.append('./interface')
sys.path.append('./db_fixture')
from HTMLTestRunnerCN import HTMLTestReportCN
import unittest
from db_fixture import test_data

test_dir='./interface'

discover=unittest.defaultTestLoader.discover(test_dir,pattern='*_test.py')

if __name__ == '__main__':
    test_data.init_data()#初始化接口测试数据

    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./report/'+now+'_result.html'
    fp=open(filename,'wb')

    runner=HTMLTestReportCN(stream=fp,
                            title='Guest Manage System Interface Test Report',
                            description='测试结果为：')
    runner.run(discover)
    fp.close()
