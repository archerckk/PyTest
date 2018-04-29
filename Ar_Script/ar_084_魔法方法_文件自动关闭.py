'''
写一个FileObject类，给文件对象进行包装，从而确认在删除对象时文件能自动关闭
'''


class FileObj:
    def __init__(self, file='resources/record.txt'):
        self.perfile = open(file)

    def __del__(self):
        print('调用自动关闭方法')
        self.perfile.close()
        '竟然close写错了，调试了半天……看来没什么精神的时候，真的是眼瞎'
        # del self.perfile

f=open('resources/record.txt')
f2 = FileObj(f)
del f2

#参考答案：
# class FileObject:
#     '''给文件对象进行包装从而确认在删除时文件流关闭'''
#
#     def __init__(self, filename='resources/record.txt'):
#         # 读写模式打开一个文件
#         self.new_file = open(filename, 'r+')
#
#     def __del__(self):
#         print("调用自动关闭方法")
#         self.new_file.close()
#         del self.new_file
#
#
# f = FileObject()
# del f
