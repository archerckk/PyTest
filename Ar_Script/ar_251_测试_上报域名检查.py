import re
import time
import subprocess


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


def get_stt_link(product):
    #测试连接
    cf_link="http://cf.pikacamera.info/m/config?pubid=10344&moduleid=3000&gaid=79e8de18-52f7-445b-9cdc-82561a913022&guid=c8892207-a92f-4f41-b267-7489a832f0d2&pkg_name=com.pika.camera.android&pkg_ver=1&sdk_vercode=2&sdk_vername=1.0.2.0313&first_time=1555660372&update_time=1555660372&new_user=1&lc=zh_CN_%23Hans&bid=75&file_ver=0"

    # 匹配mo原始链接
    reg_ne = re.compile(r'http://stt.%s.+/ne' % product, re.I)
    reg_nx = re.compile(r'http://stt.%s.+/nx' % product, re.I)
    reg_real=re.compile(r'("g_act":)(.*real_active)(.+)', re.I)
    reg_daily=re.compile(r'("g_act":)(.*daily_active)(.+)', re.I)
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

    # return cf_link_final
product=get_product_name().strip('\n')

print('\n正在执行log截取，请等待15秒左右')
handle = subprocess.Popen("adb shell  logcat |findstr Stat >log2.txt " , shell=True)
time.sleep(15)
subprocess.Popen("taskkill /F /T /PID %s"% str(handle.pid) , shell=True)

get_stt_link(product)
input()