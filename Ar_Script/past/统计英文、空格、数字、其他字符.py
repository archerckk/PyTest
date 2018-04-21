def type_count(str1):
    count_zimu=0
    count_shuzi=0
    count_space=0
    count_fuhao=0
    for i in str1:
        if i.isalpha():
            count_zimu+=1
        elif i.isdigit():
            count_shuzi+=1
        elif i.isspace():
            count_space+=1
        else:
            count_fuhao+=1
    print('字符串中有字母%d个，数字%d个，空格%d个，其他字符%d个'%(count_zimu,count_shuzi,count_space,count_fuhao))

type_count('test test test1.')
