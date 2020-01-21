import os
import time


device_id=input('请输入你的device id：')
now=time.strftime('%Y_%m_%d_%H_%M_%S',time.localtime())
file_name='anr_{}.txt'.format(now)


if device_id !='':
    cmd = 'adb -s {} shell "cp /data/anr/traces.txt /sdcard/{}" '.format(device_id,file_name)
    pull_cmd = 'adb -s{} pull /sdcard/{} d:\Anr'.format(device_id,file_name)
else:
    cmd ='adb shell "cp /data/anr/traces.txt" /sdcard/{}'.format(file_name)
    pull_cmd = 'adb pull /sdcard/{} d:\Anr'.format(file_name)


step=os.popen(cmd).read()
print(step)
time.sleep(2)
copy_file=os.popen(pull_cmd).read()
print(copy_file)