import tkinter as tk
from tkinter import ttk
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

    print(target_phone)

    return target_phone

def clear_data(package_name):
    target_phone=my_list_box.get(my_list_box.curselection())

    cmd='adb -s {} shell pm clear {}'.format(target_phone,package_name)
    os.popen(cmd)


def stop_app(package_name):

    target_phone=my_list_box.get(my_list_box.curselection())
    cmd = 'adb -s {} shell am force-stop {}'.format(target_phone,package_name)
    os.popen(cmd)

def uninstall_app(package_name):

    target_phone=my_list_box.get(my_list_box.curselection())
    cmd = 'adb -s {} uninstall {}'.format(target_phone,package_name)
    os.popen(cmd)


def install_app():
    target_phone=my_list_box.get(my_list_box.curselection())
    file_path, package_name, lanuchableActivity = getPackagInfo()
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

# my_combo_box=ttk.Combobox(my_window,variable=target_phone)
# my_combo_box['values']=tuple(phone_list)
# my_combo_box.current(0)
#
# my_combo_box.bind('<<ComboboxSelected>>',)
# my_combo_box.pack()

'清数据按钮'
clear_data_button=tk.Button(my_window,text='清数据',command=lambda :clear_data(package_name))
clear_data_button.pack(side=tk.LEFT)

'安装程序按钮'
install_app_button=tk.Button(my_window,text='安装应用',command=lambda :install_app(file_path))
install_app_button.pack()

'终止程序'
# print('测试数据:',target_phone)
stop_app_button=tk.Button(my_window,text='终止程序',command=lambda :stop_app(package_name))
stop_app_button.pack(side=tk.RIGHT)

'卸载app'
uninstall_app_button=tk.Button(my_window,text='卸载程序',command=lambda :uninstall_app(package_name))
uninstall_app_button.pack(side=tk.RIGHT)


my_window.mainloop()