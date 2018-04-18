print()
'尝试利用字典的特性编写一个通讯录程序'
'''
1.查询联系人资料
    存在打印，不存在提示
2.插入新的联系人
    不存在直接新增
    已存在提示是否修改
        是，覆盖原来的电话，提示修改成功
        否，跳出当前新增
3.删除联系人
    联系人不存在
        提示删除的联系人不存在
    联系人存在
        提示是否删除
            是，删除,打印删除id
            否，跳出当前选项
4.退出通讯录程序
    打印提示语，终止循环
'''
print(
'''
|---欢迎进入通讯录程序---|
|---1.查询联系人资料 ---|
|---2.插入新的联系人 ---|
|---3.删除已有联系人 ---|
|---4.退出通讯录程序 ---|'''
)

def contacts():
    codeList=['1','2','3','4']
    contact={}

    while 1:
        code=input('\n请输入相关的指令代码：')
        if code not in codeList:
            print('非法指令代码！',end='')

        if code=='1':
            name=input('请输入联系人姓名：')
            if name not in contact:
                print('你所查找的联系人不存在！！')
            else:
                print(name+':',contact[name])

        if code=='2':
            name = input('请输入联系人姓名：')
            if name not in contact:
                contact[name]=input('请输入联系方式：')
            else:
                print('你输入的姓名在通讯录中已存在-->>%s:%s'%(name,contact[name]))
                '两个以上的格式化参数一定要记得加（）不然会说格式化参数的数量不对'
                while 1:
                    decide = input('是否修改用户资料（YES/NO:）')
                    if decide in ['YES','yes','Yes']:
                        contact[name] = input('请输入联系方式：')
                        print('修改资料成功')
                        break
                    if decide in ['NO','No''no']:
                        break
                    else:
                        print('你的输入有误！',end='')

        if code=='3':
            name = input('请输入联系人姓名：')
            if name in contact:
                while 1:
                    decide = input('是否删除用户资料（YES/NO:）')
                    if decide in ['YES','yes','Yes']:
                        del contact[name]
                        print('删除用户%s：'%name)
                        break
                    if decide in ['NO','No','no']:
                        break
                    else:
                        print('你的输入有误！',end='')
            else:
                print('你要删除的用户不存在！')

        if code=='4':
            print('|---感谢使用通讯录程序---|')
            break

contacts()