import os
import easygui as g

'文件选择'
while 1:
    old_version = g.fileopenbox('请选择低版本APK包：')
    if old_version == '.':
        break
    if os.path.splitext(os.path.basename(old_version))[1] != '.apk':
        print('你所选择的不是apk文件！', end='')
    else:
        break

while 1:
    new_version = g.fileopenbox('请选择高版本APK包：')
    if new_version == '.':
        break
    if os.path.splitext(os.path.basename(new_version))[1] != '.apk':
        print('你所选择的不是apk文件！', end='')
    else:
        break

'测试代码'
# old_version=r'C:\Users\chenzhibin\Downloads\BeautyCamera_trunk_v1.24_svn12108_233_101_staging_defaultConfig_resguard_20180531-1731.apk'
# new_version=r'C:\Users\chenzhibin\Downloads\BeautyCamera_trunk_v1.23_svn11912_232_101_staging_defaultConfig_resguard_20180524-1526.apk'

'调用appt指令获取两个包的uses-permission列表'
old_list = list(os.popen('aapt dump permissions %s |findstr uses-permission' % old_version))
new_list = list(os.popen('aapt dump permissions %s |findstr uses-permission' % new_version))

'判断两个包的权限的权限更多'
length1 = len(old_list)
length2 = len(new_list)
judge = False

if length1 > length2:
    old_list, new_list = new_list, old_list
    judge = True

differ = []
repeat = []
dict_old = dict()
dict_new = dict()

for i in old_list:
    if i not in dict_old.keys():
        dict_old[i] = 0
    else:
        dict_old[i] += 1

for i in new_list:
    if i not in dict_new.keys():
        dict_new[i] = 0
    else:
        dict_new[i] += 1

for i in dict_new.keys():
    if i not in dict_old.keys():
        differ.append(i)
    else:
        if dict_new[i] != dict_old[i]:
            repeat.append(i)

            # print(i)
            # if i not in old_list:
            #     differ.append(i)

if len(differ) == 0 and len(repeat) == 0:
    print('无权限变更！')
    g.msgbox('无权限变更！', '提示')
else:
    # print('\n新增权限：\n')
    # for i in differ:
    #     print(i)
    content = ''
    if len(repeat) != 0:
        for i in repeat:
            content += i
        g.textbox('重复权限：', '提示', content)
    elif len(differ) != 0 and judge == True:
        for i in differ:
            content += i
        g.textbox('减少权限：', '提示', content)
    elif len(differ) != 0:
        for i in differ:
            content += i
        g.textbox('新增权限：', '提示', content)

input()
