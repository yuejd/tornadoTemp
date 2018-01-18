#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   Jiadi Yue
#   E-mail  :   jdyue19@gmail.com
#   Date    :   18/01/12 00:49:05
#   Desc    :   logger config
#

import logging
import os
from logging.handlers import RotatingFileHandler


class Logger:
    LOGNAME = "test.log"
    LOGLEVEL = logging.DEBUG
    LOGNUM = 2
    LOGSIZE = 5 * 1024 * 1024
    LOGDIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), "log")
    if not os.path.exists(LOGDIR):
        os.mkdir(LOGDIR)
    LOGFILE = os.path.join(LOGDIR, LOGNAME)

    def __init__(self):
        formatter = logging.Formatter("%(asctime)s %(filename)s[l:%(lineno)d] %(levelname)s - %(message)s")
        console_hdl = logging.StreamHandler()
        console_hdl.setFormatter(formatter)
        # console_hdl.setLevel(Logger.LOGLEVEL)
        file_hdl = RotatingFileHandler(filename=Logger.LOGFILE,
                                       maxBytes=Logger.LOGSIZE,
                                       backupCount=Logger.LOGNUM)
        file_hdl.setFormatter(formatter)
        # file_hdl.setLevel(Logger.LOGLEVEL)
        self.logger = logging.getLogger()
        self.logger.addHandler(console_hdl)
        self.logger.addHandler(file_hdl)
        self.logger.setLevel(Logger.LOGLEVEL)

    def info(self, msg, *args, **kwargs):
        self.logger.info(msg, *args, **kwargs)

    def debug(self, msg, *args, **kwargs):
        self.logger.debug(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        self.logger.warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self.logger.error(msg, *args, **kwargs)


logger = Logger()
