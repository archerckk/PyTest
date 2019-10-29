#encoding=utf-8

"""
求10000以外的100个质数
"""

"""
1.写一个判断质数的方法
2.消耗10000之前的质数生成
3.将10000之后的生成质数加进列表
4.遍历打印这个列表
"""

def is_zhishu(number):

    if number>1:
        if number==2:
            return True
        if number%2==0:
            return  False
        else:
            for i in range(3,number):
                if number%i==0:
                    return False
            return True
    return False

#断言测试
assert is_zhishu(1)==False
assert is_zhishu(2)==True
assert is_zhishu(3)==True
assert is_zhishu(0)==False
assert is_zhishu(5)==True
assert is_zhishu(23)==True


def get_zhishu(ignore_range, numbers):
    number=1
    result=[]
    while len(result)<numbers:
        if number<ignore_range:
           pass
        else:
            if is_zhishu(number):
                result.append(number)
                yield number

        number+=1

result=get_zhishu(100000,10)

result_list=[ i for i in result]
print(result_list)
