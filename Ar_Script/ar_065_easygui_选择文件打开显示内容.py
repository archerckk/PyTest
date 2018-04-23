import easygui as g
'''
提供一个文件夹浏览框，让用户选择需要打开的文本文件，打开并显示文件内容
'''

filePath=g.fileopenbox('选择你要打开的文件','文件','*')

with open(filePath)as f:
    content=f.read()

g.textbox('文件内容显示如下：','标题',content)


'参考答案的细节做更好一些吧，会拿到文件名显示为标题，然后根据将文件名拿到msg里面显示'
#参考答案
# with open(file_path) as f:
#     title = os.path.basename(file_path)
#     msg = "文件【%s】的内容如下：" % title
#     text = f.read()
#     g.textbox(msg, title, text)