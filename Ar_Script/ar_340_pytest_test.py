import pytest
import logging
import allure

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s')

def sum(a,b):

    return a+b

def test_sum():
    assert sum(1,2)==3


class Test_demo:
    @pytest.fixture(scope='function',autouse=True)
    def setup(self):
        logging.debug("setup run")


    @pytest.mark.some
    def test_sum1(self):
        logging.debug('run test_sum1')
        assert sum(10.1,1.1)==11.2

    @allure.step('参数化设置测试用例')
    @pytest.mark.web
    @pytest.mark.parametrize('a,b,expect',[
        (10,1,11),
        (12,1,13),
        (11,2,14),
        (11,2,15)
    ])
    def test_sum2(self,a,b,expect):
        logging.debug('sum2')
        assert sum(a,b)==expect

    # @pytest.fixture(scope='function',autouse=True)
    def teardown(self):
        logging.debug("teardown run")


if __name__ == '__main__':
    # pytest.main(['-s','-v','-m not some','test_pytest.py'])
    pytest.main(['-s','ar_340_pytest_test.py'])
