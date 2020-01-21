from tornado.ioloop import IOLoop
import tornado.httpserver
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self,**kwargs):
        name=kwargs.get('name')
        self.write("<h1>Tornado Index</h1>")
        self.write('Hello ,{}'.format(name))

def make_app():
    return tornado.web.Application([
        (r'/',MainHandler),
        (r'/(?P<name>.+)',MainHandler),
    ])

if __name__ == '__main__':
    app=make_app()
    app.listen(8222)
    IOLoop.current().start()

