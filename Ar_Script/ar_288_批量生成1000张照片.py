import shutil
import os


def getFileName():
    fileList = os.listdir(os.curdir)
    fileName=''
    for i in fileList:
        if os.path.splitext(i)[1]in ['.jpg','.png','.gif','.txt']:
            fileName=i
    return fileName

fileName=getFileName()
print(fileName)


for i in range(1000):
    shutil.copy(fileName, '{}{}'.format(i,fileName))


