from tool.logger import Loger
import logging
import os
import subprocess
import time
import easygui as g
import re


"""
1、获取所有的连接在电脑上面的手机列表
2、卸载手机列表上面的指定包名的程序
3、遍历手机列表安
"""
''

def getPackagInfo():
    msg = '请选择你要检查的apk安装包'
    title = '文件选择'
    default = "*.apk"
    add_time="_{}".format(time.localtime()[5])

    filePath = g.fileopenbox(msg=msg, title=title, default=default)

    # fileNewName=filePath.split('.apk')[0].strip()+add_time+'.apk'
    fileNewName=filePath.split('.apk')[0].strip()+'.apk'
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


loger=Loger('install',mode='w')
filePath, packageName, lanuchableActivity = getPackagInfo()

cmd='adb devices'
device_output=os.popen(cmd).readlines()
phone_list=[]

for line in device_output:
    if "devices"not in line:
        device='#'.join(line.split())
        phone_name=device.split('#')[0]
        phone_list.append(phone_name)

'多手机卸载app'
for phone in phone_list:
    uninstall_cmd='adb -s {} uninstall {}'.format(phone,packageName)
    log=os.popen(uninstall_cmd)
    logging.debug("{}卸载日志：{}".format(phone,log.read()))

'多手机安装app'
for phone in phone_list:
    install_cmd = 'adb -s {} install {}'.format(phone, filePath)
    log = os.popen(install_cmd)
    logging.debug("{}安装日志：{}".format(phone,log.read()))



input('输入回车结束程序！！！')