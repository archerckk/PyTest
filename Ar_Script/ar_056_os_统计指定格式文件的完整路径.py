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
                target_list.append(target_file)

    outPutDir=''
    for i in target_list:
        print(i)


filePath=r'G:\Pycharm_Project\PyTest'
get_file_list(filePath)