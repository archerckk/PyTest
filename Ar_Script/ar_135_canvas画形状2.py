from tkinter import *

app=Tk()
c=Canvas(app,width=200,height=100,background='white')
c.pack()
'画直线,dash(4,4)'
c.create_line(0,0,200,100,fill='green',width=3)
c.create_line(0,100,200,0,fill='green',width=3)
c.create_rectangle(50,25,150,75,fill='green')
c.create_rectangle(60,30,140,70,fill='yellow')
c.create_text(100,50,text='万象更新',fill='red')

mainloop()