import os
from ar_278_测试_apk安装 import getPackagInfo

"""
1、获取所有的连接在电脑上面的手机列表
2、卸载手机列表上面的指定包名的程序
3、遍历手机列表安
"""
''
filePath, packageName, lanuchableActivity = getPackagInfo()

cmd='adb devices'
device_output=os.popen(cmd).readlines()
phone_list=[]

for line in device_output:
    if "devices"not in line:
        device='#'.join(line.split())
        phone_name=device.split('#')[0]
        phone_list.append(phone_name)

for phone in phone_list:
    uninstall_cmd='adb -s {} uninstall {}'.format(phone,packageName)
    log=os.popen(uninstall_cmd)
    print(phone,"卸载日志：",log.read())

for phone in phone_list:
    install_cmd = 'adb -s {} install {}'.format(phone, filePath)
    log = os.popen(install_cmd)
    print(phone,"安装日志:",log.read())

input('输入回车结束程序！！！')