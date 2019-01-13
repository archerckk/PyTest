import unittest
from ar_196_测试_计算类测试对象 import Cal

class Test_Cal(unittest.TestCase):

    def setUp(self):
        print('test start')

    def test_add(self):
        test=Cal(2,3)
        self.assertEqual(test.add(),5)
        print('执行用例1')

    def test_add2(self):
        test=Cal(11,11)
        self.assertEqual(test.add(),22)
        print('执行用例2')

    def tearDown(self):
        print('test end')

# if __name__ == '__main__':
    # '执行所有用例'
    # unittest.main()

    '创建测试集合'
suite2=unittest.TestSuite()

# print(type(suite2))
suite2.addTest(Test_Cal("test_add2"))
print(suite2)
'执行用例'
runner=unittest.TextTestRunner()
runner.run(suite2)

