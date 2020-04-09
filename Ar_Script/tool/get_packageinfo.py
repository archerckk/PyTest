import os
import subprocess
import time
import easygui as g
import re
import logging

def getPackagInfo(add_time=False):
    msg = '请选择你要检查的apk安装包'
    title = '文件选择'
    default = "*.apk"
    add_time="_{}".format(time.localtime()[5])

    filePath = g.fileopenbox(msg=msg, title=title, default=default)

    if add_time:
        fileNewName=filePath.split('.apk')[0].strip()+add_time+'.apk'

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