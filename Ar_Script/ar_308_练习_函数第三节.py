#encoding=utf-8

#1 定义一个方法get_fundoc(func),func参数为任意一个函数对象，返回该函数对象的描述文档，如果该函数没有描述文档，则返回"not found"
def testFun():
    """
    这是一个函数的说明
    :return: 
    """
def testFun2():
    pass


def get_fundoc(func_function):
    """
    1、用__doc__方法获取到函数的描述文件
    2、判断返回的内容是否为空
    3、给予不一样的返回值
    """
    result=func_function.__doc__
    if type(func_function)=='function':
        if result!='':
            return result
        else:
            return 'not found'

# assert get_fundoc(testFun)==  """
#     这是一个函数的说明
#     :return:
#     """
assert get_fundoc(testFun2)=='not found'

#2 定义一个方法get_cjsum(),求1-100范围内的所有整数的平方和。返回结果为整数类型。


"""
#3 定义一个方法list_info(list), 参数list为列表对象，怎么保证在函数里对列表list进行一些相关的操作，不会影响到原来列表的元素值，比如：

a = [1,2,3]

def list_info(list):
   '''要对list进行相关操作，不能直接只写一句return[1,2,5]，这样就没意义了'''

print list_info(a):返回结果：[1,2,5]

print a 输出结果：[1,2,3]

写出函数体内的操作代码。
"""



#4 定义一个方法get_funcname(func),func参数为任意一个函数对象，需要判断函数是否可以调用，如果可以调用则返回该函数名(
#类型为str)，否则返回 “fun is not function"。