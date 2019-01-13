# coding=utf-8
import unittest
from ar_198_测试_测试计算类优化结构 import *

suit = unittest.TestSuite()
suit.addTest(Test_Add('test_case1'))
suit.addTest(Test_Sub('test_case1'))

runner = unittest.TextTestRunner()
runner.run(suit)