# coding=utf-8
import os
target_list=os.popen('ls')
for i in target_list:
    os.popen('dpkg -i %s'%i)

