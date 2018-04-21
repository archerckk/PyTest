account = {}

def new_user():
    prompt='请输入用户名：'
    while 1:
        name=input(prompt)
        if name in account.keys():
            prompt='此用户名已经被使用，请重新输入：'
            continue
        else:
            account[name] = input('请输入密码：')
        print('注册成功，赶紧登陆吧^_^')
        break

def login():
    prompt='请输入用户名：'
    while 1:
        name = input(prompt)
        if name not in account.keys():
            prompt='你输入的用户名不存在，请重新输入：'
            continue
        else:
            break
    psw = input('请输入密码：')
    while psw!=account[name]:
            psw=input('你输入的密码有误，请重新输入：')
    else:
        print('欢迎进入OOXX系统，请点击右上角的x结束程序！')


def index():
    code_list = ['N', 'n', 'E', 'e', 'Q', 'q']
    while 1:
        print()
        print('''
|---新建用户：N/n---|
|---登陆账号：E/e---|
|---退出程序：Q/q---|''')
        daima=input('|---请输入指令代码：')
        if daima not in code_list:
            print('你输入的代码有误！')
            continue
        elif daima=='N'or daima=='n':
            new_user()
        elif daima=='E'or daima=='e':
            login()
            break
        else:
            print('退出程序！')
            break

index()