from tkinter import *

app=Tk()
text=Text(app)
text.pack()

text.insert(1.0,'I trust fishr.com')
def getIndex(text,index):
    return tuple(map(int,str.split(text.index(index),'.')))

start='1.0'
while True:
    pos=text.search('r',start,END)
    if not pos:
        break
    print('所在的位置为：',(getIndex(text,pos)))
    start=pos+'+1c'





mainloop()