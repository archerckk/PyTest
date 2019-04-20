import re
import requests
import os
import time
import threading
import signal
import  subprocess
import sys


#获取手机日志
# handle = subprocess.Popen("adb shell  logcat |findstr nad >log.txt " , shell=True)
# time.sleep(60)
# subprocess.Popen("taskkill /F /T /PID %s"% str(handle.pid) , shell=True)



#匹配配置地址

def get_mo_conf():

    mo_link="url:http://mo.pikacamera.info/cr/config?pubid=10344&pkg_ver=1&gaid=79e8de18-52f7-445b-9cdc-82561a913022&guid=d81cb6c5-de99-455b-83cd-4a918d48f784&pkg_name=com.pika.camera.android&osv=25&new_user=1&ad_sdk_version=2&first_time=1555660372&bid=75&has_sim=false&sdk_vercode=2&sdk_vername=1.0.2.0118&channel=101&file_ver=0"

    #匹配mo原始链接
    reg_mo=re.compile(r'Url:(http://mo.pikacamera.+)(file_ver=\d+)',re.I|re.DOTALL)
    #匹配mo链接的cr参数
    reg_mo_new=re.compile(r'/(cr)/')

    with open('log.txt', 'r', encoding='utf-8')as f:
        log=f.readlines()


    result=reg_mo.search(mo_link)
    result2=reg_mo_new.search(mo_link)

    mo_link_str=mo_link.replace(result2.group(1),'v3')
    new_link_result=reg_mo.search(mo_link_str)
    mo_link_final=new_link_result.group(1)+new_link_result.group(2)
    return mo_link_final

print(get_mo_conf())

def get_cf_conf():
    mo_link="url:http://mo.pikacamera.info/cr/config?pubid=10344&pkg_ver=1&gaid=79e8de18-52f7-445b-9cdc-82561a913022&guid=d81cb6c5-de99-455b-83cd-4a918d48f784&pkg_name=com.pika.camera.android&osv=25&new_user=1&ad_sdk_version=2&first_time=1555660372&bid=75&has_sim=false&sdk_vercode=2&sdk_vername=1.0.2.0118&channel=101&file_ver=0"

    #匹配mo原始链接
    reg_mo=re.compile(r'Url:(.+)(file_ver=\d+)',re.I|re.DOTALL)
    #匹配mo链接的cr参数
    reg_mo_new=re.compile(r'/(cr)/')

    result=reg_mo.search(mo_link)
    result2=reg_mo_new.search(mo_link)

    mo_link_str=mo_link.replace(result2.group(1),'v3')
    new_link_result=reg_mo.search(mo_link_str)
    mo_link_final=new_link_result.group(1)+new_link_result.group(2)
    return mo_link_final



# reg_test=re.compile(r'.+')
# result_test=reg_test.search(str2)

# print(result)
# handle = subprocess.Popen("adb shell  logcat |findstr StatTag >log2.txt " , shell=True)
# time.sleep(30)
# subprocess.Popen("taskkill /F /T /PID %s"% str(handle.pid) , shell=True)


# print('测试成功')



