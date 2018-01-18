#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   Jiadi Yue
#   E-mail  :   jdyue19@gmail.com
#   Date    :   15/04/17 13:36:29
#   Desc    :   base handler
#

import tornado.web
import sys
sys.path.append("..")
from db.model import testdb
# from tornado.web import ErrorHandler


class BaseHandler(tornado.web.RequestHandler):
    def on_finish(self):
        if not testdb.is_closed():
            testdb.close()

    def write_error(self, status_code, **kwargs):
        if status_code == 404:
            self.write("error: Page Not Found")
        elif status_code == 400:
            self.write("error: Bad Requeste")
        elif status_code == 500:
            self.write("Internal Server Error")
        else:
            super(BaseHandler, self).write_error(status_code, **kwargs)

    def get_current_user(self):
        return self.get_secure_cookie("name")
