#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/28 16:46
# @Author  : Dengsc
# @Site    : 
# @File    : de.py
# @Software: PyCharm


from functools import wraps
from flask import abort
from flask_login import current_user
from models.account import Permission


def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.can(permission):
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator


def admin_required(f):
    return permission_required(Permission.ADMIN)(f)
