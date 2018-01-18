#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   Jiadi Yue
#   E-mail  :   jdyue19@gmail.com
#   Date    :   15/04/17 15:27:24
#   Desc    :   handler map to urls
#

from handlers import error
from handlers import index, login

routes = []
routes.extend(index.routes)
routes.extend(login.routes)


routes.extend(error.routes)
