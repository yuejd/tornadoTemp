#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   Jiadi Yue
#   E-mail  :   jdyue19@gmail.com
#   Date    :   15/01/26 13:33:26
#   Desc    :   test database manager
#

import sys
sys.path.append("..")
import model
from tornado.options import define, options
from lib.utils import find_subclasses
from lib.config import *
from datetime import datetime
import logging
logger = logging.getLogger()

define("cmd", default="syncdb", help="command for db sync")
# python dbm.py --cmd=syncdb to recreate db


class DBM:
    @classmethod
    def syncdb(cls):
        """
        to clean tables or recreate tables
        """
        mods = find_subclasses(model.BaseModel)
        for mod in mods:
            if mod.table_exists():
                mod.drop_table()
            mod.create_table()
            logger.info("created table: " + mod._meta.db_table)
        cls.add_user_admin()
        logger.info("user: admin created")

    @classmethod
    def add_user_admin(cls):
        p = model.Person.create(name="admin")
        p.save()


if __name__ == '__main__':
    options.parse_command_line()
    if options.cmd == "syncdb":
        DBM.syncdb()
