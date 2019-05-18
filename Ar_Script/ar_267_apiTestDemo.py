#encoding=utf-8
from BeautifulReport import BeautifulReport as bf
import unittest
import requests

class ApiTest(unittest.TestCase):

    def setUp(self):
        pass
    def tearDown(self):
        pass

    def testBaidu(self):
        '测试百度官网的状态码返回结果'
        self.response=requests.get('http://www.baidu.com')
        self.assertEqual(self.response.status_code,200)

    def testBaidu2(self):
        '测试百度官网的状态码返回结果'
        self.response=requests.get('http://www.baidu.com')
        self.assertEqual(self.response.status_code,200)

    def testBaidu3(self):
        '测试百度官网的状态码返回结果'
        self.response=requests.get('http://www.baidu.com')
        self.assertEqual(self.response.status_code,200)

suite=unittest.TestSuite()
suite.addTest(ApiTest('testBaidu'))
suite.addTest(ApiTest('testBaidu2'))
suite.addTest(ApiTest('testBaidu3'))
runner=bf(suite)
runner.report(filename='testreport',description='这是一个测试报告')
