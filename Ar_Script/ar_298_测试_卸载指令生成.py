import openpyxl
import easygui

xlFile=easygui.fileopenbox(title='Excel选择',msg='请选择你要选择的文件',filetypes='.xlsx')
col=input('请输入列字母:')
firstNum=int(input('请输入起始行：'))
secondNum=int(input('请输入结束行：'))

wb=openpyxl.load_workbook(xlFile)
ws=wb.active
packageNameList=[]

for i in range(firstNum,secondNum+1):
    packageNameList.append(ws['%s%s'%(col,i)].value)


newList=["adb uninstall {}".format(i) for i in packageNameList]

resultFile='adbOut.txt'
with open(resultFile,'w')as f:
        for i in newList:
            f.write(i+'\n')

