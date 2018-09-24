from  import auto_cal_demo
import unittest

class Testadd(unittest.TestCase):

    def setUp(self):
        print('test add start')

    def tearDown(self):
        print('test add end')

    def test_case1(self):
        demo=auto_cal_demo
