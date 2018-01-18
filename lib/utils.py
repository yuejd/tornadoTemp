#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   Jiadi Yue
#   E-mail  :   jdyue19@gmail.com
#   Date    :   15/01/26 13:36:52
#   Desc    :   some utilities
#

import os
import signal


def find_subclasses(klass, include_self=False):
    accum = []
    for child in klass.__subclasses__():
        accum.extend(find_subclasses(child, True))
    if include_self:
        accum.append(klass)
    return accum


def get_file_names(file_path, inner):
    source_file = os.listdir(file_path)
    return filter(lambda x: x.find(inner) >= 0, source_file)


class Timeout():
    """Timeout class using ALARM signal."""
    class Timeout(Exception):
        message = "timeout exception"
        pass

    def __init__(self, sec):
        self.sec = sec

    def __enter__(self):
        signal.signal(signal.SIGALRM, self.raise_timeout)
        signal.alarm(self.sec)

    def __exit__(self, *args):
        signal.alarm(0)    # disable alarm

    def raise_timeout(self, *args):
        raise Timeout.Timeout()
