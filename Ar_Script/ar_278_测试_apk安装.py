import os
import subprocess
import time
import easygui as g
import re


def getPackagInfo():
    msg = '请选择你要检查的apk安装包'
    title = '文件选择'
    default = "*.apk"
    add_time="_{}".format(time.localtime()[5])

    filePath = g.fileopenbox(msg=msg, title=title, default=default)
    file_dir = os.path.dirname(filePath)
    # print(file_dir)

    if ' ' in filePath:
        fileNewName = filePath.replace(' ', '_')
    if "&" in filePath:
        fileNewName = filePath.replace('&', '_')
    if "&&" in filePath:
        fileNewName = filePath.replace('&&', '_')

    fileNewName=filePath.split('.apk')[0].strip()+add_time+'.apk'
    os.rename(filePath,fileNewName)

    print('选择的apk路径为：', fileNewName)
    # command = 'aapt dumpsys badging %s > packageInfo.txt' % fileNewName
    command = 'aapt dumpsys badging "%s" ' % fileNewName
    # packInfoFile = './packageInfo.txt'

    handle = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    time.sleep(2)

    reg_packageName = re.compile(r"package: name='(.+?)'")
    reg_launchableActivity = re.compile(r"launchable-activity: name='(.+?)'")
    # log = ''
    log=str(handle.stdout.read())
    print('\n',log[0:176],'\n')#截取到targetSDK Version部分包信息
    # with open(packInfoFile, encoding='utf-8',errors='ignore')as f:
    #     for i in f:
    #         log += i
    try:
        packageName = reg_packageName.search(log).group(1)
        lanuchableActivity = reg_launchableActivity.search(log).group(1).strip()
        print('选择的apk包名为：', packageName)
        return fileNewName, packageName, lanuchableActivity
    except Exception as err:
        print(err)
    # print(lanuchableActivity)



def uninstallApp(packageName):
    command = 'adb uninstall %s' % packageName
    handle = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)

    return handle


def installapp(packagePath):
    command = 'adb install "%s"' % packagePath
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
    # print(filePath)
    handle = uninstallApp(packageName)
    uninstallApp(handle)
    judgeRunning(handle)
    print('%s 卸载成功' % packageName)

    print('%s 开始安装，请稍后' % packageName)
    handle_install = installapp(filePath)

    print('安装日志为：', handle_install.stdout.read().decode().strip('\r\n'))
    # os.remove('./packageInfo.txt')
    input('安装完成,按回车关闭窗口')