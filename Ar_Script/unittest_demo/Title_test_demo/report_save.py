import subprocess
import os
import time

run_script=os.getcwd()+os.sep+'runtest.py'
runtime=time.strftime('%Y_%m_%d_%H_%M_%S',time.localtime())
file='Report/report_%s.txt'%runtime
command='python %s >> file'%run_script

# with open('Report/report_%s.txt'%runtime,'w')as log:
#     subprocess.Popen(command,shell=True,stdout=log).wait()
subprocess.Popen(command, shell=True).wait()
# log=subprocess.Popen(command,shell=True,stdout=subprocess.PIPE)
# print(log.stdout.read())