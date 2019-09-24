#encoding=utf-8

#1.定义一个方法 func，该func可以引入任意多的整型参数，结果返回其中最大与最小的值。
def func1(*item):
    "1."
    length=len(item)



    for i in range(length):
        if isinstance(i,int):
            if i <min:
                min=i
            if i>max:
                max=i
            else:
                pass
        else:
            return '存在非数字参数'


    return "最大值为：{},最小值为：{}".format(max,min)

print(func1(123,11))




#2.定义一个方法func，该func可以引入任意多的字符串参数，结果返回（长度）最长的字符串。

#3.定义一个方法get_doc(module)，module参数为该脚本中导入或定义的模块对象，该函数返回module的帮助文档。

#例 print get_doc(urllib),则会输出urllib这个模块的帮助文档。

#4.定义一个方法get_text(f),f参数为任意一个文件的磁盘路径，该函数返回f文件的内容。

#5.定义一个方法get_dir(folder),folder参数为任意一个文件夹，该函数返回folder文件夹的文件列表。提示（可以了解python的glob模块）