#encoding=utf-8

import shutil
import os
import re

"""
1、查找文件夹里面的文件
2、找出文件名前缀
3、分析文件名剩下的数字内容
4、处理文件名的数字大小
5、重新命名文件名
"""

file_list=os.listdir(os.curdir+os.sep+'resources')
file_target_list=[]
tmp_list=[]
reg_num=re.compile(r'test(\d+)')
for i in file_list:
    if i.startswith('test'):
        tmp_list.append(i)

for i in tmp_list:
    if reg_num.search(i)!=None:
        file_target_list.append(i)
    else:
        continue
length=len(file_target_list)

for i in range(length):
    if i<length-1:
        tmp_num = reg_num.search(file_target_list[i]).group(1)
        tmp_num2=reg_num.search(file_target_list[i+1]).group(1)
        compare=int(tmp_num2)-int(tmp_num)
        if compare!=1:
            a1=os.getcwd()+os.sep+'resources'+os.sep+file_target_list[i+1]
            a2=os.getcwd()+os.sep+'resources'+os.sep+'test%03d'%(int(tmp_num)+1)
            file_target_list[i+1]='test%03d'%(int(tmp_num)+1)
            os.rename(a1,a2)

    else:
        break


for i in os.listdir(os.getcwd()+os.sep+'resources'):
    if reg_num.search(i) != None:
        print(i)
