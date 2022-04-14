# @Time : 2021/4/6 13:45 

# @Author : 麻花

# @File : logger.py 

# @Software: PyCharm


import logging
import time
import os.path
from Common.dir_config import test_log_path
from Common.generation_path import Generation_Path


class MyLog:

    def my_log(self, msg, level):

        log_name = Generation_Path().generate_path(test_log_path, '.log')

        # 定义一个日志收集器my_logger
        my_logger = logging.getLogger('python11_app_test')
        # 设定级别
        my_logger.setLevel('DEBUG')

        # 没置输出格式
        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-''日志信息:%(message)s')

        # 创建一个我们自己的输出渠道
        ch = logging.StreamHandler()
        ch.setLevel('ERROR')
        ch.setFormatter(formatter)

        fh = logging.FileHandler(log_name, encoding='utf-8')
        fh.setLevel('DEBUG')
        fh.setFormatter(formatter)

        # 两者对接
        my_logger.addHandler(ch)
        my_logger.addHandler(fh)

        # 收集日志

        if level == 'DEBUG':
            my_logger.debug(msg)
        elif level == 'INFO':
            my_logger.info(msg)
        elif level == 'WARNING':
            my_logger.warning(msg)
        elif level == 'ERROR':
            my_logger.error(msg)
        elif level == 'CRITICAL':
            my_logger.critical(msg)
        # 关闭渠道
        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)

    def debug(self, msg):
        self.my_log(msg, 'DEBUG')

    def info(self, msg):
        self.my_log(msg, 'INFO')

    def warning(self, msg):
        self.my_log(msg, 'WARNING')

    def error(self, msg):
        self.my_log(msg, 'ERROR')

    def critical(self, msg):
        self.my_log(msg, 'CRITICAL')


if __name__ == '__main__':
    # pass
    MyLog().my_log('荒野大鳄鱼2', 'ERROR')
    MyLog().my_log('荒野大鳄鱼1', 'ERROR')
