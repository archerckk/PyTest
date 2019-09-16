#encoding=utf-8

"""
1 写一个函数代码，返回这3个数字中最大的一个。

a = 123

b = 345

c = 444

"""
def returnMax(*item):
    max=0
    for i in item:
        if int(i)>max:
            max=i
        else:
            max=max

    return max

a = 123

b = 99

c = 444

d=555

print(returnMax(a,b,c,d))


"""
2.1 调用函数：ainfo(x=88,y=22,z=44) 你定义ainfo函数体里面的内容并且返回结果： 

[22, 44, 88]
"""
def ainfo(**item):
    list1=[]
    for i in item.values():
        list1.append(i)
    list1=sorted(list1)
    return list1

print(ainfo(x=88,y=22,z=44))

"""
2.2 调用函数：cinfo(x=88,y=22,z=44) 你定义cinfo函数体里面的内容并且返回结果：

('xaay','yaay','zaay')

"""
def cinfo(**item):
    list1=[]
    for i in item.keys():
        list1.append(i)
    list1=sorted(list1)
    list1=[{"{}aay".format(i)} for i in list1]
    return list1

print(cinfo(x=88,y=22,z=44))