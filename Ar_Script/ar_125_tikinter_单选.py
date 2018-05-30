from tkinter import *

app=Tk()
frame=LabelFrame(app,text='最受欢迎的动漫是：',padx=5,pady=5)
frame.pack(padx=10,pady=10)
# rank=[
#     ('海贼王',1),
#     ('火影',2),
#     ('死神',3),
#     ('猎人',4)
#     ]
rank={1:'海贼王',2:'火影',3:'死神'}


v=IntVar()
v.set(NONE)

def get_value():
    v=int(v.get())
    return v

for num,name in rank.items():
    b=Radiobutton(frame,text=name,value=num,variable=v,indicatoron=False,command=get_value)
    b.pack(fill=X)

print('你选择的是【%s】'%rank[v])


mainloop()