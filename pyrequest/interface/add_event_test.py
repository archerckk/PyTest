import unittest
import requests
import os,sys
parentdir= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
from db_fixture import test_data
import time


def get_time():
    now=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    return now


class AddEventTest(unittest.TestCase):
    '''添加发布会'''

    def setUp(self):
        self.base_url='http://127.0.0.1:8000/api/add_event/'

    def tearDown(self):
        print(self.result)

    def test_add_event_all_null(self):
        '''所有参数为空'''
        pyload={'eid':'','limit':'','address':'','start_time':''}
        r=requests.post(self.base_url,data=pyload)
        self.result=r.json()
        self.assertEqual(self.result['status'],10021)
        self.assertEqual(self.result['message'],'parameter error')

    def test_add_event_eid_exist(self):
        pyload = {'eid': '1', 'name':'红米发布会XXXX','limit': '2000', 'address': '北京水立方',
                  'start_time': get_time()}
        r = requests.post(self.base_url, data=pyload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10022)
        self.assertEqual(self.result['message'], 'event id already exists')

    def test_add_event_name_exist(self):
        pyload = {'eid': '9', 'name':'红米pro发布会','limit': '2000', 'address': '北京水立方',
                  'start_time': get_time()}
        r = requests.post(self.base_url, data=pyload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10023)
        self.assertEqual(self.result['message'], 'event name already exists')

    def test_add_event_data_type_error(self):
        pyload = {'eid': '999', 'name':'红米pro发布会XXX','limit': '2000', 'address': '北京水立方',
                  'start_time': '1999'}
        r = requests.post(self.base_url, data=pyload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10024)
        self.assertIn('start_time format error.', self.result['message'])

if __name__ == '__main__':
    test_data.init_data()
    unittest.main()