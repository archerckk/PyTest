import os
import subprocess
import time
import easygui as g
import re


def getPackagInfo():
    msg = '请选择你要检查的apk安装包'
    title = '文件选择'
    default = "*.apk"

    filePath = g.fileopenbox(msg=msg, title=title, default=default)
    if ' ' in filePath:
        os.rename(filePath, filePath.replace(' ', '_'))
        filePath = filePath.replace(' ', '_')
    if "&" in filePath:
        os.rename(filePath, filePath.replace('&', '_'))
        filePath = filePath.replace('&', '_')
    if "&&" in filePath:
        os.rename(filePath, filePath.replace('&&', '_'))
        filePath = filePath.replace('&&', '_')

    print('选择的apk路径为：', filePath)
    command = 'aapt dumpsys badging %s > packageInfo.txt' % filePath
    packInfoFile = './packageInfo.txt'

    handle = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    time.sleep(2)
    reg_packageName = re.compile(r"package: name='(.+?)'")
    reg_launchableActivity = re.compile(r"launchable-activity: name='(.+?)'")
    log = ''
    with open(packInfoFile, encoding='utf-8',errors='ignore')as f:
        for i in f:
            log += i

    packageName = reg_packageName.search(log).group(1)
    lanuchableActivity = reg_launchableActivity.search(log).group(1).strip()
    print('选择的apk包名为：', packageName)
    # print(lanuchableActivity)

    return filePath, packageName, lanuchableActivity

def uninstallApp(packageName):
    command = 'adb uninstall %s' % packageName
    handle = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)

    return handle


def installapp(packagePath):
    command = 'adb install %s' % packagePath
    handle = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)

    return handle

def judgeRunning(function):
    while True:
        if function.poll() != None:
            print('进程已终止')
            break
        else:
            continue


if __name__ == '__main__':
    filePath, packageName, lanuchableActivity = getPackagInfo()
    handle = uninstallApp(packageName)
    uninstallApp(handle)
    judgeRunning(handle)
    print('%s 卸载成功' % packageName)

    print('%s 开始安装，请稍后' % packageName)
    handle_install = installapp(filePath)

    print('安装日志为：', handle_install.stdout.read().decode().strip('\r\n'))
    os.remove('./packageInfo.txt')
