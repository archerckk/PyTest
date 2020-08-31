import re
from tkinter import *

class TextClear:

    def __init__(self):
        self.app=Tk()
        self.app.title('日志清洗')
        self.app.geometry('400x400')
        self.clear_content=StringVar()

        self.entry=Entry(self.app,textvariable=self.clear_content,validate="focusout",
                         validatecommand=self.clear,width=350)

        b1 = Button(self.app, text="insert point", width=15, height=2, command=self.insert)

        self.text=Text(self.app)


        print(self.clear_content)
        self.entry.pack(padx=20,pady=20)
        b1.pack()
        self.text.pack(padx=20,pady=20)

    def insert(self):
        var = self.entry.get()
        reg_break=re.compile(r'^2020-.+com.social.nene $')
        re.sub(reg_break,'',var)
        print(var)
        self.text.insert('insert', var)

    def reset(self):
        '重置日志清洗内容'
        pass

    def clear(self):
        return self.clear_content.get()


if __name__ == '__main__':
    app=TextClear()
    mainloop()