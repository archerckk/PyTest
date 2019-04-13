import pyperclip
#复制库

#指令字典
command_dict={
    "cdad":"cd /home/avazudev/ad/new_app_ad_engine_1/bin",
    "psad":"ps -ef|grep new_app_ad_engine_1 |grep -v grep",
    "killad":"killall -9 new_app_ad_engine_1",
    "startad":"./new_app_ad_engine_1 -c ../conf/dev/new_app_ad_engine_framework.cfg -f ../conf/dev/new_app_ad_engine.cfg -d",
    "cdcf":"/home/avazudev/app/app_config_engine/conf/dev",
    "cdapp":"/home/avazudev/app/app_config_engine/meta/config/appconfig"
}
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