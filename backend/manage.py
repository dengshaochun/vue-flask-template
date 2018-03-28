#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/27 17:39
# @Author  : Dengsc
# @Site    : 
# @File    : manage.py
# @Software: PyCharm


from flask_script import Manager, Shell, Server
from flask_migrate import MigrateCommand

from app import create_app
from app.models.account import (User, Role, Log)
from app.database import db
from app.initializtion import Init

import sys

reload(sys)
sys.setdefaultencoding('utf8')

app = create_app()

manager = Manager(app)


def _make_context():
    """Return context dict for a shell session so you can access
    app, db, and the User model by default.
    """
    return {'app': app,
            'db': db,
            'User': User,
            'Role': Role,
            'Log': Log
            }


@manager.command
def test():
    """Run the tests."""
    import pytest
    exit_code = pytest.main(['tests', '-q'])
    return exit_code


@manager.command
def feed_data():
    Init.add_role()
    Init.add_user()


manager.add_command('server', Server())
manager.add_command('shell', Shell(make_context=_make_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
