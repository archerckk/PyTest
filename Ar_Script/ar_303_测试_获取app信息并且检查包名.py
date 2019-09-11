


import os
import subprocess
import time
import easygui as g
import re
import requests
from selenium import webdriver

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
    try:
        packageName = reg_packageName.search(log).group(1)
        lanuchableActivity = reg_launchableActivity.search(log).group(1).strip()
        print('选择的apk包名为：', packageName)
        return filePath, packageName, lanuchableActivity
    except Exception as err:
        print(err)
    # print(lanuchableActivity)



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

def judgePackageExist(packageName):
    url = 'http://play.google.com/store/apps/details?id={}'.format(packageName)

    # header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'}
    # proxies = {
    #     'http': '127.0.0.1:8080',
    #     'https': '127.0.0.1:8080'
    # }
    # body = requests.get(url,header).text
    # title=body.title()

    driver=webdriver.Chrome()
    driver.get(url)
    title=driver.title

    if title=='未找到':
        print('包名线上没有重复')
    else:
        print('包名已重复')
    driver.quit()

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
    judgePackageExist(packageName)

    input()