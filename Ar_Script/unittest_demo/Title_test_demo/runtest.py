import unittest
from HTMLTestRunner import HTMLTestRunner
import time

start_dir='./'
discover=unittest.defaultTestLoader.discover(start_dir,pattern='test*.py')

if __name__ == '__main__':
    runtime = time.strftime('%Y-%m-%d %H_%M_%S', time.localtime())
    save_file=open('Report/%s result.html'%runtime,'wb')

    runner=HTMLTestRunner(
        stream=save_file,
        title='搜索测试报告',
        description='用例执行情况：'
    )
    runner.run(discover)
    save_file.close()
