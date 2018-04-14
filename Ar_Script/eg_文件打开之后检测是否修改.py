import easygui as g
import os

#先打开第一个文件，显示并提取文件内容
file = g.fileopenbox(title='文件选择', msg='请选择你要打开的第一个文件文件', default='./*.txt', filetypes=['.txt', 'txt文档'])
file_name = os.path.basename(file)
with open(file,encoding='utf-8')as f1:
    content = f1.read()
file_content = g.textbox(title='显示文件内容', msg='文件【%s】的内容显示如下' % file_name, text=content)
# print(file_new)

#设置判断两个文件是否一样的初始值
differ = []
count=0

#打开文件1并且将其内容写入文件2并进行修改
file2 = g.fileopenbox(title='文件选择', msg='请选择你要打开的第二个文件', default='./*.txt', filetypes=['.txt', 'txt文档'])
with open(file2, 'w',encoding='utf-8')as f2:
    for i in file_content:
        if i != '\n':
            f2.write(i)
        else:
            f2.write('000\n')
            continue
    # f2.write(file_content.rstrip('\n'))

#判断两个文件是否一样
with open(file2,encoding='utf-8')as f2, open(file,encoding='utf-8')as f1:
    for i in f2:
        j=f1.readline()
        count+=1
        if i != j:
            differ.append(count)
        # print(i,end='')

if len(differ)==0:
    print('两个文件是一样的')
else:
    print('文件不一样')
    for i in differ:
        print(i)


if len(differ) != 0:
    index_no = g.indexbox(title='警告', msg='检测到内容太发生改变，请选择以下操作：', choices=['覆盖保存', '放弃保存', '另存为…'])
    if index_no == 0:
        with open(file,encoding='utf-8')as f1, open(file2, 'w',encoding='utf-8')as f2:
            f2.write(f1.read())
        g.msgbox(title='提示', msg='你已经覆盖保存')
    elif index_no == 1:
        g.msgbox(title='提示', msg='你已经取消保存')
    elif index_no == 2:
        file_new = g.filesavebox(title='保存文件', msg='你要选择另存为的的文件名', default='./*.txt', filetypes='*.txt')
        with open(file_new,'w',encoding='utf-8')as f_new,open(file2,encoding='utf-8')as f2:
            f_new.write(f2.read())
else:
    g.msgbox(title='提示',msg='两个文件是一样的')

###参考###

file_path = g.fileopenbox(default="*.txt")

with open(file_path) as old_file:
    title = os.path.basename(file_path)
    msg = "文件【%s】的内容如下：" % title
    text = old_file.read()
    text_after = g.textbox(msg, title, text)

if text != text_after[:-1]:
    # textbox 的返回值会追加一个换行符
    choice = g.buttonbox("检测到文件内容发生改变，请选择以下操作：", "警告", ("覆盖保存", "放弃保存", "另存为..."))
    if choice == "覆盖保存":
        with open(file_path, "w") as old_file:
            old_file.write(text_after[:-1])
    if choice == "放弃保存":
        pass
    if choice == "另存为...":
        another_path = g.filesavebox(default=".txt")
        if os.path.splitext(another_path)[1] != '.txt':
            another_path += '.txt'
        with open(another_path, "w") as new_file:
            new_file.write(text_after[:-1])
