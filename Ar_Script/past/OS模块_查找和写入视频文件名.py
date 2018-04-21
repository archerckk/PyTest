import os

def search_file(start_dir,target):
    os.chdir(start_dir)

    for i in os.listdir(os.curdir):
        ext=os.path.splitext(i)[1]
        if ext in target:
            file_list.append(os.getcwd()+os.path.sep+i+os.linesep)
        if os.path.isdir(i):
            search_file(i,target)
            os.chdir(os.pardir)

start_dir=input('请输入你要查找的目录：')
program_dir=os.getcwd()
target=['.txt','.py']
file_list=[]

search_file(start_dir,target)

f=open(program_dir+os.sep+'file_list.txt','w')
f.writelines(file_list)
f.close()
