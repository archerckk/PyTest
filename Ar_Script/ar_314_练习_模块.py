#encoding=utf-8
import time
import datetime
import os
import pickle
import random

"""习题一：

1.1
用time模块获取当前的时间戳.
1.2
用datetime获取当前的日期，例如：2013 - 03 - 29
1.3
用datetime返回一个月前的日期：比如今天是2013 - 3 - 29
一个月前的话：2013 - 02 - 27"""

#1.1 用time模块获取当前的时间戳
print(time.time())

#1.2 用datetime获取当前的日期，例如：2013 - 03 - 29
today=datetime.date.today().isoformat()
print(today)

#1.3
month=(datetime.datetime.today()-datetime.timedelta(days=30)).__format__('%Y-%m-%d')
print(month)

"""
习题二:
1
用os模块的方法完成ping
www.baidu.com
操作。
2
定义一个函数kouzhang(dirpwd)，用os模块的相关方法，返回一个列表，列表包括：dirpwd路径下所有文件不重复的扩展名，如果有2个
".py"
的扩展名，则返回一个
".py"。

习题三：

定义一个函数xulie(dirname, info)
参数：dirname: 路径名，info: 需要序列化的数据，功能：将info数据序列化存储到dirname路径下随机的文件
"""

#2.1
# result=os.popen("ping www.baidu.com").read()
# print(result)

#2.2
def kouzhang(dirpwd):
    if not os.path.exists(dirpwd):
        return '文件目录不存在'
    ext_list=[]
    file_list=os.listdir(dirpwd)
    if file_list==[]:
        return '这是一个空目录'

    for file in file_list:
        if os.path.isdir(file):
            ext_list.append('文件夹')
        else:
            ext_list.append(os.path.splitext(file)[1])

    ext_list=list(set(ext_list))

    return ext_list

print(kouzhang(os.curdir))

#2.3
info='I just want to test pickle'
dirname='./resources/pickle_test'
def xunlie(dirname,info):
    p_file_list=os.listdir('./resources/pickle_test')
    if len(p_file_list)==0:
        return '这是一个空文件夹，不存在可写入文件'

    max_length=len(p_file_list)
    random_num=random.randint(0,max_length-1)
    file=open(dirname+os.sep+p_file_list[int(random_num)],'wb')
    pickle.dump(info,file=file)
    file.close()

xunlie(dirname,info)