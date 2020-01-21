from tornado.options import define,options
from tornado import web
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
import os
from tornado.web import authenticated

define('port',default=8221,type=int,help='run in this port')

class MainHandler(web.RequestHandler):

    def get_current_user(self):
        return self.get_secure_cookie('username')


class LoginHandler(MainHandler):

    #get方法渲染登录界面
    def get(self):
        self.render('login.html')
    #post方法设置cookie，上传对应参数
    def post(self):
        self.set_secure_cookie('username',self.get_argument('username'))
        # self.set_secure_cookie('password',self.get_argument('password'))
        self.redirect('/')

class WelcomeHandler(MainHandler):
    #要登录才可以渲染，传入user（模板参数）
    @authenticated
    def get(self):
        self.render('welcome.html',user=self.current_user)

class LogoutHandler(MainHandler):
    #假如logout参数等于1，清除传入的cookie
    def post(self):
        if (self.get_argument('logout',None)):
            self.clear_cookie('username')
            # self.clear_cookie('password')
        self.redirect('/')
        self.write('Hello world')


if __name__ == '__main__':
    #路由配置
    urls=[
        (r'/',WelcomeHandler),
        (r'/login',LoginHandler),
        (r'/logout',LogoutHandler),
    ]

    #app参数设置
    settings={
        'login_url':'/login',
        'cookie_secret':'dsfdsfdewregfgdfgfdcxvx',
        'template_path':os.path.join(os.path.dirname(__file__),'resources')
    }

    def make_app():
        return web.Application(urls,debug=True,**settings)

    options.parse_command_line()

    app=make_app()
    server=HTTPServer(app)
    server.listen(options.port)
    IOLoop.current().start()