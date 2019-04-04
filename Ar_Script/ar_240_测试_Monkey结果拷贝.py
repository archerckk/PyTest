import easygui as g
import os

key_word_input=g.enterbox(msg='请输入你的拷贝结果文件名：',title='结果输入')
target_file="/sdcard/%s"%key_word_input
computer_file="D:\monkey_result\%s"%(key_word_input)

command="adb pull %s %s"%(target_file,computer_file)
run_command=os.popen(command).read()
print(run_command)
