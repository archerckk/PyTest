#输入一个十进制数字，然后打印出来各个进制的结果
'''
1.输入非数字的检测
2.为数字则转换成int类型
3.格式化输出对应的结果
4.输入Q的话退出程序
'''
while 1:
    number=input('请输入十进制数字(输入【q】退出程序)：')
    if number in ['Q','q']:
        print('退出程序')
        break
    if not number.isdigit():
        print('你的输入有误！',end='')
        continue
    number=int(number)
    print('十进制-->2进制：%d -->%s'%(number,bin(number)))
    print('十进制-->8进制：%d -->0o%o'%(number,number))
    print('十进制-->16进制：%d -->0x%x'%(number,number))