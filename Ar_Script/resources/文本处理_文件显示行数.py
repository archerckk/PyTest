# def print_file(file,line):
#     f=open(file,encoding='utf-8')
#     line=int(line)
#     for i in range(line):
#         print(f.readline(),end='')
#
#
# file=input('请输入要打开的文件：')
# line=input('请输入需要显示该文件前几行：')
# print_file(file,line)

def show_lines(filename,lines):
    f=open(filename,encoding='utf-8')
    lines=int(lines)
    for lines in range(lines):
        print(f.readline(),end='')

filename=input('请输入你要显示内容的文件名；')
lines=input('请输入你要显示的行数:')
show_lines(filename,lines)

























