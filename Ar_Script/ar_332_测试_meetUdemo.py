import unittest
import requests
import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s')



environment='test'
if environment == 'test':
    host = 'http://150.109.38.68'
    token='Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjVkODM0MTc1N2VjZjIyZjQ5OTAzNDc0NjFjOTFmZGIxZmQwYmJiNTg2NWJiNWU0MDZmZTEyMzdlMGIwYTBkMjc1ZDA5YWMyZGE4YjAwMTc0In0.eyJhdWQiOiIyIiwianRpIjoiNWQ4MzQxNzU3ZWNmMjJmNDk5MDM0NzQ2MWM5MWZkYjFmZDBiYmI1ODY1YmI1ZTQwNmZlMTIzN2UwYjBhMGQyNzVkMDlhYzJkYThiMDAxNzQiLCJpYXQiOjE1NzUwMjM3ODUsIm5iZiI6MTU3NTAyMzc4NSwiZXhwIjoxNTc2MzE5Nzg1LCJzdWIiOiI0MjMiLCJzY29wZXMiOltdfQ.C4k3UjIoYa6moWxJjjp9mraBzsugEFBl92j5FiEmwn_fJQHkfPoWyteGy4uSr4N0erFKGIErNzhY0R4WK4F1WpvKzekNSYsIGIeX47cVzb4UXSJzd7MQ7uqVJL3_miRAu0e-Ofm9vcCq_hqtuX6wbpQsSdvvKosBAETtfnutjkAQc-rJALvG2KR2tr90fnXbgCSE_voxieOWrQUgnBIR_KvUL9cZ6E-RrtkoHYei7Kp41B-QBMmg48aXsKz9wjvLG3DJNXQnIlwJjBdAa3hTk0s-HPzTB4cih8hGcTUcFfRY5AI7J98SI-777jJ6q4ECBO88LfOcgVy6IWOCXcMQDXlT7KZ9silx2z2CkWvuSuR-3qTOV1Gi2FW3pIpbgQkIJUx48i-Lk01i14NXegxfT4lr9yp7MOiz6IlEL9GmytWP6X_dvroh_EzZunOcH_hp0C6Mo_txwM5m5NJ7qbEAGrPbuPKPrIlYmwA6AMpudp42mSryYMEClccwaXrt0EZiVC3QZkJaIQYyFkXb9YPRCyRaFZMML1ykUxKyXzWCe5Iw0-eewx6kDLxKpyn3l2NEC6QIGW5b_LjyIIlcBVGgJHOEkJTkE1kX6lhdrt76GPS-_RcMckvga6DTLvsla2DCgYkMYGxQ9mF57gKQqoM5-9jRDxVMpn9essDCdE7hI7s'
    # token = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImQzZTRhZDU5NzQ4NzU1ZjMwODI5YmYyNDQzN2JhODViODY3ODNhNzhhYmZhY2I4MGI3ODY1YTQ5OWJiNmVjZmU1MTM2ZjlmNzhiZDg5N2NhIn0.eyJhdWQiOiIyIiwianRpIjoiZDNlNGFkNTk3NDg3NTVmMzA4MjliZjI0NDM3YmE4NWI4Njc4M2E3OGFiZmFjYjgwYjc4NjVhNDk5YmI2ZWNmZTUxMzZmOWY3OGJkODk3Y2EiLCJpYXQiOjE1NzQ0Mjk3NDgsIm5iZiI6MTU3NDQyOTc0OCwiZXhwIjoxNTc1NzI1NzQ4LCJzdWIiOiI0MjkiLCJzY29wZXMiOltdfQ.COE8VPyJQOJSPWEG0i_iOcm81Rg0Y9a5gCOyeuHJfqHdvsHAOm2jkAA6nfU_WhmqXrZlNA64GrqNi9BjE8sFlMUcwRBl5EjJap_p2X33uxBtM-u4Ge1nr3H8phBYPZK6sOmGSMYuwWFo6fdem3wot5swz2eKGKrCA1Pn4aSH5L87vidfF2-FJfo5Zl45ePrzr68__MkqQyce7LWj-SGxUCejkBv7PTJputtg-7Azz8GJKl4QAyOAmhCqFTwXE4dy29jyMqdBKDEf1cTlhhiNayyLLY_m4om-MtVj9KNZWY09xnMq9WBynKU3_s_nSCLVH2po0jfUt1_o62TWKL1UAN9fBGY9Zl6d-jIwVt8WUVoJikaUahXLFzGaF880nGmYSxs_DG2-VRrLAhlm5lWfvwYH3DfGBOFp-Imk9a7sBpIKZAJ2kIjPl6Oo-RapPTNwAE3rsYsSQD0igt5_jtn55BfMKspn8RJf6leKsTCs0lSOe2qpnvU94SUTnbGbqNaLZrvDDYJQu_BRO5uZWbBDElETimMf4q4dQMEvHSC-NqiViiisgsHyztDKUsrcz_orfEmxw2yGeumobpKDt8jc0HNEJ3mPQnZKV7zs6KrDNlwDbKNvreV-ARt6rZRuLhTuKjQcKcmR0nFB6KwlfDvOfYC7AbJYdfAqFjEbhw5DE0A'
elif environment == 'normal':
    token = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImY3NGEzNTUwMTdkYjhkODBiOWMyMzFkNDhhMTc4ZDI1YjE5NTc2YzlkMGQ2ZDJkNWU0Nzk3MmQzMzgzYmNiYzQzYzdkNTgzMmVkYTBiZGFkIn0.eyJhdWQiOiIxIiwianRpIjoiZjc0YTM1NTAxN2RiOGQ4MGI5YzIzMWQ0OGExNzhkMjViMTk1NzZjOWQwZDZkMmQ1ZTQ3OTcyZDMzODNiY2JjNDNjN2Q1ODMyZWRhMGJkYWQiLCJpYXQiOjE1NzQ4NTc2MDgsIm5iZiI6MTU3NDg1NzYwOCwiZXhwIjoxNjA2NDgwMDA4LCJzdWIiOiI2MiIsInNjb3BlcyI6W119.fj92n_Rl1w_dG985eH6sv4YbqG1cccu3Rv0-GDhgsJ3bwmBT3gLamNHYNyw9RYXvezrIhIhgSvXrVffiVUTFnC6tWcG6_tMF2Hl5Xa8n-6qz4Bm0j-gJx5SJie8UDjzwTaSu6UP2tC8JL3uuq5fL_Pf35OPaOaHBjBoM6qP-iskUd3qQwyWw-c1eNQfK-Yrz-0iZSOGGYRHvR3DWh4GIAbVr7CAkBNElJ0vjAMxAJowda5et3_eQ0yHLwLRi3AiAImX7Qk_3dzPOoqE9UFqHMUrGiJUoVVvIOiVAeWq1LxrXninCRuTNEmfWmu915CF7suc79rS_avj-ZED1VlOYzUwhQhgxzHwnhpsBTvK5rkTciqwVkxiP9pxP1SnOKHxzJPd3-8yNCKM03QXpsKUGqzSQgHVkYFJODYoWgy7wZlLIoOWk5zWbN2r5EKWXdJQrcxW3skwLuoOxyipVNlaQgLAdKGrNH7ZT2KO82SnRUUluJoMWV-yzjOhsGmldMjAdpT_6OoMxhydQfWzg4WpBqvYeFCSO6M2QNZuSCTEtdw8OFNGTwmekW8xiu7bv1lAQ5JsvQr11_LziDrBSne-fyCnwDHaod0YeS8hp2xNdiPO7298Rz2LLQOP28KtK8X5TeA6Fv155YE9KblilCyz49Cc90eyE1K1ZAscERRyEwAU'
    host = 'http://www.meetuapp.info'

class TestDemo(unittest.TestCase):


    def test_update_profile(self):
        headers = {
        "Authorization":token,
        "Accept": "application/json"
        }

        data={
        "chat_user_id": "429",
        }

        url = '{}/api/user/instant_chat'.format(host)

        response=requests.post(url,headers=headers,data=data)

        result_json = response.json()

        logging.debug('返回内容为：{}'.format(result_json))


        # self.assertEqual(result_json['status'],'DISLIKED')
        # self.assertEqual(result_json['statuscode'],3)
        # self.assertEqual(result_json['message'] ,'User disliked successfully')
        # logging.debug('提示信息：{}'.format(result_json['message']))