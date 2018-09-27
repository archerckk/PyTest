import unittest

def setUpModule():
    print('test modle strat >>>>>>>>>>>')

def tearDownModule():
    print('test modle end >>>>>>>>>>>')

class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('test class start -----------')

    @classmethod
    def tearDownClass(cls):
        print('test class end --------------')

    def setUp(self):
        print('test start ----->')

    def tearDown(self):
        print('test end -------->')

    def test_print(self):
        print('print aaaa')

if __name__ == '__main__':
    unittest.main()