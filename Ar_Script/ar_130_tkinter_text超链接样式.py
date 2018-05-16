from tkinter import *
import webbrowser
app=Tk()

text=Text()
text.pack()
text.insert(1.0,'I trust fish.com!')
'tag属性设置'
text.tag_add('link',1.8,1.16)
text.tag_config('link',foreground='blue',underline=True)

'tag事件绑定'
def show_arrow(event):
    text.config(cursor="arrow")

def show_Xterm(event):
    text.config(cursor='Xterm')

def url_open(event):
    webbrowser.open('http://www.fishc.com')

text.tag_bind('link','<Enter>',show_arrow)
text.tag_bind('link','<Leave>',show_Xterm)
text.tag_bind('link','<Button-1>',url_open)


mainloop()