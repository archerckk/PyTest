import os
import subprocess
import time
import easygui as g
import re
import logging


def getPackagInfo():
    msg = '请选择你要检查的apk安装包'
    title = '文件选择'
    default = "*.apk"
    add_time="_{}".format(time.localtime()[5])

    filePath = g.fileopenbox(msg=msg, title=title, default=default)

    fileNewName=filePath.split('.apk')[0].strip()+add_time+'.apk'
    os.rename(filePath,fileNewName)

    logging.debug('选择的apk路径为：{}'.format(fileNewName))

    command = 'aapt dumpsys badging "%s" ' % fileNewName

    handle = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    time.sleep(2)

    reg_packageName = re.compile(r"package: name='(.+?)'")
    reg_launchableActivity = re.compile(r"launchable-activity: name='(.+?)'")

    log=str(handle.stdout.read())
    position=log.index('targetSdkVersion:')


    logging.debug('\n{}\n'.format(log[0:position+21]))#截取到targetSDK Version部分包信息

    try:
        packageName = reg_packageName.search(log).group(1)
        lanuchableActivity = reg_launchableActivity.search(log).group(1).strip()
        logging.debug('选择的apk包名为：{}'.format(packageName))
        logging.debug(packageName+'\n'+lanuchableActivity)
        return fileNewName, packageName, lanuchableActivity
    except Exception as err:
        logging.debug(err)



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
            logging.debug('进程已终止')
            break
        else:
            continue


if __name__ == '__main__':
    filePath, packageName, lanuchableActivity = getPackagInfo()
    # print(filePath)
    handle = uninstallApp(packageName)
    uninstallApp(handle)
    judgeRunning(handle)
    logging.debug('%s 卸载成功' % packageName)

    logging.debug('%s 开始安装，请稍后' % packageName)
    handle_install = installapp(filePath)

    logging.debug('安装日志为：', handle_install.stdout.read().decode().strip('\r\n'))

    input('安装完成,按回车关闭窗口')