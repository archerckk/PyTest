import requests

test_url='http://www.163.com'
'设置头部参数模拟手机访问'
headers={'User-Agent':'Android/H60-L01/4.4.2/'}
#Mozilla/5.0 (Windows NT 10.0; WOW64; rv:62.0) Gecko/20100101 Firefox/62.0
response=requests.get(test_url)
print(response.text)
print('*'*50)
print(response.status_code)
print('*'*50)
print(response.headers)