import logging
from logging import handlers


class Loger(object):

    def __init__(self, fileName, level="debug", mode='w',error_record=False):
        self.log = logging.getLogger()

        self.level_dict = {
            'critical': 50,
            'error': 40,
            'warning': 30,
            'info': 20,
            'debug': 10
        }

        # 2、设置文件跟屏幕输出的handler
        self.filehandler = logging.FileHandler(filename=fileName + '.log', mode=mode, encoding="utf-8")  # 默认
        # self.filehandler=handlers.TimedRotatingFileHandler(filename=fileName,when='D',backupCount="3",encoding='utf-8')
        self.streamhandler = logging.StreamHandler()


        # 3、设置格式化输出
        formatter = logging.Formatter(fmt="%(asctime)s-%(levelname)s-%(message)s")

        # 4.绑定关系：①logger绑定handler
        self.log.addHandler(self.filehandler)
        self.log.addHandler(self.streamhandler)

        # ②为handler绑定formatter
        self.filehandler.setFormatter(formatter)
        self.streamhandler.setFormatter(formatter)

        # 5、设置日志级别各个对象的日志级别
        self.log.setLevel(self.level_dict[level])
        self.filehandler.setLevel(self.level_dict[level])
        self.streamhandler.setLevel(self.level_dict[level])

        if error_record:
            self.errorhandler = logging.FileHandler(filename=fileName + ".error_log", mode=mode, encoding="utf-8")
            self.log.addHandler(self.errorhandler)
            self.errorhandler.setFormatter(formatter)
            self.errorhandler.setLevel(40)