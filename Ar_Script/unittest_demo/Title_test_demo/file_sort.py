import os
import time

start_dir='Report'

lists=os.listdir(start_dir)
lists.sort(key=lambda fn:os.path.getctime(start_dir),reverse=True)
print(lists[0])
file=os.path.join(start_dir,lists[0])
with open(file,'r',encoding='utf-8')as f:
    print(f.read())