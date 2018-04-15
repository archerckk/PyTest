'''
编写一个函数，分别统计传入字符串参数（可能不止一个）的英文、数字、空格、其他字符的数量
打印结果：
    第1个字符串共有：英文字符1个，数字1个，空格1个，其他字符1个
'''

'''
1.用收集参数来设置参数
2.拿到参数的列表，统计列表里面每个元素对应类型的数量
3.每循环一次要清0记录的数据
4.开始第二次循环
'''


def countStr(*all):
    strNum = 0
    num = 0
    spaceNum = 0
    otherNum = 0
    length = len(all)
    for i in range(length):
        for each in all[i]:
            if each.isalpha():
                strNum += 1
            elif each.isdigit():
                num += 1
            elif each.isspace():
                spaceNum += 1
            else:
                otherNum += 1
        print('第%d个字符串共有：英文字符%d个，数字%d个，空格%d个，其他字符%d个' % (i + 1, strNum, num, spaceNum, otherNum))
        strNum = 0
        num = 0
        spaceNum = 0
        otherNum = 0

countStr('a1* ','123 abc %&^')

'''
参考答案是将变量的初始化的声明是放在循环的最前面的，外层只声明了一个length
这样的话就可以省去清0这一步了，以后要遇到这种每次循环要重新统计数量的可以用这种两层嵌套循环，外层来初始化来写
'''