import os
'统计当前文件夹所有文件的大小'

def countSizes():
    fileList=os.listdir(os.curdir)
    sizesDict={}

    for i in  fileList:
        if os.path.isdir(i):
            continue
        else:
            sizesDict[i]=os.path.getsize(i)

    '其实只处理是文件的情况就好了，为何要多写一步处理文件夹呢？'
    '还是避免重复代码的思维吧，虽然这里只调用一次'
    # if os.path.isfile(each_file):
    #     file_size = os.path.getsize(each_file)
    #     file_dict[each_file] = file_size


    '另外一种遍历字典的方式'
    # for each in file_dict.items():
    #     print('%s【%dBytes】' % (each[0], each[1]))

    for i in sizesDict.keys():
        print(i,'【%sBytes】'%sizesDict[i])

countSizes()
