import requests
r=requests.get('https://api.github.com/user',auth=('archerckk@163.com',
                                                        'a3203589'))
print('状态码为：%s'%r.status_code)
print(r.headers['content-type'])
print(r.encoding)
print(r.text)
print(r.json())