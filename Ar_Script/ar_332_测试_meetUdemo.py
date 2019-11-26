import unittest
import requests
import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s')

class TestDemo(unittest.TestCase):
    def setUp(self) -> None:
        environment = 'test'
        if environment == 'test':
            self.host = 'http://150.109.38.68'
        elif environment == 'normal':
            self.host = 'http://www.meetuapp.info'

    def test_update_profile(self):
        headers = {
             "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjE1NTJlNzBmMTY5ZGQ5OWI0MWYzNmQ3OTE4ZDQ5YzZiYzNiYjE2MzZhZjE3OGM1NzBkMDFhOTZkYmNkNGZjODViZmQ5ZTVmMGEyNjU3YTY3In0.eyJhdWQiOiIyIiwianRpIjoiMTU1MmU3MGYxNjlkZDk5YjQxZjM2ZDc5MThkNDljNmJjM2JiMTYzNmFmMTc4YzU3MGQwMWE5NmRiY2Q0ZmM4NWJmZDllNWYwYTI2NTdhNjciLCJpYXQiOjE1NzQ3MjQyMTksIm5iZiI6MTU3NDcyNDIxOSwiZXhwIjoxNTc2MDIwMjE5LCJzdWIiOiI0MjMiLCJzY29wZXMiOltdfQ.oj0zj3H6wLqiG2_juT0KiOLXATy5yWj9IWsD9j1q-QH-EVq196Rx9rWw8HRVSO7__X3-2k2U2e0ykgpOdRClPe03D3dngqVnmQmCRPUPs23q19yuWzOnmpurFVLWwpt5_PiYHrVa91JSq5HboA6QSwdafX6iM2cuRwsjXZ4xzzcj29tqIgtIXblGwzc7QejWN4KdnW13sHUOMnzJVK5XU7AMNmk7NGPolgbIphoW5Zi2JwLyQdt4h9w61hs9eEUFfqXifOGdfpmT67vK-0Me56UPQQ6nIm0QlJVDHooTYYS7z9iykzmHYTutfo4_ETrI76TDi3m2tCF2gEtBUEnyf4GwrYd-4KYTeh0BDSEQwwPo6fi-TnwBVzAWpQGTArXrOll0MMvIYXoEgMlRKN-JT6fRm0ghPmfFry8tz02jaAdm45348jxf6u5vsXFMkW0OM8fgOdpZ5VLUrsV_RpJlGZs8qaKlJsXOG_yHcuZ2paO5cshz5POIgH0wf6IAqguMsjg38L8u0OqL824R1BPS1yR-Y8uEf_HhngcOqK5jeNs9ua1qLYpZQSp1Llvjdk1E3VpApLCInJLcGqxLemPJZEUcdQ7CBvxaEVRP7ijJgDMhTQZi_FQdhjWxwRgoZn2fGGxWQ3DFJ9a3vSu5-hKgq8Lbhc1nBhFBFUZl9VEiAhA",
             "Host": "150.109.38.68",
             "Connection": "Keep-Alive",
             "Accept-Encoding": "gzip",
             "User-Agent": "okhttp/3.12.0",
             "X-Requested-With": "XMLHttpRequest"
        }

        # data={
        #     "block_id": "385",
        #     "status": "block"
        # }

        url = '{}/api/user/match_list/429'.format(self.host)

        response=requests.get(url,headers=headers)

        result_json = response.json()

        logging.debug('返回内容为：{}'.format(result_json))

        self.assertEqual(result_json['message'],'success')
        self.assertEqual(result_json['status'],True)
        self.assertTrue(result_json['data'] is not None)
        # logging.debug('提示信息：{}'.format(result_json['message']))