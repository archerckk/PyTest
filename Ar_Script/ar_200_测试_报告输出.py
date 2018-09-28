import subprocess
import os


file_name=os.getcwd()+os.sep+'ar_199_测试_fixtures.py'
command='python %s'%file_name
with open('log_save.txt','w')as log:
    subprocess.Popen(command,stdout=log,shell=True).wait(5)
