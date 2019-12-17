from tornado.ioloop import IOLoop
import tornado.httpserver
import tornado.web


app=tornado.web.Application()
server=tornado.httpserver.HTTPServer(app)
server.listen(8222)
IOLoop.current().start()

