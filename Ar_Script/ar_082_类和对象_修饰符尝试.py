class Demo:
    @staticmethod
    def test():

        print('这是一个可以调用的静态方法')

    @classmethod
    def test2(cls):
        print('这是一个可以调用的类方法')
class Demo2:pass



Demo.test2()


def test1(fun):
    print('我叫路飞，我是船长')
    fun()
    print('我叫娜美，我是航海士')

@test1
def test2():
    print('我叫索隆，专治各种不服')

test2()
