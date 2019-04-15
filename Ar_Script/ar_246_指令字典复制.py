import pyperclip
import os
#复制库

#测试代码
# command_dict={
#     "cdad":"cd /home/avazudev/ad/new_app_ad_engine_1/bin",
#     "psad":"ps -ef|grep new_app_ad_engine_1 |grep -v grep",
#     "killad":"killall -9 new_app_ad_engine_1",
#     "startad":"./new_app_ad_engine_1 -c ../conf/dev/new_app_ad_engine_framework.cfg -f ../conf/dev/new_app_ad_engine.cfg -d",
#     "cdcf":"/home/avazudev/app/app_config_engine/conf/dev",
#     "cdapp":"/home/avazudev/app/app_config_engine/meta/config/appconfig",
#     "cdne":"cd log_server/data/app_tracking_nw_ne",
#     "cdnx":"cd log_server/data/app_tracking_nw_nx",
#     "grepdadian":"grep -r anative.appwall.demo",
#     "ac":"com.aplus.camera.android",
#     "ah":"com.aplushoroscope",
#     "dh":"com.day.horoscope.pro.android.info",
#     "mc":"com.max.camera.android",
#     "cpe":'com.copo.photo.editor.android',
#     "ic":'com.in.camera.android',
#     "ch":'com.copohoroscope',
#     "gp":'com.android.vending',
#     "pc":'com.pika.camera.android'
# }

#将字典内容外置到外面的txt文件
command_dict={}
with open(os.curdir+os.sep+"command_dict.txt",'r')as dict_file:
    for i in dict_file:
        key,value=i.split(':')
        command_dict[key]=value

#声明一个空的字符串变量
key=''

#一直循环执行
while True:
    #假如key的值为exit，中断循环
    if key=="exit":
        break
    else:
        #输入key的值
        key=input('请输入要复制的指令：')
        #判断key的值是否在字典的键里面，有就复制，没有就打印，不在键里面
        if key in command_dict.keys():
            pyperclip.copy(command_dict[key])
        else:
            print("你输入你的指令有误！")

