#encoding=UTF-8

import openpyxl
import os
import shutil

"""
1、先拿到桌面里面所有包含.xlsx的文件列表
2、假如有index包含在xlse里面
3、打开excel文件读取第一个工作表的第一行，将文件名获取到
4、将excel文件的index前面的内容跟产品名用空格隔开拼接一个目录名
5、将文件剪切到新建的目录里面
"""

desktop=r'C:\Users\Administrator\Desktop'
os.chdir(desktop)
fileList=os.listdir(desktop)
targetFileList=[]
productList=[]
radicalPath=r'D:\项目记录\激进包'
productNameList=[]

for i in fileList:
    if 'index' in i:
        targetFileList.append(i)

for i in targetFileList:
    print(i)
    wb=openpyxl.load_workbook(desktop+os.sep+i)
    worksheet=wb.active
    productList.append(worksheet['A1'].value)

try:
    productNameList=[ i.split("：")[1] for i in productList if "："in i]
except Exception as e:
    print('错误信息为；{}'.format(e))


for i in range(len(productNameList)):
    targetFile=radicalPath + os.sep + productNameList[i]
    if not os.path.exists(targetFile):
        os.mkdir(targetFile)
    try:
        shutil.move(desktop+os.sep+targetFileList[i],targetFile+os.sep+targetFileList[i])
    except Exception as e:
        print('文件处理异常：{}'.format(e))