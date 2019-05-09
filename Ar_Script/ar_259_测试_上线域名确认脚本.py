import os
import subprocess
import time
import easygui as g
import re

"""
1.获取文件的路径
2.用路径获取到包名
3.卸载包名
4.安装app
5.先开启日志抓取
5.打开app
6.分析日志文件抓取各个域名
    通过包名抓取cf配置，再得到主域名
    通过包名抓取mo配置
    通过包名
"""

def getPackagInfo():
    msg='请选择你要检查的apk安装包'
    title='文件选择'
    default="*.apk"
    filePath=g.fileopenbox(msg=msg,title=title,default=default)
    print(filePath)
    command='aapt dumpsys badging %s > packageInfo.txt'%filePath
    packInfoFile='./packageInfo.txt'
    list1=[]

    # with open(packInfoFileOj,'w',encoding='utf-8')as f:
    handle=subprocess.Popen(command,stdout=subprocess.PIPE,shell=True)
    time.sleep(2)
    reg_packageName=re.compile(r"package: name='(.+?)'")
    reg_launchableActivity=re.compile(r"launchable-activity: name='(.+?)'")
    log=''
    with open(packInfoFile, encoding='utf-8')as f :
        for i in f:
            log+=i

    packageName=reg_packageName.search(log).group(1)
    lanuchableActivity=reg_launchableActivity.search(log).group(1).strip()
    print(packageName)
    print(lanuchableActivity)

    return filePath,packageName,lanuchableActivity

def uninstallApp(packageName):
    command='adb uninstall %s'%packageName
    handle=subprocess.Popen(command,shell=True,stdout=subprocess.PIPE)

    return handle

def judgeRunning(function):
    while True:


        if function.poll()!=None:
            print('指令执行完成')
            break
        else:
            continue

# filePath,packageName,lanuchableActivity=getPackagInfo()
# handle=uninstallApp(packageName)
handle=subprocess.Popen("ping www.baidu.com",shell=True,stdout=subprocess.PIPE)
a=handle.stdout.read()
a=a.decode('gbk')
print(a)
# print(a.decode('utf-8'))
# print(str(handle.stdout.encode("utf-8")))


# judgeRunning(handle)