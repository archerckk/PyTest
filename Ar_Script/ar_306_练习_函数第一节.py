#encoding=utf-8
import linecache
import os
import glob


#1.定义一个方法 func，该func可以引入任意多的整型参数，结果返回其中最大与最小的值。
def func1(*item):
    "1."
    length=len(item)
    # print(length)
    max=0
    min=0
    if length>0:
        item=list(filter(lambda k:isinstance(k,int)or k.isdigit(),item))
        item=list(map(lambda k:int(k),item))
        length=len(item)

        if length==1:
            max,min=item
            print('最大值&最小值为{}'.format(min))

        if length>1:
            # print(type(item))
            # min,max=item[0]
            min=item[0]
            max=item[0]
            for i in item:
                if i > max:
                    max=i
                else:
                    max=max

            for i in item:
                if i < min:
                    min=i
                else:
                    min=min
            return "最大值为：{}，最小值为：{}".format(max,min)


    return '存在非数字参数'

print(func1(123,11,"abc",'1233333',-99,0))




#2.定义一个方法func，该func可以引入任意多的字符串参数，结果返回（长度）最长的字符串。
def func2(*items):
    "1、遍历所有元素，将元素的长度都记录在一个列表里面，再按倒序排序列表，返回第一个元素"
    lengthList=[]
    for i in items:
        length=len(i)
        lengthList.append((i,length))
    lengthList.sort(key=lambda i:i[1],reverse=True)
    maxLength=lengthList[0][0]

    return maxLength

print("长度最长的元素为{}".format(func2("1222222222222222","123")))

#3.定义一个方法get_doc(module)，module参数为该脚本中导入或定义的模块对象，该函数返回module的帮助文档。
#例 print get_doc(urllib),则会输出urllib这个模块的帮助文档。
def get_doc(module):

    doc=module.__doc__

    return doc

print(get_doc(os))


#4.定义一个方法get_text(f),f参数为任意一个文件的磁盘路径，该函数返回f文件的内容。
def get_text(f):

    with open(f)as f:
        content=f.read()

    return content

print(get_text("product_name_list.txt"))


#5.定义一个方法get_dir(folder),folder参数为任意一个文件夹，该函数返回folder文件夹的文件列表。提示（可以了解python的glob模块）
def get_dir(folder):
    fileList=glob.glob(folder)

    return fileList
fileList=get_dir(r'D:\Download\**')
for i in fileList:
    print(i)