from tkinter import filedialog
from  tkinter import *

print(filedialog.askopenfilename(title='文件选择',defaultextension='.py',
                           filetypes=[('PNG','.png'),('JPG','.jpg'),('PY','.py')]))


print(filedialog.asksaveasfilename(title='文件保存',defaultextension='.py',
                                   filetypes=[('PNG', '.png'), ('JPG', '.jpg'), ('PY', '.py')]
                                   ))
mainloop()
