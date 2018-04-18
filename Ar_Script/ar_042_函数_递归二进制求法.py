print()
'使用递归编写一个十进制转换为二进制的函数（要求采用“取2取余”的方式，结果与调用bin()一样返回字符串形式）'

def Dec2Bin(dec):
    result = ""

    if dec:
        '赋值之后不代表它最终的值，return之后还是可以改变它的值的'
        result = Dec2Bin(dec // 2)
        '先将result调用函数自身保存起来，再返回result+转变成字符串的求余结果回推'
        return result + str(dec % 2)
        #
    else:
        return result


print(Dec2Bin(8))