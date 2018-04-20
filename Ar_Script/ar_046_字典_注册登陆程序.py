print()
"""
1.写一个整体登陆的函数，里面要用包含各种操作码的操作内容
2.写一个新建用户函数，在登陆函数里面被调用
    新建用户不存在
        提示输入密码（密码不能为空）
        完成注册打印提示信息
    新建用户存在
        提示用户名已存在，重新输入
3.写一个登陆账号函数，在登陆函数里面调用
    用户不存在，提示重新输入
    输入密码
        密码不正确，要重新输入
        密码只有三次机会，三次之后锁定该账号，退出到主菜单
            锁定的账号无法再次登陆
        输入正确，提示登陆系统成功
4.选择Q退出程序
"""

account = {}
lockedAccount=[]
chose=False

def newAccount():
    toast = '请输入用户名：'
    while 1:
        name = input(toast)
        if name.isspace() or len(name) == 0:
            toast = '用户名输入为空！请重新输入：'
        elif name in account.keys():
            toast = '此用户名已经存在，请重新输入：'
        else:
            break
    while 1:
        account[name] = input('请输入你的密码：')
        if account[name].isspace() or len(account[name]) == 0:
            print('密码不能为空！', end='')
            continue
        else:
            break
    print('恭喜你的账号【%s】注册成功!' % name)


def login():
    global chose
    toast = '请输入用户名：'
    while 1:
        name = input(toast)
        if name not in account.keys():
            toast = '你的用户名不存在，请重新输入：'
        elif name in lockedAccount:
            print('你的的账号已经被锁定，无法正常登陆')
            break
        else:
            count=3
            psw_toast='请输入你的密码：'
            while 1:
                password=input(psw_toast)
                if password==account[name]:
                    print('恭喜【%s】你已成功登陆00XX系统！！'%name)
                    chose=False
                    break
                if password!=account[name]:
                    count -= 1
                    if count!=0:
                        psw_toast='密码错误！你还有%d次机会:'%count
                    else:
                        print('你的账号已被锁定!!!')
                        lockedAccount.append(name)
                        chose = True
                        break
            break


def index():
    toast='''\n|---新建用户：N/n---|
|---登陆账号：E/e---|
|---退出程序：Q/q---|
|---请输入指令代码:'''
    while 1:
        code = input(toast)
        if code not in 'NnEeQq':
            print('代码有误！')
        else:
            chosen=True

        #
        if code in 'Nn':
            newAccount()

        #条件符合调用登陆函数
        if code in 'Ee':
            login()
            # 假如chose为真，则账号继续锁定，退出到主菜单，可以继续操作
            if chose:
                continue
            #假如chose为假，则系统登陆成功，停止主菜单，退出程序
            else:
                break

        if code in ['Q','q']:
            print('退出OOXX系统')
            break

index()
