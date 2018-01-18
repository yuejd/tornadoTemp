#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   Jiadi Yue
#   E-mail  :   jdyue19@gmail.com
#   Date    :   15/04/20 23:13:04
#   Desc    :   Index handler
#
from base import BaseHandler


class ErrorHandler(BaseHandler):
    def get(self):
        self.write_error(404)


routes = [
    (r".*", ErrorHandler)
]
