import os
'''
编写一个程序，用户输入开始搜索的路径，查找该路径下（包括子文件夹内）所有制定格式的文件
并创建一个TXT文档存放所有找的文件的路径（包含文件名）
'''

'''
1.一个参数接收输入的路径
2.拿到该路径下的所有指定格式（统计[.py]文件）的文件（用列表接收？）
    
3.固定一个输出文档的目录，将列表的内容写进去
'''

def get_file_list(filePath):
    os.chdir(filePath)
    allFile=os.walk(filePath)
    target=['.py']
    target_list=[]

    for i in allFile:
        for j in i[2]:
            ext=os.path.splitext(j)
            if ext[1] in target:
                target_file=os.path.join(i[0],j)
                target_list.append(target_file+os.linesep)

    '''
    每个列表元素的末尾记得添加换行符，不然显示结果就是一条超级长的字符串了
    递归实现遍历所有文件夹，记得返回到上一层目录
    '''
    # for each_file in os.listdir(os.curdir):
    #     ext = os.path.splitext(each_file)[1]
    #     if ext in target:
    #         vedio_list.append(os.getcwd() + os.sep + each_file + os.linesep)  # 使用os.sep使程序更标准
    #     if os.path.isdir(each_file):
    #         search_file(each_file, target)  # 递归调用
    #         os.chdir(os.pardir)  # 递归调用后切记返回上一层目录


    outPutDir=filePath+os.sep+'Ar_Script'+os.sep+'result'

    f=open(outPutDir+os.sep+'result.txt','w')
    for i in target_list:
        f.write(i)

    # f.writelines('%s%s'%(target_list+os.linesep)
    f.close()


    # for i in target_list:
    #     print(i)

filePath=input(r'请输入你要查找的目录：')
# filePath=r'c:\Pycharm_Project\PyTest'
get_file_list(filePath)

#参考答案
'''
除了函数，然后执行出结果的顺序，还是可以先定义一个输出目录的变量接收了路径
然后再全局变量列表接收函数的结果，最后再写入文件，这样就可以比较稳定固定输出目录了
一个简单的执行顺序，就可以减少很多复杂的计算
'''
# def search_file(start_dir, target):
#     os.chdir(start_dir)
#
# start_dir = input('请输入待查找的初始目录：')
# program_dir = os.getcwd()
#
# target = ['.mp4', '.avi', '.rmvb']
# vedio_list = []
#
# search_file(start_dir, target)
#
# f = open(program_dir + os.sep + 'vedioList.txt', 'w')
# f.writelines(vedio_list)
# f.close()