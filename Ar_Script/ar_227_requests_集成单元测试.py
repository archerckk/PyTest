import requests
import unittest

class Get_Event_list(unittest.TestCase):

    def setUp(self):
        self.url='http://127.0.0.1:8000/api/get_event_list/'

    def test_eid_null(self):
        r=requests.get(self.url,params={'eid':''})
        result=r.json()
        self.assertEqual(result['status'],10021)
        self.assertEqual(result['message'],'parameter error')

    def test_eid_error(self):
        r = requests.get(self.url, params={'eid': '999'})
        result = r.json()
        self.assertEqual(result['status'], 10022)
        self.assertEqual(result['message'], 'query result is empty')

    def test_eid_success(self):
        r = requests.get(self.url, params={'eid': '1'})
        result = r.json()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'success')
        self.assertEqual(result['data']['name'],'1+手机发布会')
        self.assertEqual(result['data']['address'],'北京水立方')


if __name__ == '__main__':
    unittest.main()