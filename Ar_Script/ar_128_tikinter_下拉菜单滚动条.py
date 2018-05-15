from tkinter import *

app=Tk()

scy=Scrollbar(app)
scy.pack(fill=Y,side=RIGHT)
lb=Listbox(app,yscrollcommand=scy.set)
for i in range(1000):
    lb.insert(END,i)

lb.pack()

scy.config(command=lb.yview)

mainloop()
