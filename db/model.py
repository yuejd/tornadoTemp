#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   Jiadi Yue
#   E-mail  :   jdyue19@gmail.com
#   Date    :   15/01/26 13:26:54
#   Desc    :   test database model for peewee
#

from peewee import *
import os
DBPATH = os.path.dirname(__file__)
DBNAME = "test.db"
DBFILE = os.path.join(DBPATH, DBNAME)

testdb = SqliteDatabase(DBFILE, threadlocals=True)


class BaseModel(Model):
    class Meta:
        database = testdb


class Person(BaseModel):
    name = CharField(max_length=40)
    phone = CharField(null=True)
    others = TextField(null=True)
    mdftime = DateTimeField(null=True)
    right = IntegerField(default=0)
    logintimes = IntegerField(default=0)

class LoginInfo(BaseModel):
    logintime = DateTimeField()
    name = CharField()
