#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/28 21:09
# @Author  : Dengsc
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm


from app.database import db
from app.models.account import User, Role, Permission


class Init(object):

    @staticmethod
    def add_role():
        r = Role()
        r.name = 'admin'
        r.permission = Permission.ADMINISTER
        db.session.add(r)
        db.session.commit()

    @staticmethod
    def add_user():
        u = User()
        u.username = 'dengsc'
        u.email = 'dengsc@example.com'
        u.password = '12345'
        u.role = Role.get_by_id(1)
        db.session.add(u)
        db.session.commit()
