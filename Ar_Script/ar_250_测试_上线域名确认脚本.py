import re
import requests
import pprint
import os
import time
import  subprocess
import sys



#获取产品连接名字
def get_product_name():
    product=input('请输入你要选择的产品缩写：')
    with open('product_name_list.txt','r')as f:
        tmp_str=f.readline()
        if product==tmp_str.split(':')[0]:
            product=tmp_str.split(':')[1]
    return product

def get_mo_conf(product):

    #测试连接
    mo_link="url:http://mo.%s.info/cr/config?pubid=10344&pkg_ver=1&gaid=79e8de18-52f7-445b-9cdc-82561a913022&guid=d81cb6c5-de99-455b-83cd-4a918d48f784&pkg_name=com.pika.camera.android&osv=25&new_user=1&ad_sdk_version=2&first_time=1555660372&bid=75&has_sim=false&sdk_vercode=2&sdk_vername=1.0.2.0118&channel=101&file_ver=0"%product

    #匹配mo原始链接
    reg_mo=re.compile(r'Url:(http://mo.%s.+)'%product,re.I)
    #匹配mo链接的cr参数
    reg_mo_new=re.compile(r'/(cr)/')

    with open('log.txt', 'r', encoding='utf-8')as f:
        log=f.read()
        result=reg_mo.search(log)
        result_link_str=result.group(1)
        result_key = reg_mo_new.search(result_link_str)
        result_key_str=result_key.group()
        mo_link_final = result_link_str.replace(result_key_str, '/v3/')

    return mo_link_final


def get_cf_conf(product):
    #测试连接
    cf_link="http://cf.pikacamera.info/m/config?pubid=10344&moduleid=3000&gaid=79e8de18-52f7-445b-9cdc-82561a913022&guid=c8892207-a92f-4f41-b267-7489a832f0d2&pkg_name=com.pika.camera.android&pkg_ver=1&sdk_vercode=2&sdk_vername=1.0.2.0313&first_time=1555660372&update_time=1555660372&new_user=1&lc=zh_CN_%23Hans&bid=75&file_ver=0"

    # 匹配mo原始链接
    reg_mo = re.compile(r'Url:(http://cf.%s.+)' % product, re.I)
    # 匹配mo链接的cr参数
    reg_mo_new = re.compile(r'/(m)/')

    with open('log.txt', 'r', encoding='utf-8')as f:
        log = f.read()
        result = reg_mo.search(log)
        result_link_str = result.group(1)
        result_key = reg_mo_new.search(result_link_str)
        result_key_str = result_key.group()
        cf_link_final = result_link_str.replace(result_key_str, '/p/')

    return cf_link_final

product=get_product_name()
# print(product)

#获取手机日志
handle = subprocess.Popen("adb shell  logcat |findstr nad >log.txt " , shell=True)
time.sleep(30)
subprocess.Popen("taskkill /F /T /PID %s"% str(handle.pid) , shell=True)

handle2 = subprocess.Popen("adb shell  logcat |findstr Stat >log.txt " , shell=True)
subprocess.Popen("taskkill /F /T /PID %s"% str(handle2.pid) , shell=True)

mo_link=get_mo_conf(product)
cf_link=get_cf_conf(product)

mo_json=requests.get(mo_link).json()
print('广告配置的连接为：\n%s\n配置内容：'%mo_link)
pprint.pprint(mo_json)
print()
cf_json=requests.get(cf_link).json()
print('功能和外部广告配置的连接为：\n%s\n配置内容：'%cf_link)
pprint.pprint(cf_json)


# reg_test=re.compile(r'.+')
# result_test=reg_test.search(str2)

# print(result)
# handle = subprocess.Popen("adb shell  logcat |findstr StatTag >log2.txt " , shell=True)
# time.sleep(30)
# subprocess.Popen("taskkill /F /T /PID %s"% str(handle.pid) , shell=True)


# print('测试成功')



