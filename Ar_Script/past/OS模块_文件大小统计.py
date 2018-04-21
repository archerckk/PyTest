import os

# def count_size():
#     file_list=os.listdir(os.curdir)
#
#
#     for i in file_list:
#         if os.path.isdir(i):
#             continue
#         else:
#             print('%s【%dBytes】'%(i,os.path.getsize(i)))


def count_size2():
    file_list=os.listdir(os.curdir)
    file_dict={}

    for i in file_list:
        if os.path.isfile(i):
            file_size=os.path.getsize(i)
            file_dict[i]=file_size

    for i in file_dict.items():
        print('%s【%dBytes】'%(i[0],i[1]))


count_size2()