import os
import time
import subprocess
import shutil


def clearFile():
    targetPath=os.curdir
    fileList=os.listdir(os.curdir)
    for i in fileList:
        if ' 'in i:
            name=i.replace(' ','')
            shutil.move(targetPath+os.sep+i,name)


def popen(cmd):
    try:
        popen = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        popen.wait()
        lines = popen.stdout.readlines()
        return [line.decode('gbk') for line in lines]
    except BaseException as e:
        print("格式转换失败")
        return -1


def miniVersionCode():
    address = os.curdir
    apk = ".apk"
    install_result = "sdkVersion:'29'"
    # address=input('请输入APK存放路径')
    package_list = os.listdir(address)
    print("apk列表：")
    print(package_list)
    for package in package_list:
        if apk not in package:
            print("%s不是.apk文件" % package)
            continue
        p = os.popen('aapt dump badging %s |findstr "sdkVersion' % (address + '/' + package))
        result = p.read()
        p.close()
        if install_result not in result:
            print('%s miniVersionCode不是29，结果：%s ' % (package, result))
            continue
        else:
            print('Pass，miniVersionCode是29：' + package)
            print(result)  # cmd输出结果
            time.sleep(30)


if __name__ == "__main__":
    clearFile()
    miniVersionCode()
    input()