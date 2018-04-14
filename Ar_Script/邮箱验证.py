'''
1.前面部分能输入数字、英文、英文下划线、@
2.支持的邮箱有'qq','126','163','sina','gmail'
3.不同的错误会有不同的提示

'''
str_list=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','A','B','C'
      , 'D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5',
         '6','7','8','9','0','_')
num=shuzi='1234567890'
end_list=('qq.com','sina.cn','sina.com','gmail.com','qq.com','163.com','126.com')


while 1 :
    mail=input('请输入你的邮箱：')
    if mail.isspace()or len(mail)==0:
        print('你的邮箱输入为空！')

    elif len(mail)<=12 or len(mail)>=30:
        print('你输入的邮箱地址长度为12-30！')
    elif '@' not in mail:
        print('你的邮箱需要包含"@"符号！')

    elif '@' in mail:
        try:
            (start,end)=mail.split('@',1)
            target=1
            for i in start:
                if i not in str_list:
                    print('你输入的邮箱地址包含非法字符！')
                    target=0
                    break

            if end not in end_list and target==1:
                print('你输入的邮箱后缀有误！')
                continue

            elif target==1 :
                print('邮箱验证通过!你的邮箱名字为：%s'%mail)
                break
        except ValueError:
            pass
