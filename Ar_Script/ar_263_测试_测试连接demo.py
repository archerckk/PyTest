import requests
import unittest
import Selenium2Library

requestBody=requests.get('http://www.baidu.com')
try:
    assert requestBody.status_code==200
    print('���Գɹ�')
except AssertionError:
    print('����ʧ��')