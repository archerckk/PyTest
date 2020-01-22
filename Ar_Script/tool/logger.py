import logging
from logging import handlers


class Loger(object):

    def __init__(self,fileName):
        self.log = logging.getLogger()

        # 2、设置文件跟屏幕输出的handler
        # filehandler = logging.FileHandler(filename="all.log.123", mode="a", encoding="utf-8")  # 默认
        self.filehandler=handlers.TimedRotatingFileHandler(filename=fileName,when='D',backupCount="3",encoding='utf-8')
        self.streamhandler = logging.StreamHandler()

        # 3、设置格式化输出
        formatter = logging.Formatter(fmt="%(asctime)s-%(levelname)s-%(message)s")

        # 4.绑定关系：①logger绑定handler
        self.log.addHandler(self.filehandler)
        self.log.addHandler(self.streamhandler )

        # ②为handler绑定formatter
        self.filehandler.setFormatter(formatter)
        self.streamhandler .setFormatter(formatter)

        # 5、设置日志级别各个对象的日志级别
        self.log.setLevel(10)
        self.filehandler.setLevel(10)
        self.streamhandler .setLevel(10)