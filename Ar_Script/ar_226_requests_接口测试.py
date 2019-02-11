import requests

url='http://127.0.0.1:8000/api/get_event_list/'
r=requests.get(url,params={'eid':'1'})
result=r.json()

assert result['status']==200
assert result['message']=='success'
assert result['data']['name']=='产品发布会'
assert result['data']['address']=='北京国家会议中心'
assert result['data']['start_time']=='2016-12-08T14:29:21'
