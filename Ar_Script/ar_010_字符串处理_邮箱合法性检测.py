'''
1.前面部分能输入数字、英文、英文下划线、@
2.支持的邮箱有'qq','126','163','sina','gmail'
3.不同的错误会有不同的提示
4.符合条件的邮箱会提示完成注册
5.长度为12到30个字符
'''
str_list=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','A','B','C'
      , 'D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5',
         '6','7','8','9','0','_')
num=shuzi='1234567890'
end_list=('qq.com','sina.cn','sina.com','gmail.com','qq.com','163.com','126.com')

while 1:
    email=input('请输入你的邮箱：')
    if email.isspace()or len(email)==0:
        print('你输入的邮箱为空!',end='')
    elif not 12<=len(email)<=30:
        print('你输入的邮箱长度不符合规则!',end='')
    elif '@'not in email:
        print('你输入的邮箱地址没有包含【@】！',end='')
    elif '@'in email:
        try:
            (start, end) = email.split('@')
            for i in start:
                if i not in str_list:
                    print('你输入的@前面的部分有误！',end='')
                    break
            if not email.endswith(end_list):
                print('你输入的email的后缀有误！',end='')
            else:
                print('你注册的邮箱合法！你的邮箱为：',email)
                break
        except ValueError:
            print('你输入的邮箱格式有误！',end='')


