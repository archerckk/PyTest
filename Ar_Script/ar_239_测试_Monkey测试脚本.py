import easygui as g
import os
import re
import time

# msg='请选择一个你要跑脚本的产品apk包'
# default='*.apk'
# filename=g.fileopenbox(msg=msg,default=default)
# if ' ' in filename:
#     os.rename(filename,filename.replace(' ','_'))
#     filename = filename.replace(' ', '_')
# if "&"  in filename:
#     os.rename(filename,filename.replace('&','_'))
#     filename = filename.replace('&', '_')
# if "&&" in filename:
#     os.rename(filename,filename.replace('&&','_'))
#     filename=filename.replace('&&','_')
# print(filename)
# package_name_tmp=re.compile(r"package: name='(.+?)'")
# tmp_package=os.popen('aapt dump badging %s |findstr package'%filename).read()
# print(tmp_package)
# package_name=package_name_tmp.findall(tmp_package)[0]
# print(package_name)


msg='请选择一个你要跑脚本的产品包名'
title='包名选择'
package_list=[]
with open("d:"+os.sep+'package_list.txt','r',encoding='utf-8')as f:
    for i in f:
        package_list.append(i)
package_name=g.choicebox(msg=msg,title=title,choices=package_list)
package_name=package_name.strip('\n')
print('运行包名：',package_name)

#记录运行时间
runtime=time.strftime('%Y_%m_%d_%H_%M_%S',time.localtime(time.time()))
print('执行时间为：',runtime)

#间隔为小时数*60*60*1000/200（throttle的参数值）
hour=g.integerbox(msg='请输入你要运行的小时数：',lowerbound=1,upperbound=24)
events=((hour*3600*1000)/200)*3*1.5/1.12
print('事件执行数为：',int(events))

#手机monkey结果保存文件
result_file_name='/sdcard/%s_monkey_result_%s.txt'%(package_name,runtime)
print('手机生成的结果文件为：',result_file_name)

monkey='adb shell "monkey -p %s --throttle 200 --ignore-crashes --ignore-timeouts --ignore-security-exceptions --ignore-native-crashes --monitor-native-crashes -v -v -v %d > %s"'%(package_name,events,result_file_name)
print(monkey)
monkey_log=os.popen(monkey).read()
