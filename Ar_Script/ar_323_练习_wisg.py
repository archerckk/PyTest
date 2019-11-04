from wsgiref.simple_server import make_server
from ar_324_练习_wisg_show import application

#配置服务器
httpd=make_server('',8000,application)

print('Server HTTP on port 8000...')

#启动服务器
httpd.serve_forever()