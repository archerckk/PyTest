class Test:
    def __getattr__(self, item):
        return '你访问的属性不存在！！'

test=Test()
print(test.x)