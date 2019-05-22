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
        '检测国内版星座内容返回接口是否正常'
        apiLink='http://api.dailyhoroscopepro.info/v3/horoscopes/index/20190520/4'
        self.responseCh=requests.get(apiLink)
        # self.response.request.get('http://api.apluscamera.info/v3/horoscopes/index/20190505/1')
        print('接口连接：',apiLink)
        print("星座汉化版接口请求返回码为：", self.responseCh)
        regXml=re.compile('{"code":(%d).+'%404)
        print('接口的返回内容为：', self.responseCh.text)
        if regXml.search(self.responseCh.text)!=None:
            contentCode = regXml.search(self.responseCh.text).group(1)
        else:
            contentCode=None

        self.assertEqual(self.responseCh.status_code, 200)
        if contentCode == None:
            print('页面没有404状态码，测试通过')
        else:
            contentCode = regXml.search(self.responseEn.text).group(1)
            print('code=', contentCode)
            self.assertNotEqual(int(contentCode), 404)
            print('页面有404错误')

    def testEnglishApi(self):
        '检测国际版星座内容返回接口是否正常'
        apiLink = 'http://api.copohoroscopechina.info/horoscope'
        self.responseEn = requests.get(apiLink)
        print('接口连接：', apiLink)
        print("星座国际版接口请求返回码为：", self.responseEn)
        regXml = re.compile('{"code":(\d+).+')
        print('接口的返回内容为：', self.responseEn.text)
        if regXml.search(self.responseEn.text) != None:
            contentCode = regXml.search(self.responseEn.text).group(1)
        else:
            contentCode = None

        self.assertEqual(self.responseEn.status_code, 200)
        if contentCode == None:
            print('页面没有404状态码，测试通过')
        else:
            contentCode = regXml.search(self.responseEn.text).group(1)
            print('code=', contentCode)
            self.assertNotEqual(int(contentCode), 404)
            print('页面有404错误')

    def tearDown(self):
        pass


