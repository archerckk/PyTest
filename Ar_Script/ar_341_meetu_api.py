import unittest
import requests
from ddt import ddt,data,unpack
import logging
import allure
import pytest

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s')

environment = 'test'

if environment == 'test':
    host = 'http://150.109.38.68'
    token='Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjVkODM0MTc1N2VjZjIyZjQ5OTAzNDc0NjFjOTFmZGIxZmQwYmJiNTg2NWJiNWU0MDZmZTEyMzdlMGIwYTBkMjc1ZDA5YWMyZGE4YjAwMTc0In0.eyJhdWQiOiIyIiwianRpIjoiNWQ4MzQxNzU3ZWNmMjJmNDk5MDM0NzQ2MWM5MWZkYjFmZDBiYmI1ODY1YmI1ZTQwNmZlMTIzN2UwYjBhMGQyNzVkMDlhYzJkYThiMDAxNzQiLCJpYXQiOjE1NzUwMjM3ODUsIm5iZiI6MTU3NTAyMzc4NSwiZXhwIjoxNTc2MzE5Nzg1LCJzdWIiOiI0MjMiLCJzY29wZXMiOltdfQ.C4k3UjIoYa6moWxJjjp9mraBzsugEFBl92j5FiEmwn_fJQHkfPoWyteGy4uSr4N0erFKGIErNzhY0R4WK4F1WpvKzekNSYsIGIeX47cVzb4UXSJzd7MQ7uqVJL3_miRAu0e-Ofm9vcCq_hqtuX6wbpQsSdvvKosBAETtfnutjkAQc-rJALvG2KR2tr90fnXbgCSE_voxieOWrQUgnBIR_KvUL9cZ6E-RrtkoHYei7Kp41B-QBMmg48aXsKz9wjvLG3DJNXQnIlwJjBdAa3hTk0s-HPzTB4cih8hGcTUcFfRY5AI7J98SI-777jJ6q4ECBO88LfOcgVy6IWOCXcMQDXlT7KZ9silx2z2CkWvuSuR-3qTOV1Gi2FW3pIpbgQkIJUx48i-Lk01i14NXegxfT4lr9yp7MOiz6IlEL9GmytWP6X_dvroh_EzZunOcH_hp0C6Mo_txwM5m5NJ7qbEAGrPbuPKPrIlYmwA6AMpudp42mSryYMEClccwaXrt0EZiVC3QZkJaIQYyFkXb9YPRCyRaFZMML1ykUxKyXzWCe5Iw0-eewx6kDLxKpyn3l2NEC6QIGW5b_LjyIIlcBVGgJHOEkJTkE1kX6lhdrt76GPS-_RcMckvga6DTLvsla2DCgYkMYGxQ9mF57gKQqoM5-9jRDxVMpn9essDCdE7hI7s'
elif environment == 'normal':
    host = 'http://www.meetuapp.info'
    token='Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImY3NGEzNTUwMTdkYjhkODBiOWMyMzFkNDhhMTc4ZDI1YjE5NTc2YzlkMGQ2ZDJkNWU0Nzk3MmQzMzgzYmNiYzQzYzdkNTgzMmVkYTBiZGFkIn0.eyJhdWQiOiIxIiwianRpIjoiZjc0YTM1NTAxN2RiOGQ4MGI5YzIzMWQ0OGExNzhkMjViMTk1NzZjOWQwZDZkMmQ1ZTQ3OTcyZDMzODNiY2JjNDNjN2Q1ODMyZWRhMGJkYWQiLCJpYXQiOjE1NzQ4NTc2MDgsIm5iZiI6MTU3NDg1NzYwOCwiZXhwIjoxNjA2NDgwMDA4LCJzdWIiOiI2MiIsInNjb3BlcyI6W119.fj92n_Rl1w_dG985eH6sv4YbqG1cccu3Rv0-GDhgsJ3bwmBT3gLamNHYNyw9RYXvezrIhIhgSvXrVffiVUTFnC6tWcG6_tMF2Hl5Xa8n-6qz4Bm0j-gJx5SJie8UDjzwTaSu6UP2tC8JL3uuq5fL_Pf35OPaOaHBjBoM6qP-iskUd3qQwyWw-c1eNQfK-Yrz-0iZSOGGYRHvR3DWh4GIAbVr7CAkBNElJ0vjAMxAJowda5et3_eQ0yHLwLRi3AiAImX7Qk_3dzPOoqE9UFqHMUrGiJUoVVvIOiVAeWq1LxrXninCRuTNEmfWmu915CF7suc79rS_avj-ZED1VlOYzUwhQhgxzHwnhpsBTvK5rkTciqwVkxiP9pxP1SnOKHxzJPd3-8yNCKM03QXpsKUGqzSQgHVkYFJODYoWgy7wZlLIoOWk5zWbN2r5EKWXdJQrcxW3skwLuoOxyipVNlaQgLAdKGrNH7ZT2KO82SnRUUluJoMWV-yzjOhsGmldMjAdpT_6OoMxhydQfWzg4WpBqvYeFCSO6M2QNZuSCTEtdw8OFNGTwmekW8xiu7bv1lAQ5JsvQr11_LziDrBSne-fyCnwDHaod0YeS8hp2xNdiPO7298Rz2LLQOP28KtK8X5TeA6Fv155YE9KblilCyz49Cc90eyE1K1ZAscERRyEwAU'



# @ddt
# @allure.feature('MeetU接口测试')
class Test_meetU_API:

    @pytest.fixture()
    def setup(self):
        pass
    @pytest.fixture()
    def teardown(self):
        pass



    @allure.story('谁喜欢我人数统计接口')
    # @data(
    #     token,
    #     '',
    #     '123'
    # )
    @pytest.mark.parametrize('value',[token,'','123'])
    def test_who_likes_me_count(self,value):
        '谁喜欢我人数统计'
        #构造header部分
        headers={
        "Authorization":value,
        # "Host": "150.109.38.68",
        "Connection": "Keep - Alive",
        "Accept - Encoding": "gzip",
        "User - Agent": "okhttp / 3.12.0",
        "X - Requested - With": "XMLHttpRequest",
        }

        url='{}/api/user/who_likes_me_count'.format(host)

        response=requests.get(url,headers=headers)
        content=response.text
        # logging.debug('返回内容为：{}'.format(content))

        if value=='' or value=='123':
            logging.debug('无效参数传输，token值为：{}'.format(value))
            assert 'Login to Your Account'in content
            logging.debug('Login to Your Account in json result')
        else:

            assert 'likes_me_count'in content
            assert response.status_code==200
            assert '"code":200'in content


    def test_user_app(self):
        logging.debug('用户信息获取接口_user /user_app测试开始')
        headers={
        "Authorization": token,
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": "74",
        # "Host": "150.109.38.68",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "User-Agent": "okhttp/3.12.0",
         "X-Requested-With": "XMLHttpRequest"
        }

        data={
         "country_code": "cn",
         "version_name": "1.0.1.1122",
         "version_code": "1",
         "lang": "zh",
         "platform": "gp"
        }

        url='{}/api/user/user_app'.format(host)

        responese=requests.post(url,headers=headers,data=data)

        result=responese.text
        logging.debug('返回内容为：{}'.format(result))

        self.assertTrue('"message":"success"'in result)
        self.assertTrue('"user_id":423' in result)

    @data(
        token,
        '',
        '123'
    )
    def test_update_setting(self,value):
        '配置获取接口'
        # 构造header部分
        headers = {
            "Authorization": value,
            # "Host": "150.109.38.68",
            "Connection": "Keep - Alive",
            "Accept - Encoding": "gzip",
            "User - Agent": "okhttp / 3.12.0",
            "X - Requested - With": "XMLHttpRequest",
        }

        url = '{}/api/user/get_setting'.format(host)

        response = requests.get(url, headers=headers)

        content = response.text

        if value == '' or value == '123':
            self.assertTrue('Login to Your Account' in content)
        else:
            result_json = response.json()
            self.assertTrue(result_json['user_id']is not None)

            self.assertTrue(result_json['gender']is not None)

            #年龄返回检查
            self.assertTrue(result_json['age_limit']!='')

            self.assertTrue(int(result_json['age_limit'].split(',')[0])in range(18,101))
            self.assertTrue(int(result_json['age_limit'].split(',')[1])in range(18,101))


            self.assertTrue(result_json['latitude'] is not None)
            self.assertTrue(result_json['longitude']  is not None)

            self.assertTrue(result_json['created_at'] is not None)
            self.assertTrue(result_json['updated_at'] is not None)

    @data( '1','0')
    def test_find_match(self,value):
        '匹配卡片下发'
        #vip状态无法识别的时候会持续loading
        headers={
            "Authorization":token,
            "Content-Type": "application/x-www-form-urlencoded",
            "Content-Length": "5",
            # "Host": "150.109.38.68",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttp/3.12.0",
            "X-Requested-With": "XMLHttpRequest"
        }

        url='{}/api/user/find_match'.format(host)

        data={'vip':value}

        response=requests.post(url,headers=headers,data=data)
        result_json=response.json()

        logging.debug(response.text)
        logging.debug("卡片的剩余数为：{}".format(result_json['remain_amount']))
        self.assertTrue(isinstance(result_json['remain_amount'],int),True)

    @data(
        token,
        '123',
        ''
    )
    def test_get_profile(self,value):
        '获取用户信息'
        headers={
            "Authorization":value,
            "Content-Type": "application/x-www-form-urlencoded",
            "Content-Length": "5",
            # "Host": "150.109.38.68",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttp/3.12.0",
            "X-Requested-With": "XMLHttpRequest"
        }

        data={
            'device_token':"fW9SjEZW7BM%3AAPA91bFx4qQMD9mhheKv0b9WcCiviVRjkLbmWmTsqb8_9rrJGoJqWhLuuKOJia6hny-FQxgRMeMKbqMsr_VAC_WzSFIlv26YAcLtk1KWwfjhxwyWJVJNXqg5yqOFX_xb-qnbfOEaYFkH "
        }

        url='{}/api/user/get_profile'.format(host)
        response=requests.get(url,headers=headers,data=data)
        result_json=response.json()

        logging.debug(result_json)

        if value=='123' or value=='':
            self.assertEqual(result_json['error'],'Unauthenticated.')
        else:
            self.assertTrue(result_json['user']['id']==423)

    @data(
        token,
        '123',
        ''
    )
    def test_match_list(self,value):
        '获取发过消息用户列表'

        headers = {
         "Authorization": value,
         # "Host": "150.109.38.68",
         "Connection": "Keep-Alive",
         "Accept-Encoding": "gzip",
         "User-Agent": "okhttp/3.12.0",
         "X-Requested-With": "XMLHttpRequest"
        }

        url='{}/api/user/match_list'.format(host)

        response = requests.get(url, headers=headers)

        result_json = response.json()

        logging.debug(result_json)

        if value == '123' or value == '':
            self.assertEqual(result_json['error'], 'Unauthenticated.')
        else:
            self.assertTrue(result_json[0]['user_id'] == 423)

    @data(
        token,
        '123',
        ''
    )
    def test_update_online_state(self, value):
        '用户是否在线状态更新'

        headers = {
            "Authorization": value,
            # "Host": "150.109.38.68",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttp/3.12.0",
            "X-Requested-With": "XMLHttpRequest"
        }

        url = '{}/api/user/update_online_state'.format(host)

        response = requests.post(url, headers=headers)

        result_json = response.json()

        logging.debug(result_json)

        if value == '123' or value == '':
            self.assertEqual(result_json['error'], 'Unauthenticated.')
        else:
            self.assertTrue(result_json['message'] == 'update_online_state_success')

    @data(
        token,
        '123',
        ''
    )
    def test_all_matchs(self, value):
        '查看互相喜欢用户'

        headers = {
            "Authorization": value,
            "Content-Length": "0",
            # "Host": "150.109.38.68",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttp/3.12.0",
            "X-Requested-With": "XMLHttpRequest"
        }

        url = '{}/api/user/all_matchs'.format(host)

        response = requests.post(url, headers=headers)

        result_json = response.json()

        logging.debug(result_json)

        if value == '123' or value == '':
            self.assertEqual(result_json['error'], 'Unauthenticated.')
        else:
            self.assertTrue('list'in result_json['data'])
            self.assertTrue('total'in result_json['data'])

    @data(
        ( token,1),
        ( token,0),
        ('123',0),
        ('',0)
    )
    @unpack
    def test_instant_match(self, value,vip):
        '即时匹配'

        headers = {
            "Authorization": value,
            "Content-Type": "application/x-www-form-urlencoded",
            "Content-Length": "5",
            # "Host": "150.109.38.68",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttp/3.12.0",
            "X-Requested-With": "XMLHttpRequest"
        }

        data={'vip':vip}

        url = '{}/api/user/instant_match'.format(host)

        response = requests.post(url, headers=headers,data=data)

        result_json = response.json()

        logging.debug(result_json)

        if value == '123' or value == '':
            self.assertEqual(result_json['error'], 'Unauthenticated.')
        else:
            logging.debug(result_json['instantMatchCount'])
            logging.debug(result_json['surplusMatchCount'])
            self.assertTrue(result_json['instantMatchCount']is not None)
            self.assertTrue(result_json['surplusMatchCount']is not None)
            self.assertTrue(result_json['code']==200)
            self.assertTrue(result_json['message']=='User instantMatch successfully')

    # def test_send_email_code(self):
    #     ' 发送邮箱验证码（注册、忘记密码）'
    #
    #     headers = {
    #         "Accept": "application/json",
    #     }
    #
    #     data={
    #         "email": "archerckkbin@gmail.com",
    #         "operation": "setEmail"
    #           }
    #
    #     url = '{}/api/user/send_email_code'.format(host)
    #
    #     response = requests.post(url, headers=headers,data=data)
    #
    #     result_json = response.json()
    #
    #     logging.debug(result_json)
    #
    #
    #     self.assertEqual(result_json['status'],True)
    #     self.assertTrue(result_json['code']==200)
    #     self.assertTrue(result_json['data']['email']is not None)



    def test_getNationalCity(self):
        '获取国际城市'

        headers = {
            "Accept": "application/json",
        }

        # data={
        #     # "email": "archerckkbin@gmail.com",
        #     # "operation": "setEmail"
        #       }

        url = '{}/api/user/getNationalCity'.format(host)

        response = requests.post(url, headers=headers)

        result_json = response.json()

        logging.debug(result_json)


        self.assertEqual(result_json[0]['name'],'Singapore')
        self.assertEqual(result_json[1]['name'],'United Kingdom')
        self.assertEqual(result_json[2]['name'],'United States')

    def test_update_profile(self):
        headers = {
            "Authorization":token,
             "Content-Type": "application/x-www-form-urlencoded",
             "Content-Length": "246",
             # "Host": "150.109.38.68",
             "Connection": "Keep-Alive",
             "Accept-Encoding": "gzip",
             "User-Agent": "okhttp/3.12.0",
             "X-Requested-With": "XMLHttpRequest"
        }

        data={
            "interest": "11,14,1,12,8,4,5,13,2,10,9,3",
            "industry_id": "1",
            "country": "Singapore",
            "username": "6qq",
            "longitude": "113.3684076",
            "dob": "11/25/2001",
            "city": "Singapore",
            "latitude": "23.1216899",
            "about": "ppp",
            "countrycode": "2987",
            "province": "",
            "provincecode": "0",
            "citycode": "2987"
        }

        url = '{}/api/user/user_app'.format(host)

        response=requests.post(url,headers=headers,data=data)

        result_json = response.json()

        logging.debug('返回内容为：{}'.format(result_json))

        self.assertEqual(result_json['message'],'success')

    def test_user_block(self):
        '添加黑名单'
        headers = {
            "Authorization":token,
            "Content-Type": "application/x-www-form-urlencoded",
            "Content-Length": "25",
            # "Host": "150.109.38.68",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttp/3.12.0",
            "X-Requested-With": "XMLHttpRequest"
        }

        data = {
            "block_id": "385",
            "status": "block"
        }

        url = '{}/api/user/user_block'.format(host)

        response = requests.post(url, headers=headers, data=data)

        result_json = response.json()

        logging.debug('返回内容为：{}'.format(result_json))

        self.assertEqual(result_json['code'], 200)
        self.assertEqual(result_json['status'], True)
        logging.debug('提示信息：{}'.format(result_json['message']))

    def test_match_list_429(self):
        '匹配小红点状态修改接口'

        headers = {
            "Authorization":token,
            # "Host": "150.109.38.68",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttp/3.12.0",
            "X-Requested-With": "XMLHttpRequest"
        }

        url = '{}/api/user/match_list/429'.format(host)

        response = requests.get(url, headers=headers)

        result_json = response.json()

        logging.debug('返回内容为：{}'.format(result_json))

        self.assertTrue(result_json['message']is not None)
        self.assertTrue(result_json['status']is not None)
        # self.assertTrue(result_json['data'] is not None)

    @data(1,3)
    def test_likes(self,value):
        '滑动卡片发送喜欢或者不喜欢状态'

        headers = {
            "Authorization": token,
            "Content-Type": "application/x-www-form-urlencoded",
            "Content-Length": "20",
            "Host": "150.109.38.68",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttp/3.12.0",
            "X-Requested-With": "XMLHttpRequest"
        }

        data = {
            "like_id": "429",
            "status": value
        }

        url = '{}/api/user/likes'.format(host)

        response = requests.post(url, headers=headers, data=data)
        # logging.debug(response.text())
        result_json = response.json()

        logging.debug('返回内容为：{}'.format(result_json))

        if result_json['message']=='request times used up':
            logging.debug('卡片测试次数用完了')
        else:
            if value==3:
                self.assertEqual(result_json['status'],'DISLIKED')
                self.assertEqual(result_json['statuscode'],3)
                self.assertEqual(result_json['message'] ,'User disliked successfully')
            elif value==1:
                self.assertEqual(result_json['status'], 'LIKED')
                self.assertEqual(result_json['statuscode'], 1)
                self.assertEqual(result_json['message'], 'User liked successfully')


if __name__ == '__main__':
    pytest.main(' -s ./ar_341_meetu_api.py::Test_meetU_API::test_who_likes_me_count')