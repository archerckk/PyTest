from tkinter import *

app=Tk()
c=Canvas(app,width=200,height=100,background='white')
c.pack()
'画直线,dash(4,4)'
c.create_line(0,50,200,50,fill='red')
c.create_line(100,0,100,100,fill='grey',dash=(3,3))
c.create_rectangle(50,25,150,75,fill='blue')
mainloop()