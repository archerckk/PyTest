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


"""
3 递归函数解释，用自己的话说明这个递归函数的工作流程。

def func1(i):
	if i<100:
		return i + func1(i+1)
	return i
print func1(0)

"""
