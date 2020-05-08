from functools import wraps

is_login=False

def login_required(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if is_login:
            func(*args,**kwargs)
        else:
            print('你还没登录，跳转到登录页面')
    return wrapper




class Flask(object):

    def __init__(self):
        self.url_maps={}

    def router(self,url):
        def outside_wrapper(func):
            self.url_maps[url]=func.__name__
            def inside_wrapper(*args,**kwargs):
                func(*args,**kwargs)
            return inside_wrapper
        return outside_wrapper


    def run(self):

        while True:
            url=input('请输入网址：')
            func_view=self.url_maps.get(url)

            if func_view:
                exec(func_view+'()')#将字符串当成可运行对象执行
            else:
                print('你访问的的地址不存在')

app=Flask()

@app.router('/')
def index():
    print('index page')

@app.router('/list/')
def article_list():
    print('article page')

@app.router('/edit/')
@login_required
def edit():
    print('用户信息更新成功')

app.run()