#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   Jiadi Yue
#   E-mail  :   jdyue19@gmail.com
#   Date    :   15/04/20 23:13:04
#   Desc    :   Error handler
#
from base import BaseHandler
import tornado.web


class IndexHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render("index.html")


routes = [
    (r"/", IndexHandler)
]
