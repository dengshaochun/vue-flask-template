#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/27 19:45
# @Author  : Dengsc
# @Site    :
# @File    : __init__.py.py
# @Software: PyCharm


from flask_restful import Api, fields
from flask import Blueprint

api_blueprint = Blueprint('api', __name__, url_prefix='/api/v1')

api = Api(api_blueprint)

# Marshaled fields for links in meta section
link_fields = {
    'prev': fields.String,
    'next': fields.String,
    'first': fields.String,
    'last': fields.String,
}

# Marshaled fields for meta section
meta_fields = {
    'page': fields.Integer,
    'per_page': fields.Integer,
    'total': fields.Integer,
    'pages': fields.Integer,
    'links': fields.Nested(link_fields)
}


from app.api.v1 import auth  # NOQA
from app.api.v1 import errors  # NOQA
from app.api.v1 import user  # NOQA
from app.api.v1 import table  # NOQA
from app.api.v1 import login  # NOQA

