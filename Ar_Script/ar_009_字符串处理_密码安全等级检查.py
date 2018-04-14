# 低级密码要求：
#   1. 密码由单纯的数字或字母组成
#   2. 密码长度小于等于8位
#
# 中级密码要求：
#   1. 密码必须由数字、字母或特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）任意两种组合
#   2. 密码长度不能低于8位
#
# 高级密码要求：
#   1. 密码必须由数字、字母及特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）三种组合
#   2. 密码只能由字母开头
#   3. 密码长度不能低于16位

zimu=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','A','B','C'
      , 'D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
shuzi='1234567890'
fuhao='`~!@#$%^&*()-_+={}[]|\'\;:<>,./?"'
length_level=0
str_level=0

psw=input('请输入你要检查的密码：')
length=len(psw)

if length<8:
    length_level=1
elif 8<=length<16:
    length_level=2
else:
    length_level=3

for i in psw:
    if i in zimu:
        str_level+=1
        break
for i in psw:
    if i in shuzi:
        str_level+=1
        break
for i in psw:
    if i in fuhao:
        str_level+=1
        break
while 1:
    if str_level==1 or length_level==1:
        print('你的密码安全等级评为：低')
    elif length_level==2 and str_level==2:
        print('你的密码安全等级评为：中')
    elif not psw.startswith((zimu)) and (length_level==3 or str_level==3):
        print('你的密码安全等级评为：较高')
    else:
        print('你的密码安全等级评为：高\n请继续保持!!!')
        break
    print('1.密码必须由数字、字母、特殊字符三种组合\n2.密码长度不能低与16位\n3.请以字母开头')
    break