import os

'需要手机调试模式成功，并且目标程序已经运行'
def get_meminfo():
    command="adb shell dumpsys meminfo com.picstudio.photoeditorplus"

    cmd_Log=os.popen(command).readlines()
    result_list=[]
    for i in cmd_Log:
        if 'TOTAL' in i:
            i=i.split(' ')
            while ''in i:
                i.remove('')
            result_list.append(i)

    allocSize=result_list[0][6]
    allocSize/1024
    # print(allocSize)
    return allocSize




