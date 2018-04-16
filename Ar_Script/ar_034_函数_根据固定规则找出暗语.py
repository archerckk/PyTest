'''
请用已学过的知识编写程序，找出小甲鱼藏在下边这个长字符串中的密码，密码埋藏点有以下规律：
每位密码为单个小写字母
每位密码的左右两边均有且只有三个大写字母
'''

'''
1.将目标文本的内容拿出来，并且加到一个字符串当中(方便用字符串方法处理)
2.首先要定义三个变量来接收前面3个大写，中间小写，后面3个大写的计数
3.要多换行符\n进行处理
4.用range+字符串长度的方式来定位对应的字符位置跟比较前后的状态
5.统计前面3个大写字母

'''


def findCode():
    fileCode = open('resources/string2.txt')
    str1 = ''
    # str1='ABCaABCaABCaABC'
    countA = 0
    countB = 0
    countC = 0
    length = len(str1)
    # target = []
    for i in fileCode:
        str1 += i

    # print(str1)

    '''测试代码只判断一行的话是没有问题的，但是多行有问题，
    自己应该就能定位到是换行符这边的问题了，经验还是不够'''

    for i in range(length):
        if str1[i] == '\n':
            continue

        '''假如是小写字母的话，先判断是不前面大写字母的数量是不是3，不是的话全部计数清0
           假如前面的数字是3的话，在看看有没有小写字母，有的话，全部计数清0，
           不是的话小写字母数就等于1，目标为该数字'''

        if str1[i].isupper():
            if countB:
                countC += 1
            else:
                countC = 0
                countA += 1

        '''假如前后两个大写字母的数量都是正确的，再看看第四个字母是不是大写，
            是的话小写跟后面的大写字母数清零，否则的话要打印现在的所在字符串'''

        if str1[i].islower():
            if countA != 3:
                countA = 0
                countB = 0
                countC = 0
            else:
                if countB:
                    countA = 0
                    countB = 0
                    countC = 0
                else:
                    countB = 1
                    countC = 0
                    target = i

        '''假如前后两个大写字母的数量都是正确的，再看看第四个字母是不是大写，
            是的话小写跟后面的大写字母数清零，否则的话要打印现在的所在字符串'''

        if countA == 3 and countC == 3:
            if i + 1 != length and str1[i + 1].isupper():
                countB = 0
                countC = 0
            else:
                print(str1[target], end='')
                countA = 3

                countB = 0
                countC = 0


findCode()
