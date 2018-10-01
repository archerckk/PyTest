import unittest

class Skip_test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @unittest.skip('直接跳过')
    def test_skip(self):
        print('test skip')

    @unittest.skipIf(3>2,'条件为真的话，就不执行')
    def test_skipif(self):
        print('skip if')

    @unittest.skipUnless(3>2,'条件为真的话，就执行')
    def test_unless(self):
        print('unless')

    @unittest.expectedFailure
    def test_failure(self):
        print('failure')

if __name__ == '__main__':
    unittest.main()