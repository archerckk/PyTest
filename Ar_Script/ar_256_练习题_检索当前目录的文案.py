# coding=utf-8
import os
file_list=os.listdir(os.curdir)
# file_list=['ar_067_easygui_统计代码量.py']
file_ext=['.py','.txt']
test_word='os'
key_dict={}
line_list=[]
for i in file_list:
    if os.path.splitext(i)[1] in file_ext:
        line=0
        try:
            with open(i,encoding='utf-8')as f:
                for j in f.readlines():
                    line += 1
                    if test_word in j:
                        line_list.append(line)
                key_dict[i]=line_list
                line_list=[]
                # print(line)
        except UnicodeDecodeError:
            pass

for i in key_dict.items():
    if i[1]!=[]:
        print(test_word,"in %s %s line"%(i[0],i[1]))