#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   Jiadi Yue
#   E-mail  :   jdyue19@gmail.com
#   Date    :   15/01/19 00:19:31
#   Desc    :   configuration for library
#

# from datetime import datetime
import os

DEBUG = True

SITE_NAME = u"Test"
SITE_KEYWORDS = """"""
SITE_DESC = """Site powered by tornado,peewee"""
DOMAIN = 'http://0.0.0.0:8888'

# THEME_NAME = 'fluid-blue'

DB_ENGINE = 'peewee.SqliteDatabase'  # peewee.SqliteDatabase,peewee.MySQLDatabase
DB_HOST = '0.0.0.0'
DB_USER = 'root'
DB_PASSWD = 'root'
DB_NAME = os.path.join(os.path.dirname(__file__), 'blog.db')  # db file if DB_ENGINE is SqliteDatabase
