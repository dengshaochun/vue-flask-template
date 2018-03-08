#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/27 17:39
# @Author  : Dengsc
# @Site    : 
# @File    : manage.py
# @Software: PyCharm


import os
from flask_script import Manager, Shell
from flask_migrate import MigrateCommand, Migrate
from app import create_app, db
from app.models.account import User, Role


app = create_app(os.environ.get('CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)


manager.add_command('db', MigrateCommand)
manager.add_command('shell', Shell(make_context=make_shell_context))


@manager.command
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.command
def clear_alembic():
    from app.models.account import Alembic
    Alembic.clear_a()


if __name__ == '__main__':
    manager.run()
