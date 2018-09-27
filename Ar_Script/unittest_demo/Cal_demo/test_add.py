from Ar_Script.unittest_demo.Cal_demo import Calculator as cal

import unittest

class Testadd(unittest.TestCase):

    def setUp(self):
        print('test add start')

    def tearDown(self):
        print('test add end')

    def test_case1(self):
        count=cal.Cal(5,6)
        self.assertEqual(count.add(),12,'结果不等于11')

    def test_case2(self):
        count=cal.Cal(11,15)
        self.assertEqual(count.add(),12,'结果不等于26')

