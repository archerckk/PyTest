'异常处理并行写法'
try:
    # a=1+'2'
    assert 1<2,'条件为false，报错'
except (TypeError,AssertionError)as e:
    print("error message1:{}".format(e))
'''
这种写法的话，异常处理只能捕捉到第一个异常，然后第二行代码就没有执行了
'''

'异常处理分代码保护'
try:
    a=1+'2'
    try:
        assert SyntaxError
    except Exception as e:
        print('error message:{}'.format(e))
except (TypeError,AssertionError)as e:
    print("error message:{}".format(e))