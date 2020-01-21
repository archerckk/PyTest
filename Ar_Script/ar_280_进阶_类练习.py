class A:
    def __init__(self):
        print('A class call ')

class B(A):
    def __init__(self):
        print('B class call')
        A.__init__(self)

class C(A):
    def __init__(self):
        print('C class call')
        A.__init__(self)

class D(B,C):
    def __init__(self):
        print('D class call')
        B.__init__(self)
        C.__init__(self)

d=D()