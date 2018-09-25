import unittest
from ar_196_测试_计算类测试对象 import Cal

class Test_Cal(unittest.TestCase):

    def setUp(self):
        print('test start')

    def test_add(self):
        test=Cal(2,3)
        self.assertEqual(test.add(),5)

    def test_add2(self):
        test=Cal(11,11)
        self.assertEqual(test.add(),22)

    def tearDown(self):
        print('test end')

if __name__ == '__main__':
    # '执行所有用例'
    # unittest.main()

    '创建测试集合'
    suite2=unittest.TestSuite()
    suite2.addTest(Test_Cal())

    '执行用例'
    runner=unittest.TextTestRunner()
    runner.run(suite2)

