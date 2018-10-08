import subprocess
import os

filename=os.getcwd()+os.sep+'test_case'+os.sep+'driver'+os.sep+'selenium-server-standalone-3.14.0.jar'
command='java -jar %s'%filename
subprocess.Popen(command,shell=True)