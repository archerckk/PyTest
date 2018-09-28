import unittest
import subprocess
import os

def setUpModule():
    print('test modle strat >>>>>>>>>>>')

def tearDownModule():
    print('test modle end >>>>>>>>>>>')

class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('test class start -----------')

    @classmethod
    def tearDownClass(cls):
        print('test class end --------------')

    def setUp(self):
        print('test start ----->')


    def tearDown(self):
        print('test end -------->')


    def test_print(self):
        print('print aaaa')

if __name__ == '__main__':
    test=unittest.main()


'测试代码'
# file_name=os.getcwd()+os.sep+'ar_199_测试_fixtures.py'
#
# cmd='python %s'%file_name
# log = open('log.txt', 'w')
# print(123)
# subprocess.Popen('ping www.baidu.com',shell=True,stdout=log)
# log.close()
# sub.wait(10)
# print(sub.stdout.read())
