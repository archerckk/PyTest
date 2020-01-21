#encoding


"""
定义一个列表的操作类：Listinfo

包括的方法:

1 列表元素添加: add_key(keyname)  [keyname:字符串或者整数类型]
2 列表元素取值：get_key(num) [num:整数类型]
3 列表合并：update_list(list)	  [list:列表类型]
4 删除并且返回最后一个元素：del_key()

list_info = Listinfo([44,222,111,333,454,'sss','333'])

"""
class Listinfo(object):


    def __init__(self,list_value):
        self.list_value = list_value
        self.maxLength=0

    def add_key(self,keyname):

        if not isinstance(keyname, int) and not isinstance(keyname, str):
            return '参数传入并不是整形或者字符串'

        self.list_value.append(keyname)
        return self.list_value

    def get_key(self,num):
        self.maxLength=len(self.list_value)

        if not isinstance(num,int):
            return '你所传入的参数不是整形数据'

        if num>self.maxLength:
            return '你所传入的索引值超过列表的最大长度'

        return self.list_value[num-1]

    def update_list(self,list_value):
        if not isinstance(list_value, list):
            return '你所传入的参数不是列表'
        self.list_value.extend(list_value)
        return self.list_value

    def del_key(self):

        self.tmp_value=self.list_value[-1]
        del self.list_value[-1]
        return self.tmp_value

l=Listinfo([44,222,111,333,454,'sss','333'])
a=l.add_key(2)
print(a)
b=l.get_key(1)
print(b)
c=l.update_list([1,1,1])
print("扩展列表为：",c)

l.del_key()
print("执行删除后的列表数据为：",l.list_value)


"""

list_info = Listinfo([44,222,111,333,454,'sss','333'])

定义一个集合的操作类：Setinfo

包括的方法:

1 集合元素添加: add_setinfo(keyname)  [keyname:字符串或者整数类型]
2 集合的交集：get_intersection(unioninfo) [unioninfo :集合类型]
3 集合的并集： get_union(unioninfo)[unioninfo :集合类型]
4 集合的差集：del_difference(unioninfo) [unioninfo :集合类型]

set_info =  Setinfo(你要操作的集合)

"""

class Setinfo(object):

    def __init__(self,set_value):
        self.set_value=set_value

    def add_setinfo(self,keyname):
        if not isinstance(keyname, int) and not isinstance(keyname, str):
            return '参数传入并不是整形或者字符串'

        self.set_value.add(keyname)
        return self.set_value

    def get_intersection(self,union_value):
        if not isinstance(union_value, set):
            return '你所传入的参数不是集合'
        self.set_value=self.set_value.intersection(union_value)

        return self.set_value
    def get_union(self,union_value):
        if not isinstance(union_value, set):
            return '你所传入的参数不是集合'
        self.set_value = self.set_value.union(union_value)

        return self.set_value

    def del_difference(self,union_value):
        if not isinstance(union_value, set):
            return '你所传入的参数不是集合'

        self.set_value = self.set_value.difference(union_value)

        return self.set_value

setInfo=Setinfo({1,2,3})
a=setInfo.add_setinfo(4)
print('新增元素',a)
b=setInfo.get_intersection({2,3})
print("交集",b)
c=setInfo.get_union({6,7,5})
print('并集',c)
d=setInfo.del_difference({3})
print('差分',d)