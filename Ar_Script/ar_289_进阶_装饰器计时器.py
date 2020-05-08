# encoding=utf-8

import time
import functools


def timeCounter(fun):
    @functools.wraps(fun)
    def warp(*args, **kwargs):
        start = time.perf_counter()
        run = fun()
        end = time.perf_counter()
        result = end - start
        print('{}执行了{}秒'.format(fun.__name__, result))

        return run

    return warp


@timeCounter
def realFun():
    result = 0
    for i in range(10000000):
        result = result + i
    return result


realFun()

"""
网站登录例子
"""

is_login = True


def case3():
    def login_required(func):
        def wrapper():
            if is_login == True:
                func()
            else:
                print('请跳转到登录页面')

        return wrapper

    @login_required
    def edit():
        print('执行编辑成功')

    @login_required
    def update():
        print('执行升级成功')

    edit()
    update()


case3()

"网站登录，需要升级1"


def case4():
    def login_required(func):
        def wrapper(*args, **kwargs):
            if is_login == True:
                func(*args, **kwargs)
            else:
                print('请跳转到登录页面')

        return wrapper

    @login_required
    def edit(username):
        print('{},执行编辑成功'.format(username))

    @login_required
    def update(title, content):
        print('{},{}执行升级成功'.format(title, content))

    edit('测试用户')
    update('测试标题', '测试内容')


case4()

"""网站登录，新增需要区分前后台用户"""


def case5():
    def login_required(site='front'):
        def outside_wrapper(func):
            @functools.wraps(func)
            def inner_wrapper(*args, **kwargs):
                if is_login == True:
                    func(*args, **kwargs)
                else:
                    if site == 'front':
                        print('请跳转到登录页面')
                    else:
                        print('请登录到后台登录页面')

            return inner_wrapper

        return outside_wrapper

    @login_required('front')
    def edit(username):
        print('{},执行编辑成功'.format(username))

    @login_required('test')
    def update(title, content):
        print('{},{}执行升级成功'.format(title, content))

    edit('测试用户')
    update('测试标题', '测试内容')
    print(update.__name__)

case5()

class case6(object):

    __slots__ = ('name','age')
    def __init__(self):
        self.name='tom'

c=case6()
c.age=18
print(c.age)