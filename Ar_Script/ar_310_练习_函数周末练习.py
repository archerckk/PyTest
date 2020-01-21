#coding=utf-8

import random
import os
import requests
import urlparser
import urllib.parse

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
# for i in l:
#     print(i,end=' ')



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


#6、定义一个函数，可以获取到url的网页内容并且保存到一个文件目录下方，随机生成一个文件名

def func6(url,path):

    if not(url.startswith('http://')or url.startswith('https://')):
        return '传入的url参数不符合规范'

    if not os.path.isdir(path):
        return 'path参数不是一个有效的文件夹'

    body=requests.get(url)
    # content=body.text

    intRandom=random.randint(1,1000)
    fileObject=path+os.sep+'test{}.txt'.format(intRandom)

    with open(fileObject,'wb')as f:
        for chunk in body.iter_content(chunk_size=128):
            f.write(chunk)

    return fileObject

# print(func6('http://www.vgooo.com/',os.curdir))


#7、定义一个函数，可以返回一个网页里面的url数量

def func7(url):

    if not(url.startswith('http://')or url.startswith('https://')):
        return '传入的url参数不符合规范'

    body = requests.get(url)
    content=body.text
    result=content.count('a href=')

    # result=len(content.split('a href='))-1

    return result

print(func7('http://www.vgooo.com/'))


#8、合并一个文件夹里面的所有的文件内容

def func8(filePath):

    if not os.path.isdir(filePath):
        return '你所传入的参数不是一个文件夹'

    for file in os.listdir(filePath):
        fileObject=os.path.join(filePath,file)
        if os.path.isdir(file):
            func8(file)
        else:
            result=open(os.curdir+os.sep+'result.txt','ab')
            f=open(fileObject,'r')
            content=f.read().encode('utf-8')
            print(content)
            result.write(content)
            f.close()
            result.close()

# print(func8(r'D:\Pytest\Ar_Script\resources\test'))


#9 获取的到一个url后面的参数，并且返回一个字典格式：如：www.baidu.com/api?a=123&b=12，返回{a:123,b:12}
def url_dict(url):
    if not(url.startswith('http://')or url.startswith('https://')):
        return '传入的url参数不符合规范'

    urlResult=urllib.parse.urlparse(url).query
    tmp_dict=urllib.parse.parse_qs(urlResult)
    find_dict=dict([(k,v[0]) for k,v in tmp_dict.items()])

    return find_dict
print(url_dict('http://www.baidu.com?abc=1223&a=222'))


#10 删除一个文件夹里面的所有文件
def del_all_file(filePath):

    if not os.path.exists(filePath):
        return '你所传入的目录并不存在'

    if not os.path.isdir(filePath):
        return '你所传入的参数不是一个文件夹'

    for file in os.listdir(filePath):
        fileObject=os.path.join(filePath,file)
        if os.path.isdir(file):
            del_all_file(file)
        else:
            os.remove(fileObject)
            print("删除文件{}".format(fileObject))

del_all_file(r'D:\Pytest\Ar_Script\resources\test')