#coding=utf-8
import string

'''
1.定义一个func(name)，该函数效果如下。
assert func("lilei") = "Lilei"
assert func("hanmeimei") = "Hanmeimei"
assert func("Hanmeimei") = "Hanmeimei"
'''

def func(name):
    if isinstance(name,str):
        name=name.title()
        return name
    else:
        return "传入非字符串参数"

assert func("lilei") == "Lilei"
assert func("hanmeimei") == "Hanmeimei"
assert func("Hanmeimei") == "Hanmeimei"


"""
2.定义一个func(name,callback=None),效果如下。
assert func("lilei") == "Lilei"
assert func("LILEI",callback=string.lower) == "lilei"
assert func("lilei",callback=string.upper) == "LILEI"

"""
def func2(name,callback=None):
    if isinstance(name,str) and callback==None:

        return name.capitalize()
    elif isinstance(name,str) and callback!=None:

        return callback(name)
    else:
        return "传入非字符串参数"

assert func2("lilei") == "Lilei"
assert func2("LILEI",callback=str.lower) == "lilei"
assert func2("lilei",callback=str.upper) == "LILEI"


"""
3.定义一个func(*kargs),效果如下。

l = func(1,2,3,4,5)
for i in l:
	print i,
#输出 1 2 3 4 5

l = func(5,3,4,5,6)
for i in l:
	print i
#输出 5 3 4 5 6
"""

def func3(*kargs):
    return kargs

l=func3(5,5,3,4,1)
for i in l:
    print(i,end=' ')



"""
4.定义一个func(*kargs)，该函数效果如下。

assert func(222,1111,'xixi','hahahah') == "xixi"
assert func(7,'name','dasere') == 'name'
assert func(1,2,3,4) == None

"""

def func4(*kargs):
    for i in kargs:
        if  isinstance(i,str):
            return i
    return None

assert func4(222,1111,'xixi','hahahah') == "xixi"
assert func4(7,'name','dasere') == 'name'
assert func4(1,2,3,4) == None




"""
5.定义一个func(name=None,**kargs),该函数效果如下。

assert func(“lilei”) == "lilei"
assert func("lilei",years=4) == "lilei,years:4"
assert func("lilei",years=10,body_weight=20) == "lilei,years:4,body_weight:20"
"""

def func5(name=None,**kargs):
    lis= ["{}:{}".format(k,v) for k,v in kargs.items()]
    lis.insert(0,name)
    return ','.join(lis)

assert func5('lilei') == "lilei"
assert func5("lilei",years=4) == "lilei,years:4"
assert func5("lilei",years=10,body_weight=20) == "lilei,years:10,body_weight:20"
