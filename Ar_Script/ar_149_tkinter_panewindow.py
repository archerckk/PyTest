from tkinter import  *

# app=Tk()
w1=PanedWindow(showhandle=True,sashrelief=SUNKEN)
w1.pack(fill='both',expand=1)
l1=Label(w1,text='left')
l1.pack()
w1.add(l1)

w2=PanedWindow(orient=VERTICAL,showhandle=True,sashrelief=SUNKEN)
w1.add(w2)

l2=Label(w2,text='top')
l2.pack()

l3=Label(w2,text='bottom')
l3.pack()
w2.add(l2)
w2.add(l3)






mainloop()