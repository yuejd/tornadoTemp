#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   Jiadi Yue
#   E-mail  :   jdyue19@gmail.com
#   Date    :   15/04/17 13:14:19
#   Desc    :   Login Handler
#

from handlers.base import BaseHandler
from datetime import datetime
from db.model import Person, LoginInfo


class LoginHandler(BaseHandler):
    def get(self):
        if not self.current_user:
            self.render('login.html', message=None)
        else:
            self.redirect("/")

    def post(self):
        name = self.get_argument("name")
        try:
            person = Person.get(Person.name == name)
            self.set_secure_cookie("name", name, expires_days=1)
            person.logintimes += 1
            person.save()
            self.redirect("/")
        except Person.DoesNotExist:
            log = "test"
            self.render("login.html", message=log)
            LoginInfo.create(logintime=datetime.now(), name=name)


class LogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie("name")
        self.redirect("/login")


routes = [
    (r"/login", LoginHandler),
    (r"/logout", LogoutHandler),
]
