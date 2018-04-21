import os

def print_dict(key_dict):
    keys=key_dict.keys()
    keys=sorted(keys)

    for each_key in keys:
        print('关键字出现第%s行第%s个位置。'%(each_key,str(key_dict[each_key])))


def pos_list(lines,keys):
    pos=[]
    begin=lines.find(keys)

    while begin!=-1:
        pos.append(begin+1)
        begin=lines.find(keys,begin+1)

    return pos


def search_in_file(file,keys):
    keys_dict={}
    f=open(file)
    count=0

    for each_line in f:
        count+=1
        if keys in each_line:
            pos=pos_list(each_line,keys)
            keys_dict[count]=pos

    f.close()
    return keys_dict

def search_files(keys,judge):
    all_file=os.walk(os.getcwd())
    txt_files=[]

    for i in all_file:
        for each_file in i[2]:
            if os.path.splitext(each_file)[1]=='.txt':
                each_file=os.path.join(i[0],each_file)
                txt_files.append(each_file)

    for each_txt_file in txt_files:#遍历文件列表
        key_dict = search_in_file(each_txt_file, keys)
        if key_dict:
            print('================================================================')
            print('在文件【%s】中找到关键字【%s】' % (each_txt_file, keys))
            if judge in ['YES', 'Yes', 'yes']:
                print_dict(key_dict)

keys=input('请将该脚本放于带查找的文件夹内，请输入关键字：')
judge=input('请问是否需要打印关键字【%s】在文件中的具体位置（YES/NO）：'%keys)
search_files(keys,judge)