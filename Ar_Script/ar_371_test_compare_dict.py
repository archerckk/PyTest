# 构造header部分
import requests

host = 'http://150.109.38.68'
token = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjI1M2VhYzQ4OTJiNTA2NjlmMDYzMjhiOTBiYjczMzU0ZjNlODcxZTQyZTY5YzllNmQwYmM5NWQ0ZTA0MjlmYjVmZjNkMTJhYjUzYTNjY2NkIn0.eyJhdWQiOiI5IiwianRpIjoiMjUzZWFjNDg5MmI1MDY2OWYwNjMyOGI5MGJiNzMzNTRmM2U4NzFlNDJlNjljOWU2ZDBiYzk1ZDRlMDQyOWZiNWZmM2QxMmFiNTNhM2NjY2QiLCJpYXQiOjE1OTcwNDY3NTYsIm5iZiI6MTU5NzA0Njc1NiwiZXhwIjoxNTk4MzQyNzU2LCJzdWIiOiI0MjMiLCJzY29wZXMiOltdfQ.b_uq7Ks5LBVkvH_456WUoFaQr305cqgffJhbeqrgCMtaLiXg_Me1yQQUDrod9xhwsczBWneIoiLsM24Qp9iMSFCOHO_hZIpEO_iVIRsGGLtH44wnycNvGbfe6uBmI1-zhrbOzV_E-Ru_g7_VHoGH3yPmimfvCVpF86qrhZc3fA1N8rs3htEWZtLi9tK7fJH_u4RCeQF9cdsQAvsfri9oKmss4c_XIcZwQijAaep-ZTgN9AnASiW56qXaWRCRC_asDBjD43Qe9uVDyzgpLvkh2zBP-JyLFsAMKx-K7GvI6QlyKE9M27hp8jSJ84i1e2hmzmfXDv4_4GaDQnKLpQwwHc6AzJw6190JOxjL_WrWRedJe6ebOSm-Fadd-9RUa5VFMhk8ptxpA-Ma4u0VatZoGrSbJtOMDAHKGB2CYUOCdKoFISKX2usUrWrhCW_uN7R5qlXv-n1aXFZtuxJsu-mS1wQAogN2GQjHjVexrTc_ZC0rPZioKtpN3I5792mtqDsM4kNdNGyHt8xofhqhjCJ-u5fhEuAAsXv1wzpyyePuS_tLmAsZShShuqO8yM_wJCKIx6Rv4Cm_nY38pQIFzbtVq7QvzhaduivYGUsKyN3WA4YhBEHXRmcoV3TQkgXaIJ1XkKfxOfJaW84_-mCcVLICjF7jDO-m7-qsjqIrgME45DU'

headers = {
    "Authorization": token,
    "Connection": "Keep - Alive",
    "Accept - Encoding": "gzip",
    "User - Agent": "okhttp / 3.12.0",
    "X - Requested - With": "XMLHttpRequest",
}
data={'chat_user_id':429}

url = '{}/api/user/v1/instant_chat'.format(host)
response = requests.post(url, headers=headers,data=data)
content = response.json()


print(content)