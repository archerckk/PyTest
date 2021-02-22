import  json

# 字典排序
dict1={'a':1,'d':3,'c':2}
dict1_to_list=list(dict1.items())
dict1_to_list.sort(key=lambda k:k[1])
print(dict(dict1_to_list))


# 字符串转换成功json格式
str1='{"a":1,"d":3,"c":2}'
json_result=json.loads(str1)
print(type(json_result),json_result)
tmp_list=list(json_result.items())
tmp_list.sort(key=lambda k:k[1])
print(dict(tmp_list))

# filter 的使用
filter_result=list(filter(lambda x:x%2,range(10)))
print(filter_result)

# map的使用
map_result=list(map(lambda x:x**2,range(10)))
print(map_result)