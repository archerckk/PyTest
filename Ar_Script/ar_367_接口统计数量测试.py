import requests



host = 'http://150.109.38.68'
token = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjAxZDEyNDNlNTE5NTJmY2E4YjM4ZmM2NTJhNTk1YTUyZDBkYmQ1ZTQyODY3N2EyNmEwM2JiODFiYWQ2YWEyNGRjMTAzZDdjZjk0NjY4NmU5In0.eyJhdWQiOiI5IiwianRpIjoiMDFkMTI0M2U1MTk1MmZjYThiMzhmYzY1MmE1OTVhNTJkMGRiZDVlNDI4Njc3YTI2YTAzYmI4MWJhZDZhYTI0ZGMxMDNkN2NmOTQ2Njg2ZTkiLCJpYXQiOjE1OTQ5ODAwODksIm5iZiI6MTU5NDk4MDA4OSwiZXhwIjoxNTk2Mjc2MDg5LCJzdWIiOiI0MjQiLCJzY29wZXMiOltdfQ.PgLoHxslqA1JKzOTOMaw17nylSAvUfxEmlz3yDLf1-Ob8ixJzUGXUZ1xybZVhYPnxNyRH9t_sVHFm5sNtzMCOQ-IKa7A1-RRv1zNDqkoMszv8Bis43VF47O4S1vOO136J-mYoX9O1rk7fD1nrOkLxcAYUvwVsbgary3Y0DZgABgQYxhV41ryZWDz5SRs8LXbnsUp7XZIbAcplWDagp5RlBw94iqolZZ_QxTdw1X3JeEK7W8dKzS8Vm96y72Sa6-9VbXeaHc5qtNIb17GmS5oUtaPW5hXogKOXBhBiPtaVu0IY1aLJErytVf9TuiYJTQc9KOq4ROBcaQL228GAKsaSdzZDd_jiMWoHmvnsrFW-jXfHAYVJUrgt8ltBbg549d8R-cS6bWiOCjPr8_SS1vXNYrQzS0hi3ASBZldpTqV-dF5hFX1YpjuH07-OqS__-UPQQvozzhpWUClU5LNXJeo-zzTBP2yaI7SPm-ZMXa4TRjKGTDYqUdcqzICuluZc4bTjL8oVP7fqrUDtnq-YS9kFmaoU9M5dqOgFDjBr6JCRVZKEosRS3ps_K5obRydjBRejekeJsT8kX59mAQUBBwBIZtfbF9KRICdu9_RRSCQV_f4sak6ifOBc1jAwDGkQF-rAWUGxVDNnFaPVNHdtOb3NdrRnNd4I7FAIhSp56v8jC0'

headers = {
    "Authorization": token,
    "Accept":"application/json",
    "Connection": "Keep - Alive",
}

url = '{}/api/user/getAgoraVideoToken'.format(host)

data = {"unique_token":"f0770546b39b9857d24a21e559f4c416","chatType":"0"}

url_get = '{}/api/user/who_likes_me_count'.format(host)

#失败接口循环
for i in range(100):
    response = requests.post(url, headers=headers,data=data)
    print(response.status_code)
    print(response.text)

#成功接口循环
# for i in range(100):
#     response=requests.get(url_get,headers=headers)
#     print(response.status_code)
#     print(response.text)