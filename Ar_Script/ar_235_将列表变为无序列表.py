import pyperclip

'''
list1
list2
list3
list4
'''

text=pyperclip.paste()

list_tmp=text.split('\n')

for i in range(len(list_tmp)):
    list_tmp[i]='*'+list_tmp[i]
text='\n'.join(list_tmp)
pyperclip.copy(text)
print(pyperclip.paste())