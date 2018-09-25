import unittest
from Ar_Script.unittest_demo.Cal_demo import test_add
from Ar_Script.unittest_demo.Cal_demo import test_sub

suite=unittest.TestSuite()
suite.addTest(test_add.Testadd('test_case1'))
suite.addTest(test_add.Testadd('test_case2'))
suite.addTest(test_sub.Testadd('test_case1'))
suite.addTest(test_sub.Testadd('test_case2'))

if __name__ == '__main__':
    runner=unittest.TextTestRunner()
    runner.run(suite)