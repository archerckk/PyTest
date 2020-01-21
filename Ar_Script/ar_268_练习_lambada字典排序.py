import time

# dict1={'a':2,'b':1}
# x=sorted(dict1.items(),key=lambda x:x[1])
# y=sorted(dict1.items(),key=lambda x:x[0])
# print(y)
# print(x)

id=[x for x in range(1,100001)]
price=[x for x in range(200000,300000)]
product=list(zip(id,price))

'list version'
def find_unique_price_num_list(product):
    resultList=[]
    for _,price in product:
        if price not in resultList:
            resultList.append(price)
    length=len(resultList)
    return length

'set version'
def find_unique_price_num_set(product):
    uniqueSet=set()
    for _,price in product:
        uniqueSet.add(price)
    length=len(uniqueSet)
    return length

'计算并打印列表的执行时间'
startListTime=time.perf_counter()
# find_unique_price_num_list(product)
s=''
for i in range(0,1000000):
    s+=str(i)
endListTime=time.perf_counter()
print('列表版本的执行时间为：{}'.format(endListTime-startListTime))

'计算并打印集合的执行时间'
startSetTime=time.perf_counter()
# find_unique_price_num_set(product)
l=[]
for i in range(0,1000000):
    l.append(str(i))
result=''.join(l)
print(result)
endSetTime=time.perf_counter()
print('集合版本的执行时间为：{}'.format(endSetTime-startSetTime))