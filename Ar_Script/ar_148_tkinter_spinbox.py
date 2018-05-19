from tkinter import *

root = Tk()

w = Spinbox(
    root,
    values= ("Archer", "Saber", "Lancer", "Caster",'Rider','Berserker','Assassin'),
    wrap=True
)
w.pack()

def show_value():
    print(w.get())
Button(root,text='点我',command=show_value).pack()

mainloop()