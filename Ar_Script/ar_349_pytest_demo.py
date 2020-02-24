import logging
from logging import handlers
import pytest

# class Logger(object):
#     level_relations = {
#         'debug':logging.DEBUG,
#         'info':logging.INFO,
#         'warning':logging.WARNING,
#         'error':logging.ERROR,
#         'crit':logging.CRITICAL
#     }#日志级别关系映射
#
#     def __init__(self,filename,level='info',when='D',backCount=3,fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
#         self.logger = logging.getLogger(filename)
#         format_str = logging.Formatter(fmt)#设置日志格式
#         self.logger.setLevel(self.level_relations.get(level))#设置日志级别
#         sh = logging.StreamHandler()#往屏幕上输出
#         sh.setFormatter(format_str) #设置屏幕上显示的格式
#         th = handlers.TimedRotatingFileHandler(filename=filename,when=when,backupCount=backCount,encoding='utf-8')#往文件里写入#指定间隔时间自动生成文件的处理器
#         #实例化TimedRotatingFileHandler
#         #interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
#         # S 秒
#         # M 分
#         # H 小时、
#         # D 天、
#         # W 每星期（interval==0时代表星期一）
#         # midnight 每天凌晨
#         th.setFormatter(format_str)#设置文件里写入的格式
#         self.logger.addHandler(sh) #把对象加到logger里
#         self.logger.addHandler(th)

class Test_demo:

    def setUP(self):
        logging.debug('setup执行了')


    def test_app(self):
        assert 1==1


    def teardown(self):
        logging.debug('teardown执行了')

if __name__ == '__main__':
    log = logging.getLogger()

    # 2、设置文件跟屏幕输出的handler
    # filehandler = logging.FileHandler(filename="all.log.123", mode="a", encoding="utf-8")  # 默认
    filehandler=handlers.TimedRotatingFileHandler(filename="all.log",when='D',backupCount="3",encoding='utf-8')
    streamhandler = logging.StreamHandler()

    # 3、设置格式化输出
    formatter = logging.Formatter(fmt="%(asctime)s-%(levelname)s-%(message)s")

    # 4.绑定关系：①logger绑定handler
    log.addHandler(filehandler)
    log.addHandler(streamhandler)

    # ②为handler绑定formatter
    filehandler.setFormatter(formatter)
    streamhandler.setFormatter(formatter)

    # 5、设置日志级别各个对象的日志级别
    log.setLevel(10)
    filehandler.setLevel(10)
    streamhandler.setLevel(10)


    logging.debug('print')
    pytest.main('ar_349_pytest_demo.py::Test_demo')