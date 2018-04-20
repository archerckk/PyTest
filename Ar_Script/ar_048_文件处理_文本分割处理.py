print()
'''
1.先打开文件，拿到里面的内容(open())
2.针对每一行进行进行分割(split)
3.判断到分割线的话就保存文件到指定的目录(save)
'''


def save_file(boy,girl,count):
    '分别打开两个文件，记录文件的保存的序号'
    f1=open('result/boy%d.txt'%count,'w')
    f2=open('result/girl%d.txt'%count,'w')

    f1.writelines(boy)
    f2.writelines(girl)

    f1.close()
    f2.close()

def splitStr():
    count = 1
    targetFile = open('resources/record.txt')
    boy=[]
    girl=[]
    for i in targetFile:
        '在分割之前一定要判断内容是否符合格式，符合格式才能进行分割，不然会报错参数数量异常'
        if i[:6]!='======':
            '自己一直以为自己记错了语法，但是调试了测试代码，没有报错，原来是上面的原因，之前并没有理解清楚'
            (begin,end) = i.split(':',1)
            if begin == '小甲鱼':
                boy.append(i)
            if begin == '小客服':
                girl.append(i)
        else:
            '早上的时候想着用全局变量来传参数，但是函数跟函数之间本身是可以传参数的嘛，真的是路径依赖'
            save_file(boy,girl,count)
            count+=1
            '输出的结果的条数有重复，清空之前保存的列表'
            boy.clear()
            girl.clear()
    '一共只能保存两次，所以要在外层再执行一遍保存函数'
    save_file(boy, girl, count)
    '记得关闭文件'
    targetFile.close()

splitStr()

