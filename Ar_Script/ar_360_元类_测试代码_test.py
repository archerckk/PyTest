import pytest


def upper_attr(future_class_name, future_class_parents, future_class_attr):
    '''返回一个类对象，将属性都转为大写形式'''
    #  选择所有不以'__'开头的属性
    attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
    # 将它们转为大写形式
    uppercase_attr = dict((name.upper(), value) for name, value in attrs)
    print(uppercase_attr)

    # 通过'type'来做类对象的创建
    return type(future_class_name, future_class_parents, uppercase_attr)


# __metaclass__ = upper_attr  # 这会作用到这个模块中的所有类

__metaclass__ = upper_attr

class Foo(object):
    __metaclass__ = upper_attr
    # 我们也可以只在这里定义__metaclass__，这样就只会作用于这个类中
    bar = 'bip'

# print(dir(Foo))

import random

data={
    'key1':random.sample(range(10),3),
    'key2':random.sample(range(10),3),
}


@pytest.mark.parametrize('a',[1,2,3])
def test_demo(a):
    print(f'启动测试数据：{a}')