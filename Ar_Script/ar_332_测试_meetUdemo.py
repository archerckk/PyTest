import unittest
import logging
from ar_332_测试_请求_meetUGet import Get_test


logging.basicConfig(level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s')

suite = unittest.TestSuite()
suite.addTest(Get_test('test_match_list_429'))
runner=unittest.TextTestRunner()
# runner=unittest.TestRunner()
runner.run(suite)
