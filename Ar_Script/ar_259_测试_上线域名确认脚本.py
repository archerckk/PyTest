import os
import subprocess
import time
import easygui as g
import re

"""
1.获取文件的路径
2.用路径获取到包名
3.卸载包名
4.安装app
5.先开启日志抓取
5.打开app
6.分析日志文件抓取各个域名
    通过包名抓取cf配置，再得到主域名
    通过包名抓取mo配置
    通过包名
"""
packInfoFileOj = './packageInfo.txt'

def getPackagInfo():
    msg='请选择你要检查的apk安装包'
    title='文件选择'
    filePath=g.fileopenbox(msg=msg,title=title,default="*.apk")
    print(filePath)
    command='aapt dumpsys badging %s '%filePath
    packInfoFileOj='./packageInfo.txt'
    list1=[]

    with open(packInfoFileOj,'w',encoding='utf-8')as f:
        handle=subprocess.Popen(command,stdout=f,shell=True)


packageinfo=[]
def getKeyInfo():
    with open(packInfoFileOj, 'r',encoding='utf-8')as f :
        for i in f:
           print(i)


# for i in packageinfo:
#     print(i)

getPackagInfo()