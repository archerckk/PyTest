from tkinter import *

app=Tk()
def print_pos(event):
    print(event.x_root,event.y_root)

c=Canvas(app,width=600,height=600,background='white')
c.bind('<Button-1>',print_pos)
c.pack()

c.create_line(0,300,600,300,fill='gray',dash=(4,4))
c.create_line(300,0,300,600,fill='gray',dash=(4,4))

'头和脸'
c.create_oval(150,80,450,380,fill='#009fe8',outline='black')
c.create_oval(180,140,420,380,fill='white',outline='black')

'眼眶'
c.create_oval(250,120,300,180,fill='white',outline='black')
c.create_oval(300,120,350,180,fill='white',outline='black')

'眼球'
c.create_oval(280,140,295,160,fill='black',outline='black')
c.create_oval(305,140,320,160,fill='black',outline='black')

'眼珠'
c.create_oval(285,145,292,155,fill='white',outline='black')
c.create_oval(307,145,314,155,fill='white',outline='black')

'鼻子'
c.create_oval(290,165,310,185,fill='red',outline='black')

'竖线'
c.create_line(300,185,300,295,fill='black')

'嘴巴'
c.create_arc(330,323,397,353,fill='black',style='arc')


mainloop()