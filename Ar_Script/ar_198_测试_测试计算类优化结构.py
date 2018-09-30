from ar_196_测试_计算类测试对象 import Cal
import unittest

class Test_main(unittest.TestCase):

    def setUp(self):
        print('开始测试')

    def tearDown(self):
        print('结束测试')

class Test_Add(Test_main):

    def test_case1(self):
        test=Cal(5,1)
        self.assertEqual(test.add(),6,'结果不等与6')

    def test_case2(self):
        test=Cal(15,1)
        self.assertEqual(test.add(),16,'结果不等与16')

class Test_Sub(Test_main):

    def test_case1(self):
        test=Cal(5,1)
        self.assertEqual(test.sub(),4,'结果不等于4')

    def test_case2(self):
        test=Cal(11,1)
        self.assertEqual(test.sub(),9,'结果不等于10')


if __name__ == '__main__':
    suit=unittest.TestSuite()
    suit.addTest(Test_Add('test_case1'))
    suit.addTest(Test_Sub())

    runner=unittest.TextTestRunner()
    runner.run(suit)


