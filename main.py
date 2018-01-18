#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   Jiadi Yue
#   E-mail  :   jdyue19@gmail.com
#   Date    :   15/04/17 13:14:19
#   Desc    :   main app
#

import tornado.httpserver
import tornado.ioloop
import tornado.web
import os
import sys
from lib.log import logger
from urls import routes as handlers


class Application(tornado.web.Application):
    def __init__(self):
        settings = dict(
            blog_title=u"test web",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            # ui_modules = {"Entry1": EntryModule, "topx": TopXModule},
            xsrf_cookies=True,
            # use below method to generate cookie_secret key
            # import base64
            # import uuid
            # print base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes)
            cookie_secret="tjNXzvzDSOeNZucdZsW9KvmBAmTCH0a0okEyJCeA7EQ=",
            debug=True,
            login_url="/login"
        )
        tornado.web.Application.__init__(self, handlers, **settings)


def main(port=8888):
    logger.debug("main: web started.")
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main()
