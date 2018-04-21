import os

def count_file():
    file_list=os.listdir(os.curdir)
    file_dict={}


    for i in file_list:
        if os.path.isdir(i):
            file_dict.setdefault('文件夹',0)
            file_dict['文件夹']+=1
        else:
            extend = os.path.splitext(i)[1]
            file_dict.setdefault(extend,0)
            file_dict[extend]+=1


    for i in file_dict.keys():
        print('该文件夹下共有类型为【%s】的文件%d个' % (i, file_dict[i]))


count_file()