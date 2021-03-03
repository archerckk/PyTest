import json

# 字典排序
dict1 = {'a': 1, 'd': 3, 'c': 2}
dict1_to_list = list(dict1.items())
dict1_to_list.sort(key=lambda k: k[1])
print(dict(dict1_to_list))

# 字符串转换成功json格式
str1 = '{"a":1,"d":3,"c":2}'
json_result = json.loads(str1)
print(type(json_result), json_result)
tmp_list = list(json_result.items())
tmp_list.sort(key=lambda k: k[1])
print(dict(tmp_list))

# filter 的使用
filter_result = list(filter(lambda x: x % 2, range(10)))
print(filter_result)

# map的使用
map_result = list(map(lambda x: x ** 2, range(10)))
print(map_result)

# 给定一个正整数，编写程序计算多少对质数的和等于这个正整数，并输出结果。输入值小于1000.如输入10，程序应该输入结果为2[(3,7),(5,5)]
# num=10
num_list = []
result_list = []


def judge_num(num):
    for i in range(2, num):
        if num % i == 0:
            # print(num,'不是质数')
            return False
    else:
        return True



def get_num_list(num):
    for i in range(2, num):
        if judge_num(i):
            print(i)
            num_list.append(i)
    print(num_list)
    return num_list


def cal_length(num):
    get_num_list(num)
    # print(num_list)

    for i in num_list:
        for j in num_list:
            if i + j == num :
                    result_list.append((i, j))

    del_num(result_list)

    print(result_list)
    length = len(result_list)

    return length

def del_num(num):
    for i in num:
        tmp=tuple(reversed(list(i)))
        print('临时变量为：',tmp)
        if result_list.count(tmp)!= 0:
            if tmp==i :
                continue
            else:
                result_list.remove(tmp)
        else:
            continue
    print("删除结果为:",num)






print(cal_length(10))
