#encoding=utf-8
import functools

def judgeInput(func):
    @functools.wraps(func)
    def warpper():
        result=func()
        if isinstance(result,int):
            print('类型正确')
        else:
            print('输入有误!')
        return result
    return warpper

@judgeInput
def intInput():

    result=int(input('请输入一个数字：'))

    return result

intInput()