import re
import threading
import requests
import pprint
import time
import  subprocess



#获取产品连接名字
def get_product_name():
    product=input('请输入你要选择的产品缩写：')
    product_list=[]
    with open('product_name_list.txt','r')as f:
        for i in f:
            product_list.append(i)
    for i in product_list:
        if product==i.split(':')[0]:
            product=i.split(':')[1]
        else:
            pass
    return product


def get_log1():
    handle = subprocess.Popen("adb shell  logcat |findstr nad >log.txt " , shell=True)
    print('\n正在执行log截取，请等待15秒左右')
    time.sleep(15)
    subprocess.Popen("taskkill /F /T /PID %s"% str(handle.pid) , shell=True)
    print('日志获取1执行完成')


def get_log2():
    handle = subprocess.Popen("adb shell  logcat |findstr Stat >log2.txt " , shell=True)
    time.sleep(15)
    subprocess.Popen("taskkill /F /T /PID %s"% str(handle.pid) , shell=True)
    print('日志获取2执行完成')


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

    return result_link_str,mo_link_final


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

    return  result_link_str,cf_link_final

def get_stt_link(product):
    #测试连接
    cf_link="http://cf.pikacamera.info/m/config?pubid=10344&moduleid=3000&gaid=79e8de18-52f7-445b-9cdc-82561a913022&guid=c8892207-a92f-4f41-b267-7489a832f0d2&pkg_name=com.pika.camera.android&pkg_ver=1&sdk_vercode=2&sdk_vername=1.0.2.0313&first_time=1555660372&update_time=1555660372&new_user=1&lc=zh_CN_%23Hans&bid=75&file_ver=0"

    # 匹配mo原始链接
    reg_ne = re.compile(r'http://stt.%s.+/ne' % product, re.I)
    reg_nx = re.compile(r'http://stt.%s.+/nx' % product, re.I)
    reg_real=re.compile(r'("g_act":)(.*real_active)(.+}?)', re.I)
    reg_daily=re.compile(r'("g_act":)(.*daily_active)(.+}?)', re.I)
    # 匹配mo链接的cr参数
    reg_code = re.compile(r' {"code":.+{}}')

    with open('log2.txt', 'r', encoding='utf-8')as f:
        log = f.read()
        reg_real_str=reg_real.search(log).group()
        print('\n真实日活验证成功：',reg_real_str)
        reg_daily_str = reg_daily.search(log).group()
        print('\n进程日活验证成功：',reg_daily_str)
        reg_ne_str = reg_ne.search(log).group()
        print('\n事件打点上报域名验证成功：',reg_ne_str)
        reg_nx_str=reg_nx.search(log).group()
        print('\n日活打点上报验证成功：',reg_nx_str)
        reg_code_str=reg_code.search(log).group()
        print('\n上传成功日志：',reg_code_str)



#获取产品信息
product=get_product_name().strip('\n')
print(product)

#配置线程
threads=[]
t1=threading.Thread(target=get_log1)
t2=threading.Thread(target=get_log2)

threads.append(t1)
threads.append(t2)

for t in threads:
    t.start()

for t in threads:
    t.join()

mo_link=get_mo_conf(product)
cf_link=get_cf_conf(product)

#打印stt上报域名信息
get_stt_link(product)


mo_json=requests.get(mo_link[1]).json()
print('\n广告配置的连接为：\n%s\n配置内容：'%mo_link[0])
pprint.pprint(mo_json)
print()
cf_json=requests.get(cf_link[1]).json()
print('功能和外部广告配置的连接为：\n%s\n配置内容：'%cf_link[0])
pprint.pprint(cf_json)


#

#测试代码
# handle = subprocess.Popen("adb shell  logcat |findstr nad >log.txt " , shell=True)
# time.sleep(30)
# subprocess.Popen("taskkill /F /T /PID %s"% str(handle.pid) , shell=True)

# reg_test=re.compile(r'.+')
# result_test=reg_test.search(str2)

# print(result)
# handle = subprocess.Popen("adb shell  logcat |findstr StatTag >log2.txt " , shell=True)
# time.sleep(30)
# subprocess.Popen("taskkill /F /T /PID %s"% str(handle.pid) , shell=True)


# print('测试成功')



