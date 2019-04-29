import os,zipfile

def backupToZip(folder):

    folder=os.path.abspath(folder)
    print(folder)
    '检查备份文件是否存在，已存在的话备份文件名加1'
    number=1
    zip_name= os.path.basename(folder) + '_' + str(number) + '.zip'
    while True:
        if not os.path.exists(zip_name):
            break
        else:
            number+=1

    '新建一个压缩文件对象'
    # zip_file=zipfile.ZipFile(zip_name,'w')

    '获取文件列表'
    for file_link,path,file_names in os.walk(folder):
        # print(file_link)
        for filename in file_names:

            file=os.path.join(file_link,filename)
            print(file)

backupToZip(os.getcwd())

