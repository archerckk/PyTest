# # 构造header部分
# import requests
#
# host = 'http://150.109.38.68'
# token = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjI1M2VhYzQ4OTJiNTA2NjlmMDYzMjhiOTBiYjczMzU0ZjNlODcxZTQyZTY5YzllNmQwYmM5NWQ0ZTA0MjlmYjVmZjNkMTJhYjUzYTNjY2NkIn0.eyJhdWQiOiI5IiwianRpIjoiMjUzZWFjNDg5MmI1MDY2OWYwNjMyOGI5MGJiNzMzNTRmM2U4NzFlNDJlNjljOWU2ZDBiYzk1ZDRlMDQyOWZiNWZmM2QxMmFiNTNhM2NjY2QiLCJpYXQiOjE1OTcwNDY3NTYsIm5iZiI6MTU5NzA0Njc1NiwiZXhwIjoxNTk4MzQyNzU2LCJzdWIiOiI0MjMiLCJzY29wZXMiOltdfQ.b_uq7Ks5LBVkvH_456WUoFaQr305cqgffJhbeqrgCMtaLiXg_Me1yQQUDrod9xhwsczBWneIoiLsM24Qp9iMSFCOHO_hZIpEO_iVIRsGGLtH44wnycNvGbfe6uBmI1-zhrbOzV_E-Ru_g7_VHoGH3yPmimfvCVpF86qrhZc3fA1N8rs3htEWZtLi9tK7fJH_u4RCeQF9cdsQAvsfri9oKmss4c_XIcZwQijAaep-ZTgN9AnASiW56qXaWRCRC_asDBjD43Qe9uVDyzgpLvkh2zBP-JyLFsAMKx-K7GvI6QlyKE9M27hp8jSJ84i1e2hmzmfXDv4_4GaDQnKLpQwwHc6AzJw6190JOxjL_WrWRedJe6ebOSm-Fadd-9RUa5VFMhk8ptxpA-Ma4u0VatZoGrSbJtOMDAHKGB2CYUOCdKoFISKX2usUrWrhCW_uN7R5qlXv-n1aXFZtuxJsu-mS1wQAogN2GQjHjVexrTc_ZC0rPZioKtpN3I5792mtqDsM4kNdNGyHt8xofhqhjCJ-u5fhEuAAsXv1wzpyyePuS_tLmAsZShShuqO8yM_wJCKIx6Rv4Cm_nY38pQIFzbtVq7QvzhaduivYGUsKyN3WA4YhBEHXRmcoV3TQkgXaIJ1XkKfxOfJaW84_-mCcVLICjF7jDO-m7-qsjqIrgME45DU'
#
# headers = {
#     "Authorization": token,
#     "Connection": "Keep - Alive",
#     "Accept - Encoding": "gzip",
#     "User - Agent": "okhttp / 3.12.0",
#     "X - Requested - With": "XMLHttpRequest",
# }
# data={'chat_user_id':429}
#
# url = '{}/api/user/v1/instant_chat'.format(host)
# response = requests.post(url, headers=headers,data=data)
# content = response.json()
#
#
# print(content)


# dict1 = {"id": "50356270565167104", "name": "班级优化"}
# dict2 = {"id": "50356270565167104", "name": "班级优化2"}
import requests

dict1 = {"id": "503", "name": "班级优化", "info": {"uid":"2017","stuName":["张三","李四",'6666']}}
dict2 = {"id": "503", "name": "班级优化2", "info": {"uid":"2017","stuName":["张三","赵五"]}}

headers={
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"

}

url='https://www.liquid-technologies.com/online-json-to-schema-converter'
res=requests.post(url,data=dict1,headers=headers)
print(res.json())



def dict_compare(expected:dict,result:dict):
    if isinstance(expected,dict):
        for key in result:
            if key not in expected:
                print(f'多出额外字段{key}')

        for key in expected:
            if key not in result:
                print(f'缺少字段：{key}')
            else:
                dict_compare(expected[key],result[key])

    elif isinstance(result,list):
        if len(result)!=len(expected):
            print('列表结果长度跟预期结果不一致')
        for  expected_list,result_list in zip(expected,result):
            dict_compare(expected_list,result_list)
    else:
        if str(result)!=str(expected):
            print(f'{result}!={expected}')
dict_compare(dict1,dict2)
# for src_list, dst_list in zip(sorted(dict1), sorted(dict2)):
#     if str(dict1[src_list]) != str(dict2[dst_list]):
#         print(src_list,dict1[src_list],dst_list,dict2[dst_list])
#     elif