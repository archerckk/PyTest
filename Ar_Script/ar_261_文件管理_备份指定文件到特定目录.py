#encoding=utf-8

import shutil
import os

'''
1、查找当前目录下面的所有文件
2、筛选特定后缀名字的文件
3、复制到这些后缀的文件到新的目录
4、打印新的目录下面的文件的绝对路径
'''

file_tuple=os.walk(os.getcwd())
file_list=[]
file_target_list=[]
bk_file='d:%sbk_file'%os.sep

if os.path.exists(bk_file):
    print('备份目录已存在，不用新建')
else:
    print('新建备份目录：%s'%bk_file)

for i in file_tuple:
    for j in i[2]:
        file_list.append(os.path.join(i[0],j))


for i in file_list:
    if os.path.splitext(os.path.basename(i))[1]=='.py':
        file_target_list.append(i)

for i in file_target_list:
    shutil.copy(i,bk_file+os.sep+os.path.basename(i))

print('\n当前目录的文件列表信息为：')
for i in os.listdir(bk_file):
    print('\t\t\t',i)