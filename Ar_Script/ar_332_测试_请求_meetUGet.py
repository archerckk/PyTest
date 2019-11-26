import unittest
import requests
from ddt import ddt,data,unpack
import logging

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s')

@ddt
class Get_test(unittest.TestCase):

    def setUp(self) -> None:
        #environment=['test','normal']

        environment='test'
        if environment=='test':
            self.host='http://150.109.38.68'
        elif environment=='normal':
            self.host='http://www.meetuapp.info'


    @data(
        'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImQzZTRhZDU5NzQ4NzU1ZjMwODI5YmYyNDQzN2JhODViODY3ODNhNzhhYmZhY2I4MGI3ODY1YTQ5OWJiNmVjZmU1MTM2ZjlmNzhiZDg5N2NhIn0.eyJhdWQiOiIyIiwianRpIjoiZDNlNGFkNTk3NDg3NTVmMzA4MjliZjI0NDM3YmE4NWI4Njc4M2E3OGFiZmFjYjgwYjc4NjVhNDk5YmI2ZWNmZTUxMzZmOWY3OGJkODk3Y2EiLCJpYXQiOjE1NzQ0Mjk3NDgsIm5iZiI6MTU3NDQyOTc0OCwiZXhwIjoxNTc1NzI1NzQ4LCJzdWIiOiI0MjkiLCJzY29wZXMiOltdfQ.COE8VPyJQOJSPWEG0i_iOcm81Rg0Y9a5gCOyeuHJfqHdvsHAOm2jkAA6nfU_WhmqXrZlNA64GrqNi9BjE8sFlMUcwRBl5EjJap_p2X33uxBtM-u4Ge1nr3H8phBYPZK6sOmGSMYuwWFo6fdem3wot5swz2eKGKrCA1Pn4aSH5L87vidfF2-FJfo5Zl45ePrzr68__MkqQyce7LWj-SGxUCejkBv7PTJputtg-7Azz8GJKl4QAyOAmhCqFTwXE4dy29jyMqdBKDEf1cTlhhiNayyLLY_m4om-MtVj9KNZWY09xnMq9WBynKU3_s_nSCLVH2po0jfUt1_o62TWKL1UAN9fBGY9Zl6d-jIwVt8WUVoJikaUahXLFzGaF880nGmYSxs_DG2-VRrLAhlm5lWfvwYH3DfGBOFp-Imk9a7sBpIKZAJ2kIjPl6Oo-RapPTNwAE3rsYsSQD0igt5_jtn55BfMKspn8RJf6leKsTCs0lSOe2qpnvU94SUTnbGbqNaLZrvDDYJQu_BRO5uZWbBDElETimMf4q4dQMEvHSC-NqiViiisgsHyztDKUsrcz_orfEmxw2yGeumobpKDt8jc0HNEJ3mPQnZKV7zs6KrDNlwDbKNvreV-ARt6rZRuLhTuKjQcKcmR0nFB6KwlfDvOfYC7AbJYdfAqFjEbhw5DE0A',
        '',
        '123'
    )
    def test_who_likes_me_count(self,value):
        #构造header部分
        headers={
        "Authorization":value,
        "Host": "150.109.38.68",
        "Connection": "Keep - Alive",
        "Accept - Encoding": "gzip",
        "User - Agent": "okhttp / 3.12.0",
        "X - Requested - With": "XMLHttpRequest",
        }

        url='{}/api/user/who_likes_me_count'.format(self.host)

        response=requests.get(url,headers=headers)
        content=response.text
        # logging.debug('返回内容为：{}'.format(content))

        if value=='' or value=='123':
            self.assertTrue('Login to Your Account'in content)
        else:
            self.assertTrue('likes_me_count'in content)
            self.assertEqual(response.status_code,200)
            self.assertTrue('"code":200'in content)


    def test_user_app(self):
        logging.debug('用户信息获取接口_user/user_app测试开始')
        headers={
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImQzZTRhZDU5NzQ4NzU1ZjMwODI5YmYyNDQzN2JhODViODY3ODNhNzhhYmZhY2I4MGI3ODY1YTQ5OWJiNmVjZmU1MTM2ZjlmNzhiZDg5N2NhIn0.eyJhdWQiOiIyIiwianRpIjoiZDNlNGFkNTk3NDg3NTVmMzA4MjliZjI0NDM3YmE4NWI4Njc4M2E3OGFiZmFjYjgwYjc4NjVhNDk5YmI2ZWNmZTUxMzZmOWY3OGJkODk3Y2EiLCJpYXQiOjE1NzQ0Mjk3NDgsIm5iZiI6MTU3NDQyOTc0OCwiZXhwIjoxNTc1NzI1NzQ4LCJzdWIiOiI0MjkiLCJzY29wZXMiOltdfQ.COE8VPyJQOJSPWEG0i_iOcm81Rg0Y9a5gCOyeuHJfqHdvsHAOm2jkAA6nfU_WhmqXrZlNA64GrqNi9BjE8sFlMUcwRBl5EjJap_p2X33uxBtM-u4Ge1nr3H8phBYPZK6sOmGSMYuwWFo6fdem3wot5swz2eKGKrCA1Pn4aSH5L87vidfF2-FJfo5Zl45ePrzr68__MkqQyce7LWj-SGxUCejkBv7PTJputtg-7Azz8GJKl4QAyOAmhCqFTwXE4dy29jyMqdBKDEf1cTlhhiNayyLLY_m4om-MtVj9KNZWY09xnMq9WBynKU3_s_nSCLVH2po0jfUt1_o62TWKL1UAN9fBGY9Zl6d-jIwVt8WUVoJikaUahXLFzGaF880nGmYSxs_DG2-VRrLAhlm5lWfvwYH3DfGBOFp-Imk9a7sBpIKZAJ2kIjPl6Oo-RapPTNwAE3rsYsSQD0igt5_jtn55BfMKspn8RJf6leKsTCs0lSOe2qpnvU94SUTnbGbqNaLZrvDDYJQu_BRO5uZWbBDElETimMf4q4dQMEvHSC-NqiViiisgsHyztDKUsrcz_orfEmxw2yGeumobpKDt8jc0HNEJ3mPQnZKV7zs6KrDNlwDbKNvreV-ARt6rZRuLhTuKjQcKcmR0nFB6KwlfDvOfYC7AbJYdfAqFjEbhw5DE0A",
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": "74",
        "Host": "150.109.38.68",
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

        url='{}/api/user/user_app'.format(self.host)

        responese=requests.post(url,headers=headers,data=data)

        result=responese.text
        logging.debug('返回内容为：{}'.format(result))

        self.assertTrue('"message":"success"'in result)
        self.assertTrue('"user_id":429' in result)

    @data(
        'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImQzZTRhZDU5NzQ4NzU1ZjMwODI5YmYyNDQzN2JhODViODY3ODNhNzhhYmZhY2I4MGI3ODY1YTQ5OWJiNmVjZmU1MTM2ZjlmNzhiZDg5N2NhIn0.eyJhdWQiOiIyIiwianRpIjoiZDNlNGFkNTk3NDg3NTVmMzA4MjliZjI0NDM3YmE4NWI4Njc4M2E3OGFiZmFjYjgwYjc4NjVhNDk5YmI2ZWNmZTUxMzZmOWY3OGJkODk3Y2EiLCJpYXQiOjE1NzQ0Mjk3NDgsIm5iZiI6MTU3NDQyOTc0OCwiZXhwIjoxNTc1NzI1NzQ4LCJzdWIiOiI0MjkiLCJzY29wZXMiOltdfQ.COE8VPyJQOJSPWEG0i_iOcm81Rg0Y9a5gCOyeuHJfqHdvsHAOm2jkAA6nfU_WhmqXrZlNA64GrqNi9BjE8sFlMUcwRBl5EjJap_p2X33uxBtM-u4Ge1nr3H8phBYPZK6sOmGSMYuwWFo6fdem3wot5swz2eKGKrCA1Pn4aSH5L87vidfF2-FJfo5Zl45ePrzr68__MkqQyce7LWj-SGxUCejkBv7PTJputtg-7Azz8GJKl4QAyOAmhCqFTwXE4dy29jyMqdBKDEf1cTlhhiNayyLLY_m4om-MtVj9KNZWY09xnMq9WBynKU3_s_nSCLVH2po0jfUt1_o62TWKL1UAN9fBGY9Zl6d-jIwVt8WUVoJikaUahXLFzGaF880nGmYSxs_DG2-VRrLAhlm5lWfvwYH3DfGBOFp-Imk9a7sBpIKZAJ2kIjPl6Oo-RapPTNwAE3rsYsSQD0igt5_jtn55BfMKspn8RJf6leKsTCs0lSOe2qpnvU94SUTnbGbqNaLZrvDDYJQu_BRO5uZWbBDElETimMf4q4dQMEvHSC-NqiViiisgsHyztDKUsrcz_orfEmxw2yGeumobpKDt8jc0HNEJ3mPQnZKV7zs6KrDNlwDbKNvreV-ARt6rZRuLhTuKjQcKcmR0nFB6KwlfDvOfYC7AbJYdfAqFjEbhw5DE0A',
        '',
        '123'
    )
    def test_update_setting(self,value):
        '配置获取接口'
        # 构造header部分
        headers = {
            "Authorization": value,
            "Host": "150.109.38.68",
            "Connection": "Keep - Alive",
            "Accept - Encoding": "gzip",
            "User - Agent": "okhttp / 3.12.0",
            "X - Requested - With": "XMLHttpRequest",
        }

        url = '{}/api/user/get_setting'.format(self.host)

        response = requests.get(url, headers=headers)

        content = response.text

        if value == '' or value == '123':
            self.assertTrue('Login to Your Account' in content)
        else:
            result_json = response.json()
            self.assertEqual(result_json['user_id'],429)

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
            "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImQzZTRhZDU5NzQ4NzU1ZjMwODI5YmYyNDQzN2JhODViODY3ODNhNzhhYmZhY2I4MGI3ODY1YTQ5OWJiNmVjZmU1MTM2ZjlmNzhiZDg5N2NhIn0.eyJhdWQiOiIyIiwianRpIjoiZDNlNGFkNTk3NDg3NTVmMzA4MjliZjI0NDM3YmE4NWI4Njc4M2E3OGFiZmFjYjgwYjc4NjVhNDk5YmI2ZWNmZTUxMzZmOWY3OGJkODk3Y2EiLCJpYXQiOjE1NzQ0Mjk3NDgsIm5iZiI6MTU3NDQyOTc0OCwiZXhwIjoxNTc1NzI1NzQ4LCJzdWIiOiI0MjkiLCJzY29wZXMiOltdfQ.COE8VPyJQOJSPWEG0i_iOcm81Rg0Y9a5gCOyeuHJfqHdvsHAOm2jkAA6nfU_WhmqXrZlNA64GrqNi9BjE8sFlMUcwRBl5EjJap_p2X33uxBtM-u4Ge1nr3H8phBYPZK6sOmGSMYuwWFo6fdem3wot5swz2eKGKrCA1Pn4aSH5L87vidfF2-FJfo5Zl45ePrzr68__MkqQyce7LWj-SGxUCejkBv7PTJputtg-7Azz8GJKl4QAyOAmhCqFTwXE4dy29jyMqdBKDEf1cTlhhiNayyLLY_m4om-MtVj9KNZWY09xnMq9WBynKU3_s_nSCLVH2po0jfUt1_o62TWKL1UAN9fBGY9Zl6d-jIwVt8WUVoJikaUahXLFzGaF880nGmYSxs_DG2-VRrLAhlm5lWfvwYH3DfGBOFp-Imk9a7sBpIKZAJ2kIjPl6Oo-RapPTNwAE3rsYsSQD0igt5_jtn55BfMKspn8RJf6leKsTCs0lSOe2qpnvU94SUTnbGbqNaLZrvDDYJQu_BRO5uZWbBDElETimMf4q4dQMEvHSC-NqiViiisgsHyztDKUsrcz_orfEmxw2yGeumobpKDt8jc0HNEJ3mPQnZKV7zs6KrDNlwDbKNvreV-ARt6rZRuLhTuKjQcKcmR0nFB6KwlfDvOfYC7AbJYdfAqFjEbhw5DE0A",
            "Content-Type": "application/x-www-form-urlencoded",
            "Content-Length": "5",
            "Host": "150.109.38.68",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttp/3.12.0",
            "X-Requested-With": "XMLHttpRequest"
        }

        url='{}/api/user/find_match'.format(self.host)

        data={'vip':value}

        response=requests.post(url,headers=headers,data=data)
        result_json=response.json()

        logging.debug(response.text)
        logging.debug("卡片的剩余数为：{}".format(result_json['remain_amount']))
        self.assertTrue(isinstance(result_json['remain_amount'],int),True)

    @data(
        'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImQzZTRhZDU5NzQ4NzU1ZjMwODI5YmYyNDQzN2JhODViODY3ODNhNzhhYmZhY2I4MGI3ODY1YTQ5OWJiNmVjZmU1MTM2ZjlmNzhiZDg5N2NhIn0.eyJhdWQiOiIyIiwianRpIjoiZDNlNGFkNTk3NDg3NTVmMzA4MjliZjI0NDM3YmE4NWI4Njc4M2E3OGFiZmFjYjgwYjc4NjVhNDk5YmI2ZWNmZTUxMzZmOWY3OGJkODk3Y2EiLCJpYXQiOjE1NzQ0Mjk3NDgsIm5iZiI6MTU3NDQyOTc0OCwiZXhwIjoxNTc1NzI1NzQ4LCJzdWIiOiI0MjkiLCJzY29wZXMiOltdfQ.COE8VPyJQOJSPWEG0i_iOcm81Rg0Y9a5gCOyeuHJfqHdvsHAOm2jkAA6nfU_WhmqXrZlNA64GrqNi9BjE8sFlMUcwRBl5EjJap_p2X33uxBtM-u4Ge1nr3H8phBYPZK6sOmGSMYuwWFo6fdem3wot5swz2eKGKrCA1Pn4aSH5L87vidfF2-FJfo5Zl45ePrzr68__MkqQyce7LWj-SGxUCejkBv7PTJputtg-7Azz8GJKl4QAyOAmhCqFTwXE4dy29jyMqdBKDEf1cTlhhiNayyLLY_m4om-MtVj9KNZWY09xnMq9WBynKU3_s_nSCLVH2po0jfUt1_o62TWKL1UAN9fBGY9Zl6d-jIwVt8WUVoJikaUahXLFzGaF880nGmYSxs_DG2-VRrLAhlm5lWfvwYH3DfGBOFp-Imk9a7sBpIKZAJ2kIjPl6Oo-RapPTNwAE3rsYsSQD0igt5_jtn55BfMKspn8RJf6leKsTCs0lSOe2qpnvU94SUTnbGbqNaLZrvDDYJQu_BRO5uZWbBDElETimMf4q4dQMEvHSC-NqiViiisgsHyztDKUsrcz_orfEmxw2yGeumobpKDt8jc0HNEJ3mPQnZKV7zs6KrDNlwDbKNvreV-ARt6rZRuLhTuKjQcKcmR0nFB6KwlfDvOfYC7AbJYdfAqFjEbhw5DE0A',
        '123',
        ''
    )
    def test_get_profile(self,value):
        '获取用户信息'
        headers={
            "Authorization":value,
            "Content-Type": "application/x-www-form-urlencoded",
            "Content-Length": "5",
            "Host": "150.109.38.68",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttp/3.12.0",
            "X-Requested-With": "XMLHttpRequest"
        }

        data={
            'device_token':"fW9SjEZW7BM%3AAPA91bFx4qQMD9mhheKv0b9WcCiviVRjkLbmWmTsqb8_9rrJGoJqWhLuuKOJia6hny-FQxgRMeMKbqMsr_VAC_WzSFIlv26YAcLtk1KWwfjhxwyWJVJNXqg5yqOFX_xb-qnbfOEaYFkH "
        }

        url='{}/api/user/get_profile'.format(self.host)
        response=requests.get(url,headers=headers,data=data)
        result_json=response.json()

        logging.debug(result_json)

        if value=='123' or value=='':
            self.assertEqual(result_json['error'],'Unauthenticated.')
        else:
            self.assertTrue(result_json['user']['id']==429)

    @data(
        'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImQzZTRhZDU5NzQ4NzU1ZjMwODI5YmYyNDQzN2JhODViODY3ODNhNzhhYmZhY2I4MGI3ODY1YTQ5OWJiNmVjZmU1MTM2ZjlmNzhiZDg5N2NhIn0.eyJhdWQiOiIyIiwianRpIjoiZDNlNGFkNTk3NDg3NTVmMzA4MjliZjI0NDM3YmE4NWI4Njc4M2E3OGFiZmFjYjgwYjc4NjVhNDk5YmI2ZWNmZTUxMzZmOWY3OGJkODk3Y2EiLCJpYXQiOjE1NzQ0Mjk3NDgsIm5iZiI6MTU3NDQyOTc0OCwiZXhwIjoxNTc1NzI1NzQ4LCJzdWIiOiI0MjkiLCJzY29wZXMiOltdfQ.COE8VPyJQOJSPWEG0i_iOcm81Rg0Y9a5gCOyeuHJfqHdvsHAOm2jkAA6nfU_WhmqXrZlNA64GrqNi9BjE8sFlMUcwRBl5EjJap_p2X33uxBtM-u4Ge1nr3H8phBYPZK6sOmGSMYuwWFo6fdem3wot5swz2eKGKrCA1Pn4aSH5L87vidfF2-FJfo5Zl45ePrzr68__MkqQyce7LWj-SGxUCejkBv7PTJputtg-7Azz8GJKl4QAyOAmhCqFTwXE4dy29jyMqdBKDEf1cTlhhiNayyLLY_m4om-MtVj9KNZWY09xnMq9WBynKU3_s_nSCLVH2po0jfUt1_o62TWKL1UAN9fBGY9Zl6d-jIwVt8WUVoJikaUahXLFzGaF880nGmYSxs_DG2-VRrLAhlm5lWfvwYH3DfGBOFp-Imk9a7sBpIKZAJ2kIjPl6Oo-RapPTNwAE3rsYsSQD0igt5_jtn55BfMKspn8RJf6leKsTCs0lSOe2qpnvU94SUTnbGbqNaLZrvDDYJQu_BRO5uZWbBDElETimMf4q4dQMEvHSC-NqiViiisgsHyztDKUsrcz_orfEmxw2yGeumobpKDt8jc0HNEJ3mPQnZKV7zs6KrDNlwDbKNvreV-ARt6rZRuLhTuKjQcKcmR0nFB6KwlfDvOfYC7AbJYdfAqFjEbhw5DE0A',
        '123',
        ''
    )
    def test_match_list(self,value):
        '获取发过消息用户列表'

        headers = {
         "Authorization": value,
         "Host": "150.109.38.68",
         "Connection": "Keep-Alive",
         "Accept-Encoding": "gzip",
         "User-Agent": "okhttp/3.12.0",
         "X-Requested-With": "XMLHttpRequest"
        }

        url='{}/api/user/match_list'.format(self.host)

        response = requests.get(url, headers=headers)

        result_json = response.json()

        logging.debug(result_json)

        if value == '123' or value == '':
            self.assertEqual(result_json['error'], 'Unauthenticated.')
        else:
            self.assertTrue(result_json[0]['user_id'] == 429)

    @data(
        'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImQzZTRhZDU5NzQ4NzU1ZjMwODI5YmYyNDQzN2JhODViODY3ODNhNzhhYmZhY2I4MGI3ODY1YTQ5OWJiNmVjZmU1MTM2ZjlmNzhiZDg5N2NhIn0.eyJhdWQiOiIyIiwianRpIjoiZDNlNGFkNTk3NDg3NTVmMzA4MjliZjI0NDM3YmE4NWI4Njc4M2E3OGFiZmFjYjgwYjc4NjVhNDk5YmI2ZWNmZTUxMzZmOWY3OGJkODk3Y2EiLCJpYXQiOjE1NzQ0Mjk3NDgsIm5iZiI6MTU3NDQyOTc0OCwiZXhwIjoxNTc1NzI1NzQ4LCJzdWIiOiI0MjkiLCJzY29wZXMiOltdfQ.COE8VPyJQOJSPWEG0i_iOcm81Rg0Y9a5gCOyeuHJfqHdvsHAOm2jkAA6nfU_WhmqXrZlNA64GrqNi9BjE8sFlMUcwRBl5EjJap_p2X33uxBtM-u4Ge1nr3H8phBYPZK6sOmGSMYuwWFo6fdem3wot5swz2eKGKrCA1Pn4aSH5L87vidfF2-FJfo5Zl45ePrzr68__MkqQyce7LWj-SGxUCejkBv7PTJputtg-7Azz8GJKl4QAyOAmhCqFTwXE4dy29jyMqdBKDEf1cTlhhiNayyLLY_m4om-MtVj9KNZWY09xnMq9WBynKU3_s_nSCLVH2po0jfUt1_o62TWKL1UAN9fBGY9Zl6d-jIwVt8WUVoJikaUahXLFzGaF880nGmYSxs_DG2-VRrLAhlm5lWfvwYH3DfGBOFp-Imk9a7sBpIKZAJ2kIjPl6Oo-RapPTNwAE3rsYsSQD0igt5_jtn55BfMKspn8RJf6leKsTCs0lSOe2qpnvU94SUTnbGbqNaLZrvDDYJQu_BRO5uZWbBDElETimMf4q4dQMEvHSC-NqiViiisgsHyztDKUsrcz_orfEmxw2yGeumobpKDt8jc0HNEJ3mPQnZKV7zs6KrDNlwDbKNvreV-ARt6rZRuLhTuKjQcKcmR0nFB6KwlfDvOfYC7AbJYdfAqFjEbhw5DE0A',
        '123',
        ''
    )
    def test_update_online_state(self, value):
        '用户是否在线状态更新'

        headers = {
            "Authorization": value,
            "Host": "150.109.38.68",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttp/3.12.0",
            "X-Requested-With": "XMLHttpRequest"
        }

        url = '{}/api/user/update_online_state'.format(self.host)

        response = requests.post(url, headers=headers)

        result_json = response.json()

        logging.debug(result_json)

        if value == '123' or value == '':
            self.assertEqual(result_json['error'], 'Unauthenticated.')
        else:
            self.assertTrue(result_json['message'] == 'update_online_state_success')

    @data(
        'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImQzZTRhZDU5NzQ4NzU1ZjMwODI5YmYyNDQzN2JhODViODY3ODNhNzhhYmZhY2I4MGI3ODY1YTQ5OWJiNmVjZmU1MTM2ZjlmNzhiZDg5N2NhIn0.eyJhdWQiOiIyIiwianRpIjoiZDNlNGFkNTk3NDg3NTVmMzA4MjliZjI0NDM3YmE4NWI4Njc4M2E3OGFiZmFjYjgwYjc4NjVhNDk5YmI2ZWNmZTUxMzZmOWY3OGJkODk3Y2EiLCJpYXQiOjE1NzQ0Mjk3NDgsIm5iZiI6MTU3NDQyOTc0OCwiZXhwIjoxNTc1NzI1NzQ4LCJzdWIiOiI0MjkiLCJzY29wZXMiOltdfQ.COE8VPyJQOJSPWEG0i_iOcm81Rg0Y9a5gCOyeuHJfqHdvsHAOm2jkAA6nfU_WhmqXrZlNA64GrqNi9BjE8sFlMUcwRBl5EjJap_p2X33uxBtM-u4Ge1nr3H8phBYPZK6sOmGSMYuwWFo6fdem3wot5swz2eKGKrCA1Pn4aSH5L87vidfF2-FJfo5Zl45ePrzr68__MkqQyce7LWj-SGxUCejkBv7PTJputtg-7Azz8GJKl4QAyOAmhCqFTwXE4dy29jyMqdBKDEf1cTlhhiNayyLLY_m4om-MtVj9KNZWY09xnMq9WBynKU3_s_nSCLVH2po0jfUt1_o62TWKL1UAN9fBGY9Zl6d-jIwVt8WUVoJikaUahXLFzGaF880nGmYSxs_DG2-VRrLAhlm5lWfvwYH3DfGBOFp-Imk9a7sBpIKZAJ2kIjPl6Oo-RapPTNwAE3rsYsSQD0igt5_jtn55BfMKspn8RJf6leKsTCs0lSOe2qpnvU94SUTnbGbqNaLZrvDDYJQu_BRO5uZWbBDElETimMf4q4dQMEvHSC-NqiViiisgsHyztDKUsrcz_orfEmxw2yGeumobpKDt8jc0HNEJ3mPQnZKV7zs6KrDNlwDbKNvreV-ARt6rZRuLhTuKjQcKcmR0nFB6KwlfDvOfYC7AbJYdfAqFjEbhw5DE0A',
        '123',
        ''
    )
    def test_all_matchs(self, value):
        '查看互相喜欢用户'

        headers = {
            "Authorization": value,
            "Content-Length": "0",
            "Host": "150.109.38.68",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttp/3.12.0",
            "X-Requested-With": "XMLHttpRequest"
        }

        url = '{}/api/user/all_matchs'.format(self.host)

        response = requests.post(url, headers=headers)

        result_json = response.json()

        logging.debug(result_json)

        if value == '123' or value == '':
            self.assertEqual(result_json['error'], 'Unauthenticated.')
        else:
            self.assertTrue('list'in result_json['data'])
            self.assertTrue('total'in result_json['data'])

    @data(
        ( 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImQzZTRhZDU5NzQ4NzU1ZjMwODI5YmYyNDQzN2JhODViODY3ODNhNzhhYmZhY2I4MGI3ODY1YTQ5OWJiNmVjZmU1MTM2ZjlmNzhiZDg5N2NhIn0.eyJhdWQiOiIyIiwianRpIjoiZDNlNGFkNTk3NDg3NTVmMzA4MjliZjI0NDM3YmE4NWI4Njc4M2E3OGFiZmFjYjgwYjc4NjVhNDk5YmI2ZWNmZTUxMzZmOWY3OGJkODk3Y2EiLCJpYXQiOjE1NzQ0Mjk3NDgsIm5iZiI6MTU3NDQyOTc0OCwiZXhwIjoxNTc1NzI1NzQ4LCJzdWIiOiI0MjkiLCJzY29wZXMiOltdfQ.COE8VPyJQOJSPWEG0i_iOcm81Rg0Y9a5gCOyeuHJfqHdvsHAOm2jkAA6nfU_WhmqXrZlNA64GrqNi9BjE8sFlMUcwRBl5EjJap_p2X33uxBtM-u4Ge1nr3H8phBYPZK6sOmGSMYuwWFo6fdem3wot5swz2eKGKrCA1Pn4aSH5L87vidfF2-FJfo5Zl45ePrzr68__MkqQyce7LWj-SGxUCejkBv7PTJputtg-7Azz8GJKl4QAyOAmhCqFTwXE4dy29jyMqdBKDEf1cTlhhiNayyLLY_m4om-MtVj9KNZWY09xnMq9WBynKU3_s_nSCLVH2po0jfUt1_o62TWKL1UAN9fBGY9Zl6d-jIwVt8WUVoJikaUahXLFzGaF880nGmYSxs_DG2-VRrLAhlm5lWfvwYH3DfGBOFp-Imk9a7sBpIKZAJ2kIjPl6Oo-RapPTNwAE3rsYsSQD0igt5_jtn55BfMKspn8RJf6leKsTCs0lSOe2qpnvU94SUTnbGbqNaLZrvDDYJQu_BRO5uZWbBDElETimMf4q4dQMEvHSC-NqiViiisgsHyztDKUsrcz_orfEmxw2yGeumobpKDt8jc0HNEJ3mPQnZKV7zs6KrDNlwDbKNvreV-ARt6rZRuLhTuKjQcKcmR0nFB6KwlfDvOfYC7AbJYdfAqFjEbhw5DE0A',1),
        ( 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImQzZTRhZDU5NzQ4NzU1ZjMwODI5YmYyNDQzN2JhODViODY3ODNhNzhhYmZhY2I4MGI3ODY1YTQ5OWJiNmVjZmU1MTM2ZjlmNzhiZDg5N2NhIn0.eyJhdWQiOiIyIiwianRpIjoiZDNlNGFkNTk3NDg3NTVmMzA4MjliZjI0NDM3YmE4NWI4Njc4M2E3OGFiZmFjYjgwYjc4NjVhNDk5YmI2ZWNmZTUxMzZmOWY3OGJkODk3Y2EiLCJpYXQiOjE1NzQ0Mjk3NDgsIm5iZiI6MTU3NDQyOTc0OCwiZXhwIjoxNTc1NzI1NzQ4LCJzdWIiOiI0MjkiLCJzY29wZXMiOltdfQ.COE8VPyJQOJSPWEG0i_iOcm81Rg0Y9a5gCOyeuHJfqHdvsHAOm2jkAA6nfU_WhmqXrZlNA64GrqNi9BjE8sFlMUcwRBl5EjJap_p2X33uxBtM-u4Ge1nr3H8phBYPZK6sOmGSMYuwWFo6fdem3wot5swz2eKGKrCA1Pn4aSH5L87vidfF2-FJfo5Zl45ePrzr68__MkqQyce7LWj-SGxUCejkBv7PTJputtg-7Azz8GJKl4QAyOAmhCqFTwXE4dy29jyMqdBKDEf1cTlhhiNayyLLY_m4om-MtVj9KNZWY09xnMq9WBynKU3_s_nSCLVH2po0jfUt1_o62TWKL1UAN9fBGY9Zl6d-jIwVt8WUVoJikaUahXLFzGaF880nGmYSxs_DG2-VRrLAhlm5lWfvwYH3DfGBOFp-Imk9a7sBpIKZAJ2kIjPl6Oo-RapPTNwAE3rsYsSQD0igt5_jtn55BfMKspn8RJf6leKsTCs0lSOe2qpnvU94SUTnbGbqNaLZrvDDYJQu_BRO5uZWbBDElETimMf4q4dQMEvHSC-NqiViiisgsHyztDKUsrcz_orfEmxw2yGeumobpKDt8jc0HNEJ3mPQnZKV7zs6KrDNlwDbKNvreV-ARt6rZRuLhTuKjQcKcmR0nFB6KwlfDvOfYC7AbJYdfAqFjEbhw5DE0A',0),
        # ( 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImQzZTRhZDU5NzQ4NzU1ZjMwODI5YmYyNDQzN2JhODViODY3ODNhNzhhYmZhY2I4MGI3ODY1YTQ5OWJiNmVjZmU1MTM2ZjlmNzhiZDg5N2NhIn0.eyJhdWQiOiIyIiwianRpIjoiZDNlNGFkNTk3NDg3NTVmMzA4MjliZjI0NDM3YmE4NWI4Njc4M2E3OGFiZmFjYjgwYjc4NjVhNDk5YmI2ZWNmZTUxMzZmOWY3OGJkODk3Y2EiLCJpYXQiOjE1NzQ0Mjk3NDgsIm5iZiI6MTU3NDQyOTc0OCwiZXhwIjoxNTc1NzI1NzQ4LCJzdWIiOiI0MjkiLCJzY29wZXMiOltdfQ.COE8VPyJQOJSPWEG0i_iOcm81Rg0Y9a5gCOyeuHJfqHdvsHAOm2jkAA6nfU_WhmqXrZlNA64GrqNi9BjE8sFlMUcwRBl5EjJap_p2X33uxBtM-u4Ge1nr3H8phBYPZK6sOmGSMYuwWFo6fdem3wot5swz2eKGKrCA1Pn4aSH5L87vidfF2-FJfo5Zl45ePrzr68__MkqQyce7LWj-SGxUCejkBv7PTJputtg-7Azz8GJKl4QAyOAmhCqFTwXE4dy29jyMqdBKDEf1cTlhhiNayyLLY_m4om-MtVj9KNZWY09xnMq9WBynKU3_s_nSCLVH2po0jfUt1_o62TWKL1UAN9fBGY9Zl6d-jIwVt8WUVoJikaUahXLFzGaF880nGmYSxs_DG2-VRrLAhlm5lWfvwYH3DfGBOFp-Imk9a7sBpIKZAJ2kIjPl6Oo-RapPTNwAE3rsYsSQD0igt5_jtn55BfMKspn8RJf6leKsTCs0lSOe2qpnvU94SUTnbGbqNaLZrvDDYJQu_BRO5uZWbBDElETimMf4q4dQMEvHSC-NqiViiisgsHyztDKUsrcz_orfEmxw2yGeumobpKDt8jc0HNEJ3mPQnZKV7zs6KrDNlwDbKNvreV-ARt6rZRuLhTuKjQcKcmR0nFB6KwlfDvOfYC7AbJYdfAqFjEbhw5DE0A',0),
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
            "Host": "150.109.38.68",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttp/3.12.0",
            "X-Requested-With": "XMLHttpRequest"
        }

        data={'vip':vip}

        url = '{}/api/user/instant_match'.format(self.host)

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
    #     url = '{}/api/user/send_email_code'.format(self.host)
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

        url = '{}/api/user/getNationalCity'.format(self.host)

        response = requests.post(url, headers=headers)

        result_json = response.json()

        logging.debug(result_json)


        self.assertEqual(result_json[0]['name'],'Singapore')
        self.assertEqual(result_json[1]['name'],'United Kingdom')
        self.assertEqual(result_json[2]['name'],'United States')

    def test_update_profile(self):
        headers = {
             "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjE1NTJlNzBmMTY5ZGQ5OWI0MWYzNmQ3OTE4ZDQ5YzZiYzNiYjE2MzZhZjE3OGM1NzBkMDFhOTZkYmNkNGZjODViZmQ5ZTVmMGEyNjU3YTY3In0.eyJhdWQiOiIyIiwianRpIjoiMTU1MmU3MGYxNjlkZDk5YjQxZjM2ZDc5MThkNDljNmJjM2JiMTYzNmFmMTc4YzU3MGQwMWE5NmRiY2Q0ZmM4NWJmZDllNWYwYTI2NTdhNjciLCJpYXQiOjE1NzQ3MjQyMTksIm5iZiI6MTU3NDcyNDIxOSwiZXhwIjoxNTc2MDIwMjE5LCJzdWIiOiI0MjMiLCJzY29wZXMiOltdfQ.oj0zj3H6wLqiG2_juT0KiOLXATy5yWj9IWsD9j1q-QH-EVq196Rx9rWw8HRVSO7__X3-2k2U2e0ykgpOdRClPe03D3dngqVnmQmCRPUPs23q19yuWzOnmpurFVLWwpt5_PiYHrVa91JSq5HboA6QSwdafX6iM2cuRwsjXZ4xzzcj29tqIgtIXblGwzc7QejWN4KdnW13sHUOMnzJVK5XU7AMNmk7NGPolgbIphoW5Zi2JwLyQdt4h9w61hs9eEUFfqXifOGdfpmT67vK-0Me56UPQQ6nIm0QlJVDHooTYYS7z9iykzmHYTutfo4_ETrI76TDi3m2tCF2gEtBUEnyf4GwrYd-4KYTeh0BDSEQwwPo6fi-TnwBVzAWpQGTArXrOll0MMvIYXoEgMlRKN-JT6fRm0ghPmfFry8tz02jaAdm45348jxf6u5vsXFMkW0OM8fgOdpZ5VLUrsV_RpJlGZs8qaKlJsXOG_yHcuZ2paO5cshz5POIgH0wf6IAqguMsjg38L8u0OqL824R1BPS1yR-Y8uEf_HhngcOqK5jeNs9ua1qLYpZQSp1Llvjdk1E3VpApLCInJLcGqxLemPJZEUcdQ7CBvxaEVRP7ijJgDMhTQZi_FQdhjWxwRgoZn2fGGxWQ3DFJ9a3vSu5-hKgq8Lbhc1nBhFBFUZl9VEiAhA",
             "Content-Type": "application/x-www-form-urlencoded",
             "Content-Length": "246",
             "Host": "150.109.38.68",
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

        url = '{}/api/user/user_app'.format(self.host)

        response=requests.post(url,headers=headers,data=data)

        result_json = response.json()

        logging.debug('返回内容为：{}'.format(result_json))

        self.assertEqual(result_json['message'],'success')

    def test_user_block(self):
        headers = {
            "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjE1NTJlNzBmMTY5ZGQ5OWI0MWYzNmQ3OTE4ZDQ5YzZiYzNiYjE2MzZhZjE3OGM1NzBkMDFhOTZkYmNkNGZjODViZmQ5ZTVmMGEyNjU3YTY3In0.eyJhdWQiOiIyIiwianRpIjoiMTU1MmU3MGYxNjlkZDk5YjQxZjM2ZDc5MThkNDljNmJjM2JiMTYzNmFmMTc4YzU3MGQwMWE5NmRiY2Q0ZmM4NWJmZDllNWYwYTI2NTdhNjciLCJpYXQiOjE1NzQ3MjQyMTksIm5iZiI6MTU3NDcyNDIxOSwiZXhwIjoxNTc2MDIwMjE5LCJzdWIiOiI0MjMiLCJzY29wZXMiOltdfQ.oj0zj3H6wLqiG2_juT0KiOLXATy5yWj9IWsD9j1q-QH-EVq196Rx9rWw8HRVSO7__X3-2k2U2e0ykgpOdRClPe03D3dngqVnmQmCRPUPs23q19yuWzOnmpurFVLWwpt5_PiYHrVa91JSq5HboA6QSwdafX6iM2cuRwsjXZ4xzzcj29tqIgtIXblGwzc7QejWN4KdnW13sHUOMnzJVK5XU7AMNmk7NGPolgbIphoW5Zi2JwLyQdt4h9w61hs9eEUFfqXifOGdfpmT67vK-0Me56UPQQ6nIm0QlJVDHooTYYS7z9iykzmHYTutfo4_ETrI76TDi3m2tCF2gEtBUEnyf4GwrYd-4KYTeh0BDSEQwwPo6fi-TnwBVzAWpQGTArXrOll0MMvIYXoEgMlRKN-JT6fRm0ghPmfFry8tz02jaAdm45348jxf6u5vsXFMkW0OM8fgOdpZ5VLUrsV_RpJlGZs8qaKlJsXOG_yHcuZ2paO5cshz5POIgH0wf6IAqguMsjg38L8u0OqL824R1BPS1yR-Y8uEf_HhngcOqK5jeNs9ua1qLYpZQSp1Llvjdk1E3VpApLCInJLcGqxLemPJZEUcdQ7CBvxaEVRP7ijJgDMhTQZi_FQdhjWxwRgoZn2fGGxWQ3DFJ9a3vSu5-hKgq8Lbhc1nBhFBFUZl9VEiAhA",
            "Content-Type": "application/x-www-form-urlencoded",
            "Content-Length": "25",
            "Host": "150.109.38.68",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttp/3.12.0",
            "X-Requested-With": "XMLHttpRequest"
        }

        data = {
            "block_id": "385",
            "status": "block"
        }

        url = '{}/api/user/user_block'.format(self.host)

        response = requests.post(url, headers=headers, data=data)

        result_json = response.json()

        logging.debug('返回内容为：{}'.format(result_json))

        self.assertEqual(result_json['code'], 200)
        self.assertEqual(result_json['status'], True)
        logging.debug('提示信息：{}'.format(result_json['message']))

    def test_match_list_429(self):
        '匹配小红点状态修改接口'

        headers = {
            "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjE1NTJlNzBmMTY5ZGQ5OWI0MWYzNmQ3OTE4ZDQ5YzZiYzNiYjE2MzZhZjE3OGM1NzBkMDFhOTZkYmNkNGZjODViZmQ5ZTVmMGEyNjU3YTY3In0.eyJhdWQiOiIyIiwianRpIjoiMTU1MmU3MGYxNjlkZDk5YjQxZjM2ZDc5MThkNDljNmJjM2JiMTYzNmFmMTc4YzU3MGQwMWE5NmRiY2Q0ZmM4NWJmZDllNWYwYTI2NTdhNjciLCJpYXQiOjE1NzQ3MjQyMTksIm5iZiI6MTU3NDcyNDIxOSwiZXhwIjoxNTc2MDIwMjE5LCJzdWIiOiI0MjMiLCJzY29wZXMiOltdfQ.oj0zj3H6wLqiG2_juT0KiOLXATy5yWj9IWsD9j1q-QH-EVq196Rx9rWw8HRVSO7__X3-2k2U2e0ykgpOdRClPe03D3dngqVnmQmCRPUPs23q19yuWzOnmpurFVLWwpt5_PiYHrVa91JSq5HboA6QSwdafX6iM2cuRwsjXZ4xzzcj29tqIgtIXblGwzc7QejWN4KdnW13sHUOMnzJVK5XU7AMNmk7NGPolgbIphoW5Zi2JwLyQdt4h9w61hs9eEUFfqXifOGdfpmT67vK-0Me56UPQQ6nIm0QlJVDHooTYYS7z9iykzmHYTutfo4_ETrI76TDi3m2tCF2gEtBUEnyf4GwrYd-4KYTeh0BDSEQwwPo6fi-TnwBVzAWpQGTArXrOll0MMvIYXoEgMlRKN-JT6fRm0ghPmfFry8tz02jaAdm45348jxf6u5vsXFMkW0OM8fgOdpZ5VLUrsV_RpJlGZs8qaKlJsXOG_yHcuZ2paO5cshz5POIgH0wf6IAqguMsjg38L8u0OqL824R1BPS1yR-Y8uEf_HhngcOqK5jeNs9ua1qLYpZQSp1Llvjdk1E3VpApLCInJLcGqxLemPJZEUcdQ7CBvxaEVRP7ijJgDMhTQZi_FQdhjWxwRgoZn2fGGxWQ3DFJ9a3vSu5-hKgq8Lbhc1nBhFBFUZl9VEiAhA",
            "Host": "150.109.38.68",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttp/3.12.0",
            "X-Requested-With": "XMLHttpRequest"
        }

        url = '{}/api/user/match_list/429'.format(self.host)

        response = requests.get(url, headers=headers)

        result_json = response.json()

        logging.debug('返回内容为：{}'.format(result_json))

        self.assertEqual(result_json['message'], 'success')
        self.assertEqual(result_json['status'], True)
        self.assertTrue(result_json['data'] is not None)




if __name__ == '__main__':
    unittest.main()