from Ar_Script.unittest_demo.Cal_demo import Calculator as cal

import unittest


class Testadd(unittest.TestCase):
    def setUp(self):
        print('test sub start')

    def tearDown(self):
        print('test sub end')

    def test_case1(self):
        count = cal.Cal(5, 6)
        self.assertEqual(count.sub(), -1, '结果不等于-1')

    def test_case2(self):
        count = cal.Cal(11, 15)
        self.assertEqual(count.sub(), -4, '结果不等于-4')