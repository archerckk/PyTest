from tkinter import *

app=Tk()
frame=LabelFrame(app,text='最受欢迎的动漫是：',padx=5,pady=5)
frame.pack(padx=10,pady=10)
rank=[
    ('海贼王',1),
    ('火影',2),
    ('死神',3),
    ('猎人',4)
    ]
v=IntVar()
v.set(1)
for name,num in rank:
    b=Radiobutton(frame,text=name,value=num,variable=v,indicatoron=False).pack(fill=X)
    print(v.get())



mainloop()