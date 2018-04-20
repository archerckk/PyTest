print()
'''
编写一个程序，当用户输入文件名和行数后，将该文件的前N行内容打印到屏幕上
如：
    文件【xx】的前xx行的内容如下：
    
    XXXXX

'''

def printLine(fileName,lines):
    f=open('resources/%s'%fileName)
    lines=int(lines)
    print('\n文件【%s】的前%d行的内容如下：\n'%(fileName,lines))

    for i in range(lines):
        'readline()也是需要用print打印出来的'
        print(f.readline())

    f.close()

fileName=input('请输入你要打开的文件名：')
lines=input('请输入需要显示该文件前几行：')
printLine(fileName,lines)



