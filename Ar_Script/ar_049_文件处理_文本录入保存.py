#encoding=gbk
print()
'''
编写一个程序，接受用户的输入并保存为新的文件，输入保存指令为【:w】
'''

filename=input('请输入输入文件名：')
f=open('result/%s'%filename,'w')
print('请输入内容【单独输入":w"保存退出】：')
while 1:
    content = input()
    if content!=':w':
        f.write(content+'\n')
        #参考答案做法：f.write('%s\n' % write_some)
        #是有点洋气啊，这个写法
    else:
        break

