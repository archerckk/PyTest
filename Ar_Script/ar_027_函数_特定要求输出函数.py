'''
编写一个符合以下要求的函数
	a 计算打印所有参数的和乘以基数（base=3）的结果
    b 如果参数中最后一个参数为（base=5），则最后一个数参数不参与求和，并将和乘以基数5
'''


def sum(*program):
    'help:'
    '定义一个sum变量接收他们的和'
    '判断最后一个参数是否为5'
    '为5则求和不包括5,乘以基数5'
    '不为5则一并求和乘以基数3'
    sum = 0
    length=len(program)
    if program[length - 1] == 5:
        for i in range(length-1):
            sum += program[i]
        sum = sum*5

        # for i in program:
        #     sum+=i
        # sum=(sum-5)*5

    else:
        for i in program:
            sum += i
        sum *= 3
    return sum


print(sum(1, 2, 3, 5))
