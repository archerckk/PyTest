from tkinter import *

app = Tk()

img = PhotoImage(file='resources/icon.png')
Label(app, image=img).place(relx=0.5, rely=0.5,anchor=CENTER)

def callback():
    print('我在正中央')

Button(app, text="点我", command=callback).place(relx=0.5, rely=0.5, anchor=CENTER)


mainloop()
