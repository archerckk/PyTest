import os
import subprocess
import time
import easygui as g
import re
import threading
import sys
import requests
import pprint

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
        "adb shell touch sdcard/xxtestmodexx",
        'adb shell touch sdcard/appflashtm'
    ]
    for i in add_debug_list:
        os.popen(i)
    print("测试日志文件创建成功")

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

    print('选择的apk路径为：',filePath)
    command='aapt dumpsys badging %s > packageInfo.txt'%filePath
    packInfoFile='./packageInfo.txt'

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
    print('选择的apk包名为：',packageName)
    # print(lanuchableActivity)

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
    print('\n正在执行log截取，请等待20秒左右')
    time.sleep(20)
    result=subprocess.Popen("taskkill /F /T /PID %s"% str(handle.pid) , stdout=subprocess.PIPE,shell=True)
    # print('日志获取1执行完成')

def get_cf_conf(packageName):

    # 各个配置连接的正则表达式
    reg_cashSDK_cf = re.compile(r'(http://cf.(.+?)\..+moduleid=(3000)&.+%s.+)' % packageName, re.I)
    reg_radicalSDK_cf=re.compile(r'(http://cf.(.+?)\..+moduleid=(3300)&.+%s.+)' % packageName, re.I)
    reg_guidSDK_cf = re.compile(r'(http://cf.(.+?)\..+moduleid=(3100)&.+%s.+)' % packageName, re.I)
    reg_adSDK_cf=re.compile(r'(http://mo.(.+)\..+/(cr)/.+pkg_name=%s&.+has_sim=false.+)'%packageName,re.I)

    # 匹配cf链接的m参数
    reg_cf_new = re.compile(r'/(m)/')
    reg_mo_new = re.compile(r'/(cr)/')

    mainIndex=''
    result_cash_mainIndex=''
    result_guidSDK_mainIndex=''
    result_adSDK_mainIndex=''
    result_radicalSDK_mainIndex=''

    with open('log.txt', 'r', encoding='utf-8')as f:
        try:
            log = f.read()
        except Exception as e:
            print(e)

        '变现sdk的功能配置请求信息打印'
        try:
            result_cash = reg_cashSDK_cf.search(log)
            result_cash_link_str = result_cash.group(1)  # 原始链接
            result_cash_mainIndex = result_cash.group(2)  # 主域名
            result3000_key = reg_cf_new.search(result_cash_link_str)
            result3000_key_str = result3000_key.group()
            cf_link_final = result_cash_link_str.replace(result3000_key_str, '/p/')
        except:
            print('\n获取变现sdk的功能配置请求失败')
        else:
            print('\n变现sdk的功能配置请求连接为：\n%s\n配置内容：' % result_cash_link_str)
            try:
                cf_json = requests.get(cf_link_final).json()
                pprint.pprint(cf_json)
                print()
            except Exception as e:
                print('\n解析变现sdk的功能配置请求失败，错误信息为：%s' % e)

        #激进sdk的功能配置请求信息打印
        try:
            result_radicalSDK = reg_radicalSDK_cf.search(log)
            result_radicalSDK_link_str = result_radicalSDK.group(1)  # 原始链接
            result_radicalSDK_mainIndex = result_radicalSDK.group(2)  # 主域名
            result3300_key = reg_cf_new.search(result_radicalSDK_link_str)
            result_key3300_str = result3300_key.group()
            cf_link_final = result_radicalSDK_link_str.replace(result_key3300_str, '/p/')
        except:
            print('\n获取激进sdk的功能配置请求失败')
        else:
            print('\n激进sdk的功能配置请求连接为：\n%s\n配置内容：' % result_radicalSDK_link_str)
            try:
                cf_json = requests.get(cf_link_final).json()
                pprint.pprint(cf_json)
                print()
            except Exception as e:
                print('解析激进sdk的功能配置请求失败，错误信息为：%s' % e)
        print()

        #guidsdk功能配置请求信息打印
        try:
            result_guidSDK = reg_guidSDK_cf.search(log)
            result_guidSDK_link_str = result_guidSDK.group(1)  # 原始链接
            result_guidSDK_mainIndex = result_guidSDK.group(2)  # 主域名
            result3100_key = reg_cf_new.search(result_guidSDK_link_str)
            result_key3100_str = result3100_key.group()
            cf_link_final = result_cash_link_str.replace(result_key3100_str, '/p/')
        except:
            print('\n获取guidsdk功能配置请求失败')
        else:
            print('\nguidsdk功能配置请求连接为：\n%s\n配置内容：' % result_guidSDK_link_str)
            try:
                cf_json = requests.get(cf_link_final).json()
                pprint.pprint(cf_json)
                print()
            except Exception as e:
                print('\n解析guidsdk功能配置请求失败，错误信息为：%s' % e)
        print()

        # adsdk功能配置请求信息打印
        try:
            result_adSDK = reg_adSDK_cf.search(log)
            result_adSDK_link_str = result_adSDK.group(1)  # 原始链接
            result_adSDK_mainIndex = result_adSDK.group(2)  # 主域名
            resultAD_key = reg_mo_new.search(result_adSDK_link_str)
            resultAD_key_str = resultAD_key.group()
            cf_link_final = result_adSDK_link_str.replace(resultAD_key_str, '/v3/')
        except:
            print('\n获取adsdk功能配置请求失败')
        else:
            print('\nadsdk功能配置请求连接为：\n%s\n配置内容：' % result_adSDK_link_str)
            try:
                cf_json = requests.get(cf_link_final).json()
                pprint.pprint(cf_json)
                print()
            except Exception as e:
                print('\n解析adsdk功能配置请求失败，错误信息为：%s' % e)
        print()

        for i in result_cash_mainIndex,result_radicalSDK_mainIndex,result_guidSDK_mainIndex,result_adSDK_mainIndex:
            if i != None:
                mainIndex = i
                break
            else:
                print('\n没有匹配到请求配置的相关连接')

    return mainIndex

def get_stt_link(product):

    # 匹配stt原始链接
    reg_ne = re.compile(r'http://stt.%s.+/ne' % product, re.I)
    reg_nx = re.compile(r'http://stt.%s.+/nx' % product, re.I)
    reg_real=re.compile(r'({("g_act":"real_active").+?"g_cnt":1})', re.I)
    reg_daily = re.compile(r'({("g_act":"daily_active").+?"g_cnt":1})', re.I)
    reg_code = re.compile(r' {"code":.+{}}')

    with open('log.txt', 'r', encoding='utf-8')as f:
        try:
            log = f.read()
        except Exception as e:
            print(e)
        try:
            reg_real_str=reg_real.search(log).group(2)
            print('真实日活验证成功：',reg_real_str)
        except:
            print('\n真实日活验证失败')
        try:
            reg_daily_str = reg_daily.search(log).group(2)
            print('\n进程日活验证成功：', reg_daily_str)
        except:
            print('\n进程日活验证失败')
        try:
            reg_ne_str = reg_ne.search(log).group()
            print('\n事件打点上报域名验证成功：',reg_ne_str)
        except:
            print('\n事件打点上报域名验证失败')
        try:
            reg_nx_str=reg_nx.search(log).group()
            print('\n日活打点上报验证成功：',reg_nx_str)
        except:
            print('\n日活打点上报验失败')
        try:
            reg_code_str = reg_code.search(log).group()
            print('\n成功上传打点日志：：', reg_code_str)
        except:
            print('\n没有找到上传成功的日志')
        print()

def get_longLive_versionName(packageName):
    with open('log.txt', 'r', encoding='utf-8')as f:
        try:
            log = f.read()
        except Exception as e:
            print(e)
    try:
        reg_longLive = re.compile(r'{.+g_pkgname":"(%s)".+"libVerName":"(.+?)",' % packageName)
    except:
        print('由于配置连接获取失败，无法正常匹配')
    else:
        try:
            reg_longLive_str = reg_longLive.search(log).group(2)
            print('保活SDK匹配日志为：', reg_longLive.search(log).group())
            print('匹配的包名为：',reg_longLive.search(log).group(1))
            print('保活SDK版本为：：', reg_longLive_str)
        except:
            print('\n没有找到上传成功的日志')


# #测试代码
# handle=subprocess.Popen("ping www.baidu.com",shell=True,stdout=subprocess.PIPE)
# a=handle.stdout.read()
# a=a.decode()
# print(a)
#
if __name__ == '__main__':
    openLog()

    filePath,packageName,lanuchableActivity=getPackagInfo()
    handle=uninstallApp(packageName)
    uninstallApp(handle)
    judgeRunning(handle)
    print('%s 卸载成功'%packageName)

    print('%s 开始安装，请稍后'%packageName)
    handle_install=installapp(filePath)

    print('安装日志为：',handle_install.stdout.read().decode().strip('\r\n'))

    while True:
        handle=os.popen('adb shell pm list package')
        if packageName in handle.read():
            print('%s 安装成功' % packageName)
            break
        else:
            continue

    # if str(handle_install.stdout.read()).find('Success')!=-1:
    #     print('%s 安装成功' % packageName)
    # else:
    #     input('程序安装失败！请检查是否没有授权安装程序，按回车退出脚本')
    #     sys.exit()
    judgeRunning(handle_install)



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

    while 1:
        # if os.path.exists('.%slog.txt'%os.sep)and  os.path.exists('.%slog2.txt'%os.sep):
        if os.path.exists('.%slog.txt' % os.sep):
            print('\n日志文件生成完毕')
            print('\n开始检查日志文件')
            break
        else:
            print('\n日志生成中，继续检查')
            continue

    time.sleep(2)
    product=get_cf_conf(packageName)
    get_stt_link(product)
    get_longLive_versionName(packageName)

    toast = '\n是否删除tmp文件（log.txt文件）y/n：'
    while True:
        choice=input(toast)
        if choice =='y':
            print('执行删除缓存的log')
            os.remove('./log.txt')
            os.remove('./packageInfo.txt')
            break
        elif choice =='n':
            print('不执行删除')
            break
        else:
            toast='你输入的选项有误！请重新输入：'
            continue

    input('输入回车关闭窗口')