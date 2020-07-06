import tkinter as tk
from tkinter import *
import os
from tool.get_packageinfo import getPackagInfo
from tool.logger import Loger
import logging


def get_phone_info():
    cmd = 'adb devices'
    device_output = os.popen(cmd).readlines()
    phone_list = []

    for line in device_output:
        if "devices" not in line:
            device = '#'.join(line.split())
            phone_name = device.split('#')[0]
            phone_list.append(phone_name)
    if '' in phone_list:
        phone_list.remove('')

    return phone_list


def get_phone_list(my_list_box):
    phone_list_for_button = get_phone_info()

    my_list_box.delete(0, END)

    for i in phone_list_for_button:
        my_list_box.insert(END, i)

    return phone_list_for_button


def get_phone_id(event):
    target_phone = my_list_box.get(my_list_box.curselection())
    # target_phone=my_list_box.curselection()

    logging.debug('选择设备为：{}'.format(target_phone))

    return target_phone


def clear_data(package_name):
    target_phone = my_list_box.get(my_list_box.curselection())

    cmd = 'adb -s {} shell pm clear {}'.format(target_phone, package_name)
    os.popen(cmd)
    logging.debug('清除{}手机的{}应用数据'.format(target_phone, package_name))


def stop_app(package_name):
    target_phone = my_list_box.get(my_list_box.curselection())
    cmd = 'adb -s {} shell am force-stop {}'.format(target_phone, package_name)
    os.popen(cmd)
    logging.debug('停止{}手机的{}'.format(target_phone, package_name))


def uninstall_app(package_name):
    target_phone = my_list_box.get(my_list_box.curselection())
    cmd = 'adb -s {} uninstall {}'.format(target_phone, package_name)
    os.popen(cmd)
    logging.debug('卸载{}手机的{}'.format(target_phone, package_name))


def install_app():
    target_phone = my_list_box.get(my_list_box.curselection())
    file_path, package_name, lanuchableActivity = getPackagInfo()
    install_cmd = 'adb -s {} install {}'.format(target_phone, file_path)
    os.popen(install_cmd)
    logging.debug('安装{}到{}手机,包名为：{}'.format(file_path, target_phone, package_name))


def install_all_phone():
    phone_name_list = get_phone_info()
    file_path, package_name, lanuchableActivity = getPackagInfo()

    for phone in phone_name_list:
        uninstall_cmd = 'adb -s {} uninstall {}'.format(phone, package_name)
        log = os.popen(uninstall_cmd)
        logging.debug('手机{}：执行卸载\n{}'.format(phone, log.read()))

    for phone in phone_name_list:
        install_cmd = 'adb -s {} install {}'.format(phone, file_path)
        log = os.popen(install_cmd)
        logging.debug('安装{}到{}手机,包名为：{}\n{}'.format(file_path, phone, package_name, log.read()))


def override_install_phone(override='r'):
    target_phone = my_list_box.get(my_list_box.curselection())
    file_path, package_name, lanuchableActivity = getPackagInfo()
    install_cmd = 'adb -s {} install -{} {}'.format(target_phone, override, file_path)
    os.popen(install_cmd)
    logging.debug('安装{}到{}手机,包名为：{}'.format(file_path, target_phone, package_name))


def clear_gp_data():
    package_gp = 'com.android.vending'
    target_phone = my_list_box.get(my_list_box.curselection())
    clear_gp_data_cmd = 'adb -s {} shell pm clear {}'.format(target_phone, package_gp)
    log = os.popen(clear_gp_data_cmd)
    logging.debug("清除{}手机的GP数据\n{}".format(target_phone, log.read()))


my_loger = Loger()
my_window = tk.Tk()
my_window.title('手机指令操作')
my_window.geometry('400x400')

file_path, package_name, lanuchableActivity = getPackagInfo()

'测试代码'
# file_path, package_name, lanuchableActivity=1,2,3


target_phone = tk.StringVar()

my_list_box = tk.Listbox(my_window, selectmode='extended')
my_list_box.grid(row=1, column=1, columnspan=10, padx=30, pady=30, sticky="nsew")

phone_list = get_phone_list(my_list_box)

my_list_box.bind("<Double-Button-1>", get_phone_id)

'刷新手机连接列表'
flash_phone_list_button = tk.Button(my_window, text='刷新列表', command=lambda: get_phone_list(my_list_box))
flash_phone_list_button.grid(row=2, column=1, padx=10, pady=20)

'清除数据按钮'
clear_data_button = tk.Button(my_window, text='清除数据', command=lambda: clear_data(package_name))
clear_data_button.grid(row=2, column=2, padx=10, pady=20)
#
'终止程序'
# print('测试数据:',target_phone)
stop_app_button = tk.Button(my_window, text='终止程序', command=lambda: stop_app(package_name))
stop_app_button.grid(row=2, column=3, padx=10, pady=20)

"清除GP数据"
clear_gp_data_button=tk.Button(my_window, text='谷歌清理', command=clear_gp_data)
clear_gp_data_button.grid(row=2, column=4, padx=10, pady=20)

'卸载app'
uninstall_app_button = tk.Button(my_window, text='卸载程序', command=lambda: uninstall_app(package_name))
uninstall_app_button.grid(row=2, column=5, padx=10, pady=20)

"安装所有手机"
install_all_phone_button = tk.Button(my_window, text='遍历安装', command=install_all_phone)
install_all_phone_button.grid(row=3, column=1, padx=10, pady=20)

'安装程序按钮'
install_app_button = tk.Button(my_window, text='安装应用', command=install_app)
install_app_button.grid(row=3, column=2, padx=10, pady=20)

"覆盖安装app"
override_install_button = tk.Button(my_window, text='覆盖安装', command=override_install_phone)
override_install_button.grid(row=3, column=3, padx=10, pady=20)



my_window.mainloop()
