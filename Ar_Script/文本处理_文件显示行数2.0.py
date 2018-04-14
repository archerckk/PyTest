def file_print2(file,lines):
    (start,end)=lines.split(':')
    if start=='':
        start='1'
    if end=='':
        end='-1'

    #根据不一样的输入内容显示不一样的toast
    if start=='1'and end=='-1':
        prompt='的全文'
    elif start=='1':
        prompt='从开始到%s行'%(end)
    elif end=='-1':
        prompt='从第%s行到末尾'%start
    else:
        prompt = '从第%s行到%s'%(start,end)

    print('\n文件%s%s的内容如下：\n'%(file,prompt))

    f=open(file,encoding='utf-8')

    #计算要打印多少的行数
    start=int(start)-1
    end=int(end)
    lines=end-start

    #先消耗一下开始那些不用打印的行数
    for i in range(start):
        f.readline()

    #小于0的话就
    if lines<0:
        print(f.read(),end='')
    else:
        for i in range(lines):
            print(f.readline(),end='')

    f.close()

file=input('请输入要打开的文件：')
lines=input('请输入需要显示的行数【格式如13:28或：21或21：】：')
file_print2(file,lines)

#
# def showLinesEX(filename,lines):
#     (begin,end)=lines.split(':')
#     if begin=='':
#         begin='1'
#     if end=='':
#         end='-1'
#
#     if begin=='1'and end=='-1':
#         prompt='的全文'
#     elif begin=='1':
#         prompt='从开始到%s行'%end
#     elif end=='-1':
#         prompt='从%s行到结束'%begin
#     else:
#         prompt='从%s行到%s行'%(begin,end)
#     print('\n文件%s%s的内容如下：\n'%(filename,prompt))
#
#     result = int(end) - int(begin)
#     f=open(filename,encoding='utf-8')
#     begin=int(begin)
#     for i in range(begin):
#         f.readline()
#
#     if result<0:
#         print(f.read())
#         f.close()
#     else:
#         for i in range(result):
#             print(f.readline())
#         f.close()
#
# filename=input('请输入你要显示的文件名：')
# lines=input('请输入你要显示的行数（格式如：12:20,12：，：12）：')
#
# showLinesEX(filename,lines)









