import os
import easygui as g


while 1:
    old_version = g.fileopenbox('请选择低版本APK包：')
    if old_version=='.':
        break
    if os.path.splitext(os.path.basename(old_version))[1]!='.apk':
        print('你所选择的不是apk文件！',end='')
    else:
        break

while 1:
    new_version = g.fileopenbox('请选择高版本APK包：')
    if new_version=='.':
        break
    if os.path.splitext(os.path.basename(new_version))[1]!='.apk':
        print('你所选择的不是apk文件！',end='')
    else:
        break


# old_version='CollagePhotoEditor_branches_v1.02_svn28418_202_101_staging_resguard_20170512-1542.apk'
# new_version='CollagePhotoEditor_branches_v1.02_svn28418_202_101_staging_resguard_20170512-1542.apk'

old_list=list(os.popen('aapt dump permissions %s'%old_version))
new_list=list(os.popen('aapt dump permissions %s'%new_version))
differ=[]

for i in new_list:
    if i not in old_list:
        differ.append(i)

if len(differ)==0:
    print('无权限变更！')
    g.msgbox('无权限变更！','提示')
else:
    # print('\n新增权限：\n')
    # for i in differ:
    #     print(i)
    content=''
    for i in differ:
        content+=i
    g.textbox('新增权限：','提示',content)

# input()
