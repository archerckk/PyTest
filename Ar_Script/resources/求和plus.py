'过滤字符串对于求和的影响'

def sum(x):
    result=0
    for i in x:
        if type(i)==float or type(i)==int:
            result=result+i
        else:
            continue
    return result

print(sum([1,2,4,5,6,3.15,7.25,'sdfdsf',10*10]))