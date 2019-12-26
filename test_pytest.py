import pytest

def sum(a,b):

    return a+b

def test_sum():
    assert sum(1,2)==3


class Test_demo:
    # @pytest.fixture(scope='function')
    def setup(self):
        print("setup run")

    def test_sum1(self):
        assert sum(10.1,1.1)==11.2

    def test_sum2(self):
        assert sum(10,1)==11

    # @pytest.fixture(scope='function')
    def teardown(self):
        print("teardown run")

