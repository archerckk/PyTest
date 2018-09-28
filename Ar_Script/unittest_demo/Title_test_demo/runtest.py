import unittest

start_dir='./'
discover=unittest.defaultTestLoader.discover(start_dir,pattern='test*.py')

if __name__ == '__main__':
    runner=unittest.TextTestRunner()
    runner.run(discover)