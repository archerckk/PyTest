import unittest
import requests
from ddt import ddt,data,unpack
import logging
import allure
import pytest

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(levelname)s %(message)s')

environment = 'normal'

if environment == 'test':
    host = 'http://150.109.38.68'
    token='Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjBiNTEzNjVkZjhhZjlmNWI0MWYxMmI0MDQ2NmFhMTY2M2QyMjAxNjE2Mjc2ODVmNTkxMWE4OTNmMzNkZDVlNGI4ZjFjNjNjYmY3ZjA1MWIzIn0.eyJhdWQiOiIxIiwianRpIjoiMGI1MTM2NWRmOGFmOWY1YjQxZjEyYjQwNDY2YWExNjYzZDIyMDE2MTYyNzY4NWY1OTExYTg5M2YzM2RkNWU0YjhmMWM2M2NiZjdmMDUxYjMiLCJpYXQiOjE1Nzc2OTYxNDgsIm5iZiI6MTU3NzY5NjE0OCwiZXhwIjoxNjA5MzE4NTQ4LCJzdWIiOiI3MjgiLCJzY29wZXMiOltdfQ.ZFPe-vWCLgqAfvjcHTHwlBCFHtdB4dBfz_9NNYgBzEPhN5bCTEeLzPgUViG75g2JA9xZndGmHXa6j8FXymmV7UG2XyQwINvc5l68E5K9y2ozikUTNRLTKoloaNK0d5p0nb2fWN6AgRdgdppsRFT_CrJcvcql5kcMzQektHCld3CX8DP41inB-NxdHTSFO4EPF6lHaKIjYGVz9j5coxP6yPaoSZ6aZaY4SMrXVxO5_RQlRyPgfrhfhVOTl0zyY13r8QF1mlMHKqGiK8FsXdVaC3uSWNLFTqDYI83VtPwiWJlrCGkL1d1mxwUC-mAgns49GdlPrISZWNNi8ZWHogs8kn07jPTOK5_fuYIDJM_tXCjzOc3iYkAVRxvydALgV1e9DtW6oRXwuJnAwsTKhVFq5VfgGleAcY0Yx4fFDoq-SztARPOVqGrJzmbMQINR-16FY3FsxJbXHEAm3pNp5isNeIjEt3r8hwX-9iLZQCyWK4a2OEmfpaHbAbS6a_Tw616lpqFvrtCjulUg0lZpfMo4DyIX_RLbC01QHYmLb3td8iCaJmyZicTsGaU-e4f7MzbxdkuiMmFbrUEsMzhlr45uCX6o19BNPSVSVfUsLmJU8t2CKDncpzXmThSYazF4QbB6nt9LUVQy41GTx5k_lIGS9fSMUmGzj-GQpHw8H0nsu1E'
    remain_test_token='Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImM0NjU3YTI2ZDRiYWFjZTdiMTNiMjg3NmI4NmJiMjAwMDU1YzUxOWQ2YzM1M2IxY2Y1NGRhOTA3ZGRhNThlYjkxYTEyMGFkZWZiZWUwNjBkIn0.eyJhdWQiOiIxIiwianRpIjoiYzQ2NTdhMjZkNGJhYWNlN2IxM2IyODc2Yjg2YmIyMDAwNTVjNTE5ZDZjMzUzYjFjZjU0ZGE5MDdkZGE1OGViOTFhMTIwYWRlZmJlZTA2MGQiLCJpYXQiOjE1Nzc3ODU2MDAsIm5iZiI6MTU3Nzc4NTYwMCwiZXhwIjoxNjA5NDA4MDAwLCJzdWIiOiI3NDUiLCJzY29wZXMiOltdfQ.i59VkkDGna6OhbNOYhk5_ZRGjx41IbiEgQEZ8qM7_5dLb2w895tMU1avsFWUMCQ4ETPLJeJXV-PFSzagbFzfVliTwj8xdUPyxddbvzFzpbkI19RlKjMXmlbPIk9KoxOyMnmzJGBy-TQFOMQ0PbQfS9t1Lv0L_3Z1LvxaIT1QZTfc69BoP1OpuCFiGvu55DOSpA_6Wefp85qug93ORnW6qFNBI3gqAGEiCduVyIbqSixBMuaDwmusFUswroGrV9e2Qtz8PSK5IexyAGDM1P7Yts5uASiKG61uX6C793rSmp8Qq2_3UPjlQ2iyML4XSKpfJLg0tFevZMZtMOzBR7cMsSrFsMQJxZVdyZCb6FNOuMKqRe1ZMnU2N23WlbNKWoPhuOwmQTO8a0tbgYgg-TrGo1se6Azise0Aw-T6NkukHGbuUcJKJNBzI7F3br86fhBN4tE1uI9KzXjzA7inKwyB_ew3nqQLDw_r-OnjDTnoPZ3sxVWltZAHI1AWbUhk_x9mgxgyLtw83Tgg89o6A8fcYGCPK59BRj-RR2RwoMjJDVEnVcnMa3-lQ69SHGn2R6dXwM3pPEtohPtAzPRIwYu9FwG73gnqZd2cjzy3JIfPWLMEnDE9jAOc2tzqqpQTirs0h3TYG9pFh77xlLiNEWDJAiU_aHWquiXbI5-Pb5odLfo'
elif environment == 'normal':
    host = 'http://www.meetuapp.info'
    token='Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImY3NGEzNTUwMTdkYjhkODBiOWMyMzFkNDhhMTc4ZDI1YjE5NTc2YzlkMGQ2ZDJkNWU0Nzk3MmQzMzgzYmNiYzQzYzdkNTgzMmVkYTBiZGFkIn0.eyJhdWQiOiIxIiwianRpIjoiZjc0YTM1NTAxN2RiOGQ4MGI5YzIzMWQ0OGExNzhkMjViMTk1NzZjOWQwZDZkMmQ1ZTQ3OTcyZDMzODNiY2JjNDNjN2Q1ODMyZWRhMGJkYWQiLCJpYXQiOjE1NzQ4NTc2MDgsIm5iZiI6MTU3NDg1NzYwOCwiZXhwIjoxNjA2NDgwMDA4LCJzdWIiOiI2MiIsInNjb3BlcyI6W119.fj92n_Rl1w_dG985eH6sv4YbqG1cccu3Rv0-GDhgsJ3bwmBT3gLamNHYNyw9RYXvezrIhIhgSvXrVffiVUTFnC6tWcG6_tMF2Hl5Xa8n-6qz4Bm0j-gJx5SJie8UDjzwTaSu6UP2tC8JL3uuq5fL_Pf35OPaOaHBjBoM6qP-iskUd3qQwyWw-c1eNQfK-Yrz-0iZSOGGYRHvR3DWh4GIAbVr7CAkBNElJ0vjAMxAJowda5et3_eQ0yHLwLRi3AiAImX7Qk_3dzPOoqE9UFqHMUrGiJUoVVvIOiVAeWq1LxrXninCRuTNEmfWmu915CF7suc79rS_avj-ZED1VlOYzUwhQhgxzHwnhpsBTvK5rkTciqwVkxiP9pxP1SnOKHxzJPd3-8yNCKM03QXpsKUGqzSQgHVkYFJODYoWgy7wZlLIoOWk5zWbN2r5EKWXdJQrcxW3skwLuoOxyipVNlaQgLAdKGrNH7ZT2KO82SnRUUluJoMWV-yzjOhsGmldMjAdpT_6OoMxhydQfWzg4WpBqvYeFCSO6M2QNZuSCTEtdw8OFNGTwmekW8xiu7bv1lAQ5JsvQr11_LziDrBSne-fyCnwDHaod0YeS8hp2xNdiPO7298Rz2LLQOP28KtK8X5TeA6Fv155YE9KblilCyz49Cc90eyE1K1ZAscERRyEwAU'
    remain_test_token='Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImY3NGEzNTUwMTdkYjhkODBiOWMyMzFkNDhhMTc4ZDI1YjE5NTc2YzlkMGQ2ZDJkNWU0Nzk3MmQzMzgzYmNiYzQzYzdkNTgzMmVkYTBiZGFkIn0.eyJhdWQiOiIxIiwianRpIjoiZjc0YTM1NTAxN2RiOGQ4MGI5YzIzMWQ0OGExNzhkMjViMTk1NzZjOWQwZDZkMmQ1ZTQ3OTcyZDMzODNiY2JjNDNjN2Q1ODMyZWRhMGJkYWQiLCJpYXQiOjE1NzQ4NTc2MDgsIm5iZiI6MTU3NDg1NzYwOCwiZXhwIjoxNjA2NDgwMDA4LCJzdWIiOiI2MiIsInNjb3BlcyI6W119.fj92n_Rl1w_dG985eH6sv4YbqG1cccu3Rv0-GDhgsJ3bwmBT3gLamNHYNyw9RYXvezrIhIhgSvXrVffiVUTFnC6tWcG6_tMF2Hl5Xa8n-6qz4Bm0j-gJx5SJie8UDjzwTaSu6UP2tC8JL3uuq5fL_Pf35OPaOaHBjBoM6qP-iskUd3qQwyWw-c1eNQfK-Yrz-0iZSOGGYRHvR3DWh4GIAbVr7CAkBNElJ0vjAMxAJowda5et3_eQ0yHLwLRi3AiAImX7Qk_3dzPOoqE9UFqHMUrGiJUoVVvIOiVAeWq1LxrXninCRuTNEmfWmu915CF7suc79rS_avj-ZED1VlOYzUwhQhgxzHwnhpsBTvK5rkTciqwVkxiP9pxP1SnOKHxzJPd3-8yNCKM03QXpsKUGqzSQgHVkYFJODYoWgy7wZlLIoOWk5zWbN2r5EKWXdJQrcxW3skwLuoOxyipVNlaQgLAdKGrNH7ZT2KO82SnRUUluJoMWV-yzjOhsGmldMjAdpT_6OoMxhydQfWzg4WpBqvYeFCSO6M2QNZuSCTEtdw8OFNGTwmekW8xiu7bv1lAQ5JsvQr11_LziDrBSne-fyCnwDHaod0YeS8hp2xNdiPO7298Rz2LLQOP28KtK8X5TeA6Fv155YE9KblilCyz49Cc90eyE1K1ZAscERRyEwAU'



# @ddt
# @allure.feature('MeetU接口测试')
class Test_meetU_API:

    @pytest.fixture()
    def setup(self):
        pass
    @pytest.fixture()
    def teardown(self):
        pass

    def login_require(self,result_json,value):
        logging.debug('传入异常token，验证接口需要登录才能使用')
        logging.debug('无效参数传输，token值为：{}'.format(value))
        assert 'Unauthenticated' in result_json['error']
        logging.debug(result_json)


    @allure.story('谁喜欢我人数统计接口')
    @pytest.mark.parametrize('value',[token,'','123'])
    def test_who_likes_me_count(self,value):
        #构造header部分
        headers={
        "Authorization":value,
        "Connection": "Keep - Alive",
        "Accept - Encoding": "gzip",
        "User - Agent": "okhttp / 3.12.0",
        "X - Requested - With": "XMLHttpRequest",
        }

        url='{}/api/user/who_likes_me_count'.format(host)
        response=requests.get(url,headers=headers)
        content=response.text
        logging.debug(content)
        # logging.debug('返回内容为：{}'.format(content))

        if value=='' or value=='123':
            logging.debug('传入异常token，验证接口需要登录才能使用')
            logging.debug('无效参数传输，token值为：{}'.format(value))
            assert 'Login to Your Account' in content
            logging.debug(content)
        else:
            content=response.json()
            assert 'likes_me_count'in content
            logging.debug('喜欢我的人数为：{}'.format(content['likes_me_count']))
            assert response.status_code==200
            assert content['code']==200
            assert content['status']==True

    @allure.story('用户信息获取接口测试')
    @pytest.mark.parametrize('value', [token, '', '123'])
    def test_user_app(self,value):
        logging.debug('用户信息获取接口_user /user_app测试开始')
        headers={
        "Authorization": value,
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

        if value==token:
            logging.debug('返回内容为：{}'.format(result))

            assert '"message":"success"'in result
            assert '"user_id":728' in result
        else:
            logging.debug('传入异常token，验证接口需要登录才能使用')
            logging.debug('无效参数传输，token值为：{}'.format(value))
            assert 'Unauthenticated' in result
            logging.debug(result)

    @allure.story('配置获取接口接口测试')
    @pytest.mark.parametrize('value', [token, '', '123'])
    def test_update_setting(self,value):
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
            assert ('Login to Your Account' in content)
        else:
            result_json = response.json()
            assert(result_json['user_id']is not None)

            assert(result_json['gender']is not None)
            logging.debug('user_id返回为：{}'.format(result_json['user_id']))
            logging.debug('gender返回为：{}'.format(result_json['gender']))


            #年龄返回检查
            assert(result_json['age_limit']!='')
            logging.debug('年龄限制返回为：{}'.format(result_json['age_limit']))

            assert(int(result_json['age_limit'].split(',')[0])in range(18,101))
            assert(int(result_json['age_limit'].split(',')[1])in range(18,101))
            logging.debug('年龄最小值跟最大值返回正常')

            assert(result_json['latitude'] is not None)
            assert(result_json['longitude']  is not None)
            logging.debug('经纬度返回正常{}{}'.format(result_json['latitude'],result_json['longitude']))

            assert(result_json['created_at'] is not None)
            assert(result_json['updated_at'] is not None)


    @allure.story('匹配卡片下发')
    @pytest.mark.parametrize('value,vip', [(remain_test_token,0),
                                           (remain_test_token,1),
                                            ('',0),
                                            ('123',0)])
    def test_find_match(self,value,vip):
        #vip状态无法识别的时候会持续loading
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

        url='{}/api/user/find_match'.format(host)

        data={'vip':vip}

        response=requests.post(url,headers=headers,data=data)
        result_json=response.json()


        logging.debug(response.text)
        if value==remain_test_token:
            if vip==1:
                assert result_json['remain_amount']==30
                logging.debug('vip用户下发的卡片数量为30')
            elif vip==0:
                assert result_json['remain_amount'] == 15
                logging.debug('普通用户下发的卡片数量为15')
            logging.debug("卡片的剩余数为：{}".format(result_json['remain_amount']))
        else:
            assert result_json['error']=='Unauthenticated.'

    @allure.story('获取用户信息接口测试')
    @pytest.mark.parametrize('value', [token, '', '123'])
    def test_get_profile(self,value):
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
            assert (result_json['error'],'Unauthenticated.')
        else:
            assert(result_json['user']['id']==728)

    @allure.story('获取发过消息用户列表接口测试')
    @pytest.mark.parametrize('value', [token, '', '123'])
    def test_match_list(self,value):
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
            assert (result_json['error'], 'Unauthenticated.')
        else:
            assert(result_json[0]['user_id'] == 728)

    @allure.story('用户是否在线状态更新接口测试')
    @pytest.mark.parametrize('value', [token, '', '123'])
    def test_update_online_state(self, value):
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
            assert(result_json['error'], 'Unauthenticated.')
        else:
            assert(result_json['message'] == 'update_online_state_success')
            logging.debug("更新状态信息结果为：{}".format(result_json['message']))

    @allure.story('查看互相喜欢用户接口测试')
    @pytest.mark.parametrize('value', [token, '', '123'])
    def test_all_matchs(self, value):
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
            assert(result_json['error'], 'Unauthenticated.')
        else:
            assert('list'in result_json['data'])
            assert('total'in result_json['data'])
            logging.debug('相互喜欢的人数为：{}'.format( result_json['data']['total']))

    @allure.story('即时匹配接口测试')
    @pytest.mark.parametrize('value,vip', [(token, 0),
                                           (token, 1),
                                           ('', 0),
                                           ('123', 0)])
    def test_instant_match(self, value,vip):
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
            self.login_require(result_json,value)
        else:
            if vip==0:
                logging.debug("普通用户的匹配总次数为：{}".format(result_json['matchTotal']))

            assert (result_json['instantMatchCount'] is not None)
            assert (result_json['surplusMatchCount'] is not None)
            logging.debug("已使用次数为:{}".format(result_json['instantMatchCount']))
            logging.debug("剩余次数为:{}".format(result_json['surplusMatchCount']))
            assert result_json['matchTotal']==result_json['surplusMatchCount']+result_json['instantMatchCount']

            assert(result_json['code']==200)
            assert(result_json['message']=='User instantMatch successfully')
            logging.debug('即时匹配返回状态码200，返回信息为：{}'.format('User instantMatch successfully'))

    @allure.story('发送邮箱验证码（注册、忘记密码）')
    def test_send_email_code(self):
        headers = {
            "Accept": "application/json",
        }

        data={
            "email": "archerckkbin@gmail.com",
            "operation": "setEmail"
              }

        url = '{}/api/user/send_email_code'.format(host)

        response = requests.post(url, headers=headers,data=data)

        result_json = response.json()

        logging.debug(result_json)

        assert(result_json['status'],True)
        assert(result_json['code']==200)
        assert(result_json['data']['email']is not None)
        logging.debug('验证码发送状态码会200，发送成功')


    # @allure.story('获取国际城市接口测试_已弃用')
    # def test_getNationalCity(self):
    #     '获取国际城市'
    #
    #     headers = {
    #         "Accept": "application/json",
    #     }
    #
    #     url = '{}/api/user/getNationalCity'.format(host)
    #
    #     response = requests.post(url, headers=headers)
    #
    #     result_json = response.json()
    #
    #     logging.debug(result_json)
    #     assert(result_json[0]['name'],'Singapore')
    #     assert(result_json[1]['name'],'United Kingdom')
    #     assert(result_json[2]['name'],'United States')

    @allure.story('更新用户状态接口测试')
    @pytest.mark.parametrize('value', [token, '', '123'])
    def test_update_profile(self,value):
        headers = {
            "Authorization":value,
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

        if value==token:
            assert(result_json['message'],'success')
            assert(result_json['code'],1)
            logging.debug('更新成功')
        else:
            self.login_require(result_json,value)

    @allure.story('添加黑名单接口测试')
    @pytest.mark.parametrize('value', [token, '', '123'])
    def test_user_block(self,value):
        headers = {
            "Authorization":value,
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

        if value==token:
            assert(result_json['code'], 200)
            assert(result_json['status'], True)
            logging.debug('提示信息：{}'.format(result_json['message']))
        else:
            self.login_require(result_json,value)

    @allure.story('匹配小红点状态修改接口')
    def test_match_list_429(self):
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

        assert(result_json['message']is not None)
        assert(result_json['status']is not None)
        logging.debug('选中的id不正确，修改失败')
        # assert(result_json['data'] is not None)

    @allure.story('滑动卡片发送状态接口测试')
    @pytest.mark.parametrize('value,code', [(token,1),
                                            (token,3),
                                            (token,2),
                                            (token,4),
                                            ('',3),
                                            ('123',3)])
    def test_likes(self,value,code):
        '滑动卡片发送喜欢或者不喜欢状态'

        headers = {
            "Authorization": value,
            "Content-Type": "application/x-www-form-urlencoded",
            "Content-Length": "20",
            "Host": "150.109.38.68",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttp/3.12.0",
            "X-Requested-With": "XMLHttpRequest"
        }

        data = {
            "like_id": "728",
            "status": value
        }

        url = '{}/api/user/likes'.format(host)

        response = requests.post(url, headers=headers, data=data)
        # logging.debug(response.text())
        result_json = response.json()

        logging.debug('返回内容为：{}'.format(result_json))

        if value==token:
            if result_json['message']=='request times used up':
                logging.debug('测试卡片是否用完')
                logging.debug('卡片测试次数用完了')
            elif code==3:
                logging.debug('测试标记不喜欢')
                assert result_json['status']=='DISLIKED'
                assert result_json['statuscode']==3
                assert result_json['message'] =='User disliked successfully'
                logging.debug('不喜欢成功')
            elif value==1:
                logging.debug('测试标记喜欢')
                assert result_json['status']=='LIKED'
                assert result_json['statuscode']== 1
                assert result_json['message']=='User liked successfully'
                logging.debug('喜欢成功')
            elif value==2:
                logging.debug('测试标记超级喜欢')
                assert result_json['status']=='SUPERLIKED'
                assert result_json['statuscode']==2
                assert result_json['message']=='User superliked successfully'
                logging.debug('超级喜欢成功')
            elif value==4:
                logging.debug('测试标记你已经喜欢过他了')
                assert (result_json['status']=='ALREADY_LIKED')
                assert (result_json['statuscode']==4)
                assert (result_json['message'], 'You already liked')
                logging.debug('你已经喜欢过他了')
        else:
            self.login_require(result_json,value)



if __name__ == '__main__':
    pytest.main(' -s ./ar_341_meetu_api.py::Test_meetU_API::test_instant_match')