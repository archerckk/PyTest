#encoding=utf-8

#1 定义一个方法get_fundoc(func),func参数为任意一个函数对象，返回该函数对象的描述文档，如果该函数没有描述文档，则返回"not found"
def testFun():
    '这是一个函数的说明'
def testFun2():
    pass


def get_fundoc(func_function):
    """
    1、用__doc__方法获取到函数的描述文件
    2、判断返回的内容是否为空
    3、给予不一样的返回值
    """
    result=func_function.__doc__
    if callable(func_function):
        if result!= None:
            # print(result)
            return result
        else:
            return 'not found'
    return '传入参数有误'

# assert get_fundoc(testFun)==  """
#     这是一个函数的说明
#     :return:
#     """

str1='这是一个函数的说明'

assert get_fundoc(testFun2)=='not found'
assert get_fundoc(123)=='传入参数有误'
assert get_fundoc(testFun)==str1


#2 定义一个方法get_cjsum(),求1-100范围内的所有整数的平方和。返回结果为整数类型。

def get_cjsum():
    sum=0
    for i in range(1,101):
        sum+=i*i

    return sum

# print(get_cjsum())

assert type(get_cjsum())==int

"""
#3 定义一个方法list_info(list), 参数list为列表对象，怎么保证在函数里对列表list进行一些相关的操作，不会影响到原来列表的元素值，比如：

a = [1,2,3]

def list_info(list):
   '''要对list进行相关操作，不能直接只写一句return[1,2,5]，这样就没意义了'''

print list_info(a):返回结果：[1,2,5]

print a 输出结果：[1,2,3]

写出函数体内的操作代码。
"""

a=[1,2,3]
def list_info(item_list):
    newList=item_list[:]

    # newList=[i*i for i in newList]
    newList.append('abc')
    return newList

assert a==[1,2,3]
assert len(list_info(a))==len(a)+1



#4 定义一个方法get_funcname(func),func参数为任意一个函数对象，需要判断函数是否可以调用，如果可以调用则返回该函数名(
#类型为str)，否则返回 “fun is not function"。
def get_funname(func_function):
    """
    1、用__doc__方法获取到函数的描述文件
    2、判断返回的内容是否为空
    3、给予不一样的返回值
    """

    if callable(func_function):
        name = func_function.__name__
        return name

    return 'fun is not function'

assert get_funname('fu')=='fun is not function'
assert get_funname(get_funname)=='get_funname'
assert type(get_funname(get_funname))==str