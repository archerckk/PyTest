#encoding=utf-8

import time
import functools

def timeCounter(fun):
    @functools.wraps(fun)
    def warp(*args,**kwargs):
        start=time.perf_counter()
        run=fun()
        end=time.perf_counter()
        result=end-start
        print('{}执行了{}秒'.format(fun.__name__,result))

        return run
    return warp

@timeCounter
def realFun():
    result=0
    for i in range(10000000):
        result=result+i
    return result

realFun()