
psw=input('请输入需要检查的密码组合：')
zimu=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','A','B','C'
      , 'D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
shuzi='1234567890'
fuhao='~!@#$%^&*()_+[]{}:;"|\<,>.?//*-+.'
length=len(psw)
while psw.isspace()or length==0:
    print('你输入的密码为空（只包含空格），请重新输入：',end='')
    psw=input()
    length=len(psw)

if length<=8:
    num_level=1

elif 8<length<16:
    num_level=2
else:
    num_level=3

str_level=0
for i in psw:
    if i in zimu:
        str_level+=1
        break

for i in psw:
    if i in fuhao:
        str_level += 1
        break

for i in psw:
    if i in shuzi:
        str_level += 1
        break

while 1:
    if num_level==1 and str_level==1:
        print('安全等级为：低')
    elif num_level==2 or str_level==2 :
        print('安全等级为：中')
    elif (num_level==3 or str_level==3)and not psw.startswith(zimu):
        print('安全等级为：较高')
    else:
        print('安全等级为：高\n请继续保持')
        break
    print('1.密码必须由数字、字母、特殊字符三种组合\n2.密码长度不能低与16位\n3.请以字母开头')
    break
