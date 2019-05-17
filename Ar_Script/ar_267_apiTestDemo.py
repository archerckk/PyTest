from BeautifulReport import BeautifulReport
import unittest
import requests

class ApiTest(unittest.TestCase):

    def setUp(self):
        pass
    def tearDown(self):
        pass

    def testBaidu(self):
        self.response=requests.get('http://www.baidu.com')
        self.assertEqual(self.response.status_code,200)

suite=unittest.TestSuite()
suite.addTest(ApiTest('testBaidu'))