print()
'''
用户可以随意输入需要现实的行数。如输入：13:21打印13到21行
输入：21打印前21行，输入：21打印从第21行开始到文件结尾所有内容
'''

'''
1.打开文件，拿到里面的内容
2.处理输入需要显示的行数的格式
3.不同的处理要有不同的提示文案
4.打印对应行数的内容
'''
#
#
# def printLines(fileName):
#     f = open('resources/%s' % fileName)
#     fileList = list(f)
#     length = len(fileList)
#     toast = '请输入你要打印的行数【必须包含一个":"号，两边包含或不包含数字】：'
#     while 1:
#         lines = input(toast)
#
#         try:
#             '新增分割错误校验，对格式进行验证'
#             (begin, end) = lines.split(':', 1)
#
#             if end == '' and begin == '':
#                 print('文件【%s】全文的内容如下：\n' % fileName)
#                 for i in range(length):
#                     print(fileList[i])
#                 break
#
#             '新增最大的显示行数内容校验'
#             if (int(begin) > length) or (int(end) > length):
#                 toast='你输入的行数大于文件的最大行数或者！请重新输入：'
#                 continue
#
#             '对第0行识别为开始的处理'
#             if (begin == ''or int(begin)==0) and end != '':
#                 print('文件【%s】从开始到%s行的内容如下：\n' % (fileName, end))
#                 for i in range(int(end)):
#                     print(fileList[i])
#                 break
#
#             if end == '' and begin != '':
#                 print('文件【%s】从%s行到结尾的内容如下：\n' % (fileName, begin))
#                 for i in range(int(begin) - 1, length):
#                     print(fileList[i])
#                 break
#
#
#             if end != '' and begin != '':
#                 print('文件【%s】从%s行到%s行的内容如下：\n' % (fileName, begin, end))
#                 for i in range(int(begin) - 1, int(end)):
#                     print(fileList[i])
#                 break
#
#         except ValueError:
#             toast='【1.必须包含一个":"号，两边包含或不包含数字】\n【2.不能输入非数字字符】\n请重新输入：'
#
# fileName = 'record.txt'
#
#
# printLines(fileName)


'''
参考答案：
将输入的内容通过split分割
设置两个变量，内容都通过固定的变量接收，设计变量的运算规则来显示菜单的打印内容（这样的话可以比较一次，然后就不用重复打印了，减少代码量）
无论怎么输入都由开始参数开始打印的，其他的情况是打印多少行的话将结束减去开始的，然后就可以得出行数了
只需要记录一种全部打印的，其他都可以通过这个规则来实现'''


'阅读答案后优化代码：'

def printLines(fileName):
    f = open('resources/%s' % fileName)
    fileList = list(f)
    length = len(fileList)
    toast_input = '请输入你要打印的行数【必须包含一个":"号，两边包含或不包含数字】：'
    # toast_output=''
    while 1:
        lines = input(toast_input)
        toast_output=''
        try:
            '新增分割错误校验，对格式进行验证'
            (begin, end) = lines.split(':', 1)

            if begin=='':
                begin='1'
            if end=='':
                end='-1'

            if end == '1' and begin == '-1':
                toast_output='全文的内容如下:'

            '新增最大的显示行数内容校验'
            if (int(begin) > length) or (int(end) > length):
                toast_input = '你输入的行数大于文件的最大行数或者！请重新输入：'
                continue

            '对第0行识别为开始的处理'
            if (begin == '-1' or int(begin) == 0) and end != '':
                toast_output = '从开始到%s行的内容如下:'%end

            if end == '-1' and begin != '1':
                toast_output = '从%s行到结尾的内容如下：'%begin

            if end != '-1' and begin != '1':
                toast_output = '从%s行到%s行的内容如下：'% (begin, end)

            '不同toast的显示处理手法'
            print('文件【%s】%s'%(fileName,toast_output))

            '一次计算得出要打印的范围'
            result=int(end)-int(begin)

            if result<0:
                for i in range(length):
                    print(fileList[i])
            else:
                for i in range(result):
                    print(fileList[i])

            f.close()

            break
        except ValueError:
            toast_input='【1.必须包含一个":"号，两边包含或不包含数字】\n【2.不能输入非数字字符】\n请重新输入：'

fileName = 'record.txt'

printLines(fileName)


# def file_view(file_name, line_num):
#     if line_num.strip() == ':':
#         begin = '1'
#         end = '-1'
#
#     (begin, end) = line_num.split(':')
#
#     if begin == '':
#         begin = '1'
#     if end == '':
#         end = '-1'
#
#     if begin == '1' and end == '-1':
#         prompt = '的全文'
#     elif begin == '1':
#         prompt = '从开始到%s' % end
#     elif end == '-1':
#         prompt = '从%s到结束' % begin
#     else:
#         prompt = '从第%s行到第%s行' % (begin, end)
#
#     print('\n文件%s%s的内容如下：\n' % (file_name, prompt))
#
#     # 因为是由0开始遍历的，所以要-1
#     begin = int(begin) - 1
#     end = int(end)
#     lines = end - begin
#
#     f = open(file_name)
#
#     # 用于消耗掉begin之前的内容
#     for i in range(begin):
#         f.readline()
#
#     if lines < 0:
#         print(f.read())
#     else:
#         for j in range(lines):
#             print(f.readline(), end='')
#
#     f.close()
#
#
# # file_name = input(r'请输入要打开的文件（C:\\test.txt）：')
# file_name='record.txt'
# line_num = input('请输入需要显示的行数【格式如 13:21 或 :21 或 21: 或 : 】：')
# file_view(file_name, line_num)
