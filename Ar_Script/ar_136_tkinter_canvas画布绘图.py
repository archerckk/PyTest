from tkinter import *

app=Tk()
c=Canvas(app,width=400,height=200,background='white')
c.pack()

def paint(event):
    x1,y1=(event.x-1),(event.y-1)
    x2,y2=(event.x+1),(event.y+1)
    c.create_oval(x1,y1,x2,y2,fill='black')

c.bind('<B1-Motion>',paint)


def clear():
    c.delete(ALL)
Button(app,text='清除',command=clear).pack()



mainloop()