import re
import threading
import requests
import pprint
import time
import  subprocess
import os


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
    handle = subprocess.Popen("adb shell  logcat  >log.txt " , shell=True)
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
        try :
            log=f.read()
            result=reg_mo.search(log)
            result_link_str=result.group(1)
            result_key = reg_mo_new.search(result_link_str)
            result_key_str=result_key.group()
            mo_link_final = result_link_str.replace(result_key_str, '/v3/')
        except AttributeError as e:
            print(e)

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
        try:
            result = reg_mo.search(log)
            result_link_str = result.group(1)
            result_key = reg_mo_new.search(result_link_str)
            result_key_str = result_key.group()
            cf_link_final = result_link_str.replace(result_key_str, '/p/')
        except AttributeError as e:
            print(e)

    return  result_link_str,cf_link_final

def get_stt_link(product):
    #测试连接
    cf_link="http://cf.pikacamera.info/m/config?pubid=10344&moduleid=3000&gaid=79e8de18-52f7-445b-9cdc-82561a913022&guid=c8892207-a92f-4f41-b267-7489a832f0d2&pkg_name=com.pika.camera.android&pkg_ver=1&sdk_vercode=2&sdk_vername=1.0.2.0313&first_time=1555660372&update_time=1555660372&new_user=1&lc=zh_CN_%23Hans&bid=75&file_ver=0"

    # 匹配mo原始链接
    reg_ne = re.compile(r'http://stt.%s.+/ne' % product, re.I)
    reg_nx = re.compile(r'http://stt.%s.+/nx' % product, re.I)
    reg_real=re.compile(r'({"g_act":)(.*real_active)(.+?,"g_ver")', re.I)
    reg_daily=re.compile(r'("g_act":)(.*daily_active)(.+?,"g_ver")', re.I)
    # 匹配mo链接的cr参数
    reg_code = re.compile(r' {"code":.+{}}')

    with open('log2.txt', 'r', encoding='utf-8')as f:
        log = f.read()
        try:
            reg_real_str=reg_real.search(log).group()
            print('\n真实日活验证成功：',reg_real_str)
        except:
            print('\n真实日活验证失败')
        try:
            reg_daily_str = reg_daily.search(log).group()
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
            reg_code_str=reg_code.search(log).group()
            print('\n成功上传打点日志：',reg_code_str)
        except:
            print('\n没有找到上传成功的日志')
        print()

#获取产品信息
product=get_product_name().strip('\n')
print(product)

#配置线程
threads=[]
# t1=threading.Thread(target=get_log1,args=(product,))
t1=threading.Thread(target=get_log1)
t2=threading.Thread(target=get_log2)

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
    if os.path.exists('.%slog.txt'%os.sep)and  os.path.exists('.%slog2.txt'%os.sep):
        print('\n日志文件生成完毕')
        print('\n开始检查日志文件')
        break
    else:
        print('\n日志生成中，继续检查')
        continue

# 打印stt上报域名信息
get_stt_link(product)

#尝试打印广告配置
try:
    mo_link = get_mo_conf(product)
except:
    print('广告配置获取失败')
else:
    print('\n广告配置的连接为：\n%s\n配置内容：' % mo_link[0])
    try:
        mo_json = requests.get(mo_link[1]).json()
        pprint.pprint(mo_json)
        print()
    except Exception as e:
        print('解析服务器地址失败，错误信息为：%s'%e)

#尝试打印功能和外部广告配置
try:
    cf_link = get_cf_conf(product)
except:
    print('功能和外部广告配置获取失败')
else:
    print('功能和外部广告配置的连接为：\n%s\n配置内容：' % cf_link[0])
    try:
        cf_json = requests.get(cf_link[1]).json()
        pprint.pprint(cf_json)
    except Exception as e:
        print('解析服务器地址失败，错误信息为：%s' % e)

# print('在日志中查找不到要匹配的地址，请不要删除log文件，检查输出的内容！！！')

toast = '\n是否删除tmp文件（log.txt文件）y/n：'
while True:
    choice=input(toast)
    if choice =='y':
        print('执行删除缓存的log')
        os.remove('./log.txt')
        os.remove('./log2.txt')
        break
    elif choice =='n':
        print('不执行删除')
        break
    else:
        toast='你输入的选项有误！请重新输入：'
        continue


input('输入回车关闭窗口')