print(
'''
|---欢迎进入通讯录程序---|
|---1.查询联系人资料 ---|
|---2.插入新的联系人 ---|
|---3.删除已有联系人 ---|
|---4.退出通讯录程序 ---|''')


contact={}
code=['1','2','3','4']
judge=['YES','NO']

while 1:
    print()
    daima=input('请输入相关的指令代码：')
    if daima not in code:
        print('你输入的代码有误!')
        continue

    if daima=='1':
        name = input('请输入联系人姓名：')
        if name in contact.keys():
            print(name,':',contact[name])

        else:
            print('你查找的用户不存在!')

    if daima=='2':
        name = input('请输入联系人姓名：')
        if name not in contact.keys():
            contact[name] = input('请输入联系人电话：')
        else:
            print('你输入的姓名在通讯录中已存在-->%s：%s'%(name,contact[name]))
            flag=input('是否修改用户资料（YES/NO）：')
            if flag ==judge[0]:
                contact[name] = input('请输入联系人电话：')
            elif flag==judge[1]:
                continue
            else:
                print('你的确认有误！')
                continue

    if daima=='3':
        name = input('请输入你要删除的联系人姓名：')
        if name in contact.keys():
            flag = input('是否删除用户资料（YES/NO：）')
        else:
            print('你要删除的用户不存在！')
            continue
        if flag ==judge[0]:
            contact.pop(name)
        elif flag==judge[1]:
            continue
        else:
            print('你的确认有误！')
            continue

    if daima=='4':
        print('|---感谢使用通讯录程序---|')
        break
