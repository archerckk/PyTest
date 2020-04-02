import tkinter as tk
import os
from tool.get_packageinfo import getPackagInfo


def get_phone_list():
    cmd = 'adb devices'
    device_output = os.popen(cmd).readlines()
    phone_list = []

    for line in device_output:
        if "devices" not in line:
            device = '#'.join(line.split())
            phone_name = device.split('#')[0]
            phone_list.append(phone_name)
    if ''in phone_list:
        phone_list.remove('')
    return phone_list

def get_phone_id(event):
    target_phone=my_list_box.get(my_list_box.curselection())
    # target_phone=my_list_box.curselection()


    # print(target_phone)

    return target_phone

def clear_data():

    cmd='adb -s {} shell pm clear {}'.format(target_phone,package_name)
    os.popen(cmd)

def stop_app(target_phone,package_name):
    # target_phone=get_phone_list()
    cmd = 'adb -s {} shell am force-stop {}'.format(target_phone,package_name)
    os.popen(cmd)

def install_app():
    install_cmd = 'adb -s {} install {}'.format(target_phone, file_path)
    os.popen(install_cmd)



my_window=tk.Tk()
my_window.title('手机指令操作')
my_window.geometry('400x600')

file_path, package_name, lanuchableActivity=getPackagInfo()

phone_list=get_phone_list()
target_phone=tk.StringVar()

my_list_box=tk.Listbox(my_window,selectmode='extended')
my_list_box.pack()
for i in phone_list:
    my_list_box.insert('end',i)

my_list_box.bind("<Double-Button-1>", get_phone_id)


'清数据按钮'
clear_data_button=tk.Button(my_window,text='清数据',command=lambda :clear_data(target_phone,package_name))
clear_data_button.pack(side=tk.LEFT)

'安装程序按钮'
install_app_button=tk.Button(my_window,text='安装应用',command=install_app)
install_app_button.pack()

'终止程序'
stop_app_button=tk.Button(my_window,text='终止程序',command=stop_app)
stop_app_button.pack(side=tk.RIGHT)


my_window.mainloop()