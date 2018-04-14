import os

def read_type_size(file,target):
    os.chdir(file)
    all_file=os.listdir(os.getcwd())


    for each_file in all_file:
        if os.path.splitext(each_file)[1] in target:
            file_dict[os.getcwd()+os.sep+each_file]='【%sBytes】'%os.path.getsize(each_file)
            # file_list.append(os.getcwd() + os.sep + each_file+os.linesep)
        if os.path.isdir(each_file):
            read_type_size(each_file,target)
            os.chdir(os.pardir)


target=['.py','.txt','.avi','.mp4']
file_dict={}
file_list=[]
program_path=os.getcwd()

file=input('请输入你要查找的目录：')
read_type_size(file,target)


f=open(program_path+os.sep+'文件保存列表2.txt','w')

for i in file_dict.keys():
    print(i)
    f.writelines(i+file_dict[i]+os.linesep)
f.close()
