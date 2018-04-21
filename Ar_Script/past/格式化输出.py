'这是一个将10进制的数转换为8进制、16进制、2进制的脚本'

while 1:
    tmp = input('请输入你要转换的数字：')
    if tmp=='q' or tmp=='Q':
        print('退出程序')
        break
    elif not tmp.isdigit():
        print('你的输入有误！',end='')
        continue
    else:
        num = int(tmp)
        print('十进制->十六进制：%d->0o%o'%(num,num))
        print('十进制->十六进制：%d->0x%X' % (num, num))
        print('十进制->十六进制：%d->' % num+str(bin(num)))
        break