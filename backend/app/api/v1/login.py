#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/28 20:27
# @Author  : Dengsc
# @Site    :
# @File    : login.py
# @Software: PyCharm


from flask import g
from flask_restful import Resource
from auth import multi_auth
from app.api.v1 import api
from .errors import unauthorized
from flask_login import logout_user


class LoginResource(Resource):
    decorators = [multi_auth.login_required, ]

    def post(self):
        if g.current_user.is_anonymous() or g.token_used:
            return unauthorized('Invalid credentials!')
        data = {
            'token': g.current_user.generate_auth_token(expiration=3600),
            'username': g.current_user.username,
            'expiration': 3600
        }
        return {
            'code': 20000,
            'data': data
        }


class LogoutResource(Resource):
    decorators = [multi_auth.login_required, ]

    def post(self):
        logout_user()
        return {
            'code': 20000,
            'data': 'success'
        }


api.add_resource(LoginResource, '/login/')
api.add_resource(LogoutResource, '/logout/')
