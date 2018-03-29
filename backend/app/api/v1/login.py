#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/28 20:27
# @Author  : Dengsc
# @Site    :
# @File    : login.py
# @Software: PyCharm


from flask import g
from flask_restful import Resource
from auth import auth
from app.api.v1 import api


class LoginResource(Resource):
    decorators = [auth.login_required, ]

    def get(self):
        pass

    def post(self):
        return {
            'code': 20000,
            'data': {
                'token': g.current_user.generate_auth_token(expiration=3600)
            }
        }

    def put(self):
        pass

    def delete(self):
        pass


class LogoutResource(Resource):

    def get(self):
        pass

    def post(self):
        return {
            'code': 20000,
            'data': 'success'
        }

    def put(self):
        pass

    def delete(self):
        pass


api.add_resource(LoginResource, '/user/login')
api.add_resource(LogoutResource, '/user/logout')
