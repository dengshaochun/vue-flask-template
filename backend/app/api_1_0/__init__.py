#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/27 19:45
# @Author  : Dengsc
# @Site    :
# @File    : __init__.py.py
# @Software: PyCharm


from flask import Blueprint
api_1_0 = Blueprint('api_1_0', __name__)

from . import errors, authentication
