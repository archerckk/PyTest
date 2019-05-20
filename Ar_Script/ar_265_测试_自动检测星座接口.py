#encoding=utf-8
import logging
import requests
import unittest
import re

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s-%(levelname)s-%(message)s')

class DailyTest(unittest.TestCase):

    def setUp(self):
        pass

    def testChinaApi(self):
        self.responseCh=requests.get('http://api.dailyhoroscopepro.info/horoscope/article')
        # self.response.request.get('http://api.apluscamera.info/v3/horoscopes/index/20190505/1')
        print("星座汉化版接口请求返回码为：", self.responseCh)
        regXml=re.compile('{"code":(\d+).+')
        print('接口的返回内容为：', self.responseCh.text[0:20])
        self.assertEqual(self.responseCh.status_code,200)
        logging.debug(regXml.search(self.responseCh.text[0:30]).group(1))
        self.assertNotEqual(regXml.search(self.responseCh.text[0:30]).group(1), 404)


    def testEnglishApi(self):
        regXml=re.compile('{"code":(\d+).+')

        self.responseEn=requests.get('http://api.dailyhoroscopepro.info/v3/horoscopes/index/20190517/1')
        print("星座中文版接口请求返回码为：", self.responseEn.status_code)
        print('接口的返回内容为：', self.responseEn.text[0:20])
        self.assertEqual(self.responseEn.status_code,200)
        logging.debug(regXml.search(self.responseEn.text[0:30]).group(1))
        self.assertNotEqual(regXml.search(self.responseEn.text[0:30]).group(1), 404)

    def tearDown(self):
        pass


