import time
import logging as log
import easygui as g
import os

log.basicConfig(level=log.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s')

def monkey_run(package_name):

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
    log.debug('开始运行momkey')
    monkey='adb shell "monkey -p %s --throttle 200 --ignore-crashes --ignore-timeouts --ignore-security-exceptions --ignore-native-crashes --monitor-native-crashes -v -v -v %d  2>%s "'%(package_name,events,result_file_name)
    print(monkey)
    log.debug(monkey)
    monkey_log=os.popen(monkey).read()
    log.debug(monkey_log)