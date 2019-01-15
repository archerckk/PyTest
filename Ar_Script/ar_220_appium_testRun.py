# coding=utf-8
from ar_220_appium_testXPE import *
import unittest
suite=unittest.TestSuite()
# suite.addTest(Test_Case('test_case1'))
# suite.addTest(Test_Case('test_case2'))
suite.addTest(Test_Case('test_case3'))

runner=unittest.TextTestRunner()
runner.run(suite)