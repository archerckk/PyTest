#encording=gbk
import easygui as g
import os


'''
统计你当前代码量的总和，并显示离是万行代码量还有多远？
1.递归搜索各个文件夹
2.显示各个类型的源文件和源代码数量
3.显示总行数与百分比
'''

def showresult():
    lines=0
    result=''
    total=0
    for i in fileNums:
        lines=codeLines[i]
        total+=lines
        result+='【%s】原文件%d个，源代码%d行\n'%(i,fileNums[i],lines)
    msg='你目前共积累编写了%d行代码，完成进度：%.2f%%\n离10万行代码还差%d行，请继续努力'%(total,total/1000,100000-total)
    title='统计结果'

    g.textbox(msg,title,result)



def calLines(file):
    lines=0
    '一直以为计算逻辑有问题，其实是编码有问题，真的是debug的时候看清楚一点定位好问题才好解决啊'
    with open(file,encoding='utf-8') as f:
        try:
            print('正在分析文件%s'%file)
            for j in f:
                lines += 1
        except UnicodeDecodeError:
            pass
    return lines



def search_file(filePath,targetExt):

    #递归实现bug代码
    # allFile=os.listdir(filePath)
    #
    #
    # for i in allFile:
    #     ext=os.path.splitext(i)
    #     if ext[1] in targetExt:
    #         targetFile.append(os.getcwd()+os.sep+i+os.linesep)
    #     if os.path.isdir(i):
    #         search_file(i,targetExt)
    #         os.chdir(os.path.pardir)
    allFile = os.walk(filePath)

    for i in allFile:
        for each_file in i[2]:
            ext=os.path.splitext(each_file)[1]
            if ext in targetExt:
                fileName = os.path.join(i[0], each_file)
                lines=calLines(fileName)

                '计算文件个数'
                try:
                    fileNums[ext]+=1
                except KeyError:
                    fileNums[ext]=1

                '计算行数'
                try:
                    codeLines[ext]+=lines
                except KeyError:
                    codeLines[ext]=lines

fileNums={}
codeLines={}
targetFile=[]
targetExt=['.py']
outPutPath=os.curdir+'result/'

filePath=g.diropenbox('请选择你要查找的目录：','提示')
search_file(filePath,targetExt)


showresult()

'参考答案：'
# def show_result(start_dir):
#     lines = 0
#     total = 0
#     text = ""
#
#     for i in source_list:
#         lines = source_list[i]
#         total += lines
#         text += "【%s】源文件 %d 个，源代码 %d 行\n" % (i, file_list[i], lines)
#     title = '统计结果'
#     msg = '您目前共累积编写了 %d 行代码，完成进度：%.2f %%\n离 10 万行代码还差 %d 行，请继续努力！' % (total, total / 1000, 100000 - total)
#     g.textbox(msg, title, text)
#
#
# def calc_code(file_name):
#     lines = 0
#     with open(file_name,encoding='utf-8') as f:
#         print('正在分析文件：%s ...' % file_name)
#         try:
#             for each_line in f:
#                 lines += 1
#         except UnicodeDecodeError:
#             pass  # 不可避免会遇到格式不兼容的文件，这里忽略掉......
#     return lines
#
#
# def search_file(start_dir):
#     os.chdir(start_dir)
#
#     for each_file in os.listdir(os.curdir):
#         ext = os.path.splitext(each_file)[1]
#         if ext in target:
#             lines = calc_code(each_file)  # 统计行数
#             # 还记得异常的用法吗？如果字典中不存，抛出 KeyError，则添加字典键
#
#             # 统计文件数
#             try:
#                 file_list[ext] += 1
#             except KeyError:
#                 file_list[ext] = 1
#
#                 # 统计源代码行数，假如能读取就加上行数，否则就赋值保存行数
#             try:
#                 source_list[ext] += lines
#             except KeyError:
#                 source_list[ext] = lines
#
#         if os.path.isdir(each_file):
#             search_file(each_file)  # 递归调用
#             os.chdir(os.pardir)  # 递归调用后切记返回上一层目录
#
#
# target = ['.c', '.cpp', '.py', '.cc', '.java', '.pas', '.asm']
# file_list = {}
# source_list = {}
#
# g.msgbox("请打开您存放所有代码的文件夹......", "统计代码量")
# path = g.diropenbox("请选择您的代码库：")
#
# search_file(path)
# show_result(path)