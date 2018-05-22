from tkinter import colorchooser
from tkinter import *

def callback():
    color=colorchooser.askcolor()
    print(color[1])

Button(text='颜色选择',command=callback).pack()

mainloop()