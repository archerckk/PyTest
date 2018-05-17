from tkinter import *

app=Tk()
c=Canvas(app,width=600,height=600,background='white')
c.pack()

c.create_line(0,300,600,300,fill='gray',dash=(4,4))
c.create_line(300,0,300,600,fill='gray',dash=(4,4))


c.create_oval(150,80,450,380,fill='#009fe8',outline='black')
c.create_oval(180,140,420,380,fill='white',outline='black')

c.create_oval(250,120,300,180,fill='white',outline='black')
c.create_oval(300,120,350,180,fill='white',outline='black')

c.create_oval(280,140,295,160,fill='black',outline='black')
c.create_oval(305,140,320,160,fill='black',outline='black')




mainloop()