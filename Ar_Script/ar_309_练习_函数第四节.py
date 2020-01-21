#encoding=utf-8

#1 用lambda和filter完成下面功能：输出一个列表，列表里面包括：1-100内的所有偶数。（提示：可以用filter,lambda）

targetList=[ i for i in range(1,101)]
result=list(filter(lambda x:x%2==0,targetList))
print(result)

"""
2 用位置匹配，关键字匹配，收集匹配(元组收集,字典收集)分别写4个函数，完成功能；

传递3个列表参数：

[1,2,3],[1,5,65],[33,445,22]

返回这3个列表中元素最大的那个，结果是：445

"""

def func_position(listItem1,listItem2,listItem3):
    extendList=[]
    extendList.extend(listItem1)
    extendList.extend(listItem2)
    extendList.extend(listItem3)

    extendList.sort(reverse=True)
    return extendList[0]

assert func_position([1,2,3],[1,5,65],[33,445,22])==445

def func_keyword(listItem1=[1,2,3],listItem2=[1,5,65],listItem3=[33,445,22]):
    extendList=[]
    extendList.extend(listItem1)
    extendList.extend(listItem2)
    extendList.extend(listItem3)

    extendList.sort(reverse=True)
    return extendList[0]


assert func_keyword()==445


def func_tuple(*listItems):
    extendList = []
    for i in listItems:
        if  isinstance(i,list):

            extendList.extend(i)
        else:
            return '参数有误'
    extendList.sort(reverse=True)
    return extendList[0]

assert func_tuple([1,2,3],[1,5,65],[33,445,22])==445
assert func_tuple('123')=='参数有误'

def func_dict(**listItems):
    extendList = []
    for k,v in listItems.items():
        if isinstance(v,list):
            extendList.extend(v)
        else:
            return '参数有误'
    extendList.sort(reverse=True)
    return extendList[0]

assert func_dict(a=[1,2,3],b=[1,5,65],c=[33,445,22])==445
assert func_dict(str1='123')=='参数有误'

"""
3 递归函数解释，用自己的话说明这个递归函数的工作流程。

def func1(i):
	if i<100:
		return i + func1(i+1)
	return i
print func1(0)

"""

#当i小于100的时候会调用 i+函数自身再传入i+1 第一轮的值相当于 0+func1(0+1)，
# 第二轮相当于1+func1(1+1),直到i大于100，再返回i的初始值0，代入上面的相加过程中得出结果