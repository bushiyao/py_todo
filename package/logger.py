# coding=utf-8
# @Time : 2022/6/27 11:16 
# @Author : hh
# @File : logger.py 
# @Software: PyCharm


import os, time, sys, json

from time import strftime, localtime
import threading
import logging.handlers

# sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/../'))

# =========================================================================
#
# class CustomLogger
#
# =========================================================================

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(filename)s(%(lineno)d) - %(funcName)s(): %(message)s')

logger = logging.getLogger(__name__)
logger.propagate = False


class CustomLogger:
    def __init__(self, this_file):
        self.this_file = this_file
        self.log_dir = os.getcwd() + os.sep + 'logs' + os.sep
        self.log_filename = ''
        self.today_save = None
        self.fileHandler = None

    def getLogger(self):
        self.check_date()
        return logger

    def now(self):
        tt = time.time()
        local_time = time.localtime(tt)
        now_YMDHMS = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
        millisecond = (tt - int(tt)) * 1000
        time_stamp = "%s.%03d" % (now_YMDHMS, millisecond)

        return ''  # time_stamp

    def _addHandler(self, file_path):
        self.fileHandler = logging.handlers.RotatingFileHandler(file_path, maxBytes=100 * 1024 * 1024,
                                                                backupCount=3, encoding="utf-8", delay=False)

        self.fileHandler.setFormatter(
            logging.Formatter('%(asctime)s - %(filename)s(%(lineno)d)\t%(message)s'))
        # logging.Formatter('%(asctime)s - %(filename)s(%(lineno)d) - %(funcName)s(): %(message)s'))

        logger.addHandler(self.fileHandler)

    def _removeHandler(self):
        if self.fileHandler != None:
            logger.removeHandler(self.fileHandler)

    def _foundHandler(self):
        num = len(logger.handlers)
        for i in range(num):
            # if isinstance(logger.handlers[i], logging.handlers.RotatingFileHandler):
            if self.fileHandler == logger.handlers[i]:
                return True;

        return False

    def get_log_file_and_ip(self):
        return self.raw_input_filename, self.raw_log_ip

    def set_log_file(self, filename='', log_ip='127.0.0.1', ):

        # 避免多次进入，设置多个 fileHandler.
        #
        if self._foundHandler() == True:
            return

        self.raw_input_filename = filename
        self.raw_log_ip = log_ip

        time_stamp = time.strftime("%Y%m%d")
        today_dir = time.strftime("%Y-%m-%d")

        # 新旧时间交替：一元伊始，万象更新 ！
        if self.today_save == None:
            self.today_save = time_stamp
        elif self.today_save != time_stamp:
            self.today_save = time_stamp

        # 改造 根据pid区分进程日志
        if len(filename) == 0:
            filename = str(os.getpid())

        # the final logfile
        self.log_filename = time_stamp + '_{}_{}.log'.format(log_ip.replace('.', '-'), filename)

        today_dir = self.log_dir + today_dir

        # create the log dir
        try:
            if not os.path.exists(today_dir):
                os.makedirs(today_dir)
        except Exception as e:
            print("os.makedirs('{}': {}".format(today_dir, repr(e)))

        file_path = today_dir + os.sep + self.log_filename

        self._addHandler(file_path)

    def check_date(self):
        # 判断今天的日期是否有已经改变？
        today = time.strftime("%Y%m%d")
        if (today != self.today_save):
            self._removeHandler()
            self.set_log_file(filename=self.raw_input_filename, log_ip=self.raw_log_ip)

        # 线程是需要随时动态获取的
        pid_str = str(os.getpid())
        tid_str = str(threading.currentThread().ident)

        self.pid_tid_str = '[pid={}, tid={}] - '.format(pid_str, tid_str)

    def getId(self):
        return self.pid_tid_str

    def write(self, level='info', *args):
        if len(self.log_filename) == 0:
            print(self.now() + " - " + " ".join(args))
        else:

            # 检查日期是否已更新
            self.check_date()

            if level == 'info':
                logger.info(self.now() + self.getId() + " ".join(args))
            elif level == 'debug':
                logger.debug(self.now() + self.getId() + " ".join(args))
            elif level == 'error':
                logger.error(self.now() + self.getId() + " ".join(args))
            elif level == 'warning':
                logger.warning(self.now() + self.getId() + " ".join(args))

    def write_except(self, e):  # 打印异常信息
        # logger.info(self.now() + " - " + str(e))
        logger.info(self.now() + " - " + str(e))

    # 1. error/log_error
    def error(self, msg):
        self.log_error(msg)

    def log_error(self, msg):
        self.write('error', msg)

    # 2. info/log_info
    def info(self, msg):
        self.log_info(msg)

    def log_info(self, msg):
        self.write('info', msg)

    # 3. warning/log_warning
    def warning(self, msg):
        self.log_warning(msg)

    def log_warning(self, msg):
        self.write('warning', msg)

    # 4. debug/log_debug
    def debug(self, msg):
        self.log_debug(msg)

    def log_debug(self, msg):
        self.write('debug', msg)

    def write_bootinfo(self):
        strTitle = "========  Start to launch '{}'  =============".format(os.path.abspath(sys.argv[0]))

        text_len = len(strTitle)

        i = 0
        strBanner = ''
        while i < text_len:
            strBanner += '='
            i += 1

        self.info(strBanner)  # ("=================================================")
        self.info(strTitle)
        self.info(strBanner)


if __name__ == '__main__':
    log = CustomLogger(__file__)
    log.set_log_file(log_ip='127.0.0.1', filename='log-test')

    log.log_error('error...')
    log.log_info('info ...')
    log.log_debug('debug ...')
    log.log_warning('warning...')
