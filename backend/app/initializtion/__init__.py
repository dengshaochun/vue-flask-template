#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/28 21:09
# @Author  : Dengsc
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm


from app.database import db
from app.models.account import User, Role


class Init(object):

    @staticmethod
    def add_role():
        Role.insert_roles()

    @staticmethod
    def add_user():
        u = User()
        u.username = 'dengsc'
        u.email = 'dengsc@example.com'
        u.password = '12345'
        u.confirmed = True
        u.role = Role.get_by_name('Administrator')
        db.session.add(u)
        db.session.commit()
