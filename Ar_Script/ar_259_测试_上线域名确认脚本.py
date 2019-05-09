import os
import subprocess
import time
import easygui as g
import re
import threading
"""
1.获取文件的路径
2.用路径获取到包名
3.卸载包名
4.安装app
    新建日志开启文件
5.先开启日志抓取
5.打开app
6.分析日志文件抓取各个域名
    通过包名抓取cf配置，再得到主域名
    通过包名抓取mo配置
    通过包名
"""

def openLog():
    add_debug_list = [
        "adb shell touch sdcard/abcxxxtestmodefilexxx",
        "adb shell touch sdcard/logger.ChargerSdk.debug",
        "adb shell touch sdcard/logger.CleanerSdk.debug",
        "adb shell touch sdcard/logger.DefenderSdk.debug",
        "adb shell touch sdcard/logger.CommonSdk.debug",
        "adb shell touch sdcard/logger.CoverSdk.debug",
        "adb shell touch sdcard/logger.innerSdk.debug",
        "adb shell touch sdcard/logger.AnalyticsSdk.debug",
        "adb shell touch /sdcard/stoooooorm",
        "adb shell touch sdcard/moooooon",
        "adb shell touch sdcard/appsurfacetestmode",
        "adb shell touch sdcard/xxtestmodexx"
    ]
    for i in add_debug_list:
        os.popen(i)
    print("files creat successful!")

def getPackagInfo():
    msg='请选择你要检查的apk安装包'
    title='文件选择'
    default="*.apk"

    filePath=g.fileopenbox(msg=msg,title=title,default=default)
    if ' ' in filePath:
        os.rename(filePath, filePath.replace(' ', '_'))
        filePath = filePath.replace(' ', '_')
    if "&" in filePath:
        os.rename(filePath, filePath.replace('&', '_'))
        filePath = filePath.replace('&', '_')
    if "&&" in filePath:
        os.rename(filePath, filePath.replace('&&', '_'))
        filePath = filePath.replace('&&', '_')

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

def installapp(packagePath):
    command='adb install %s'%packagePath
    handle=subprocess.Popen(command,shell=True,stdout=subprocess.PIPE)

    return handle

def starApp(packageName,lanuchableActivity):
    handle = subprocess.Popen(r'adb shell am start %s/%s' % (packageName,lanuchableActivity))

    return handle

def judgeRunning(function):
    while True:
        if function.poll()!=None:
            print('进程已终止')
            break
        else:
            continue

def get_log():
    handle = subprocess.Popen("adb shell  logcat  >log.txt " , shell=True)
    print('\n正在执行log截取，请等待15秒左右')
    time.sleep(15)
    result=subprocess.Popen("taskkill /F /T /PID %s"% str(handle.pid) , stdout=subprocess.PIPE,shell=True)
    # print('日志获取1执行完成')



# #测试代码
# handle=subprocess.Popen("ping www.baidu.com",shell=True,stdout=subprocess.PIPE)
# a=handle.stdout.read()
# a=a.decode()
# print(a)

filePath,packageName,lanuchableActivity=getPackagInfo()
handle=uninstallApp(packageName)
uninstallApp(handle)
judgeRunning(handle)
print('%s 卸载成功'%packageName)
print('%s 开始安装，请稍后'%packageName)
handle_install=installapp(filePath)
judgeRunning(handle_install)
print('%s 安装成功'%packageName)

#配置线程
threads=[]
# t1=threading.Thread(target=get_log1,args=(product,))
t1=threading.Thread(target=get_log)
t2=threading.Thread(target=starApp,args=[packageName,lanuchableActivity])

threads.append(t1)
threads.append(t2)

for t in threads:
    t.start()

for t in threads:
    t.join()

i = 2
for t in threads:
    while 1:
        if t.is_alive():
            continue
        else:
            i-=1
            print('线程运行数为：',i)
            break

print('线程关闭完毕')



# print(a.decode('utf-8'))
# print(str(handle.stdout.encode("utf-8")))
