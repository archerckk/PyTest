class Counter:
    def __init__(self):
        '添加一个初始化couner属性，并且初始值为0'
        super().__setattr__('counter', 0)

    def __setattr__(self, name, value):
        '计算初始值+1'
        super().__setattr__('counter', self.counter + 1)
        super().__setattr__(name, value)

    def __delattr__(self, name):
        super().__setattr__('counter', self.counter - 1)
        super().__delattr__(name)