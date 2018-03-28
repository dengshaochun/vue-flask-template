#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/27 19:46
# @Author  : Dengsc
# @Site    :
# @File    : user.py
# @Software: PyCharm


from flask import g
from flask_restful import Resource, reqparse, marshal_with, fields
from app.models.account import Role
from auth import auth
from app.api.v1 import api, meta_fields
from app.helpers import paginate


parser = reqparse.RequestParser()
parser.add_argument('username', type=str)
parser.add_argument('password', type=str)


# Marshaled field definitions for user objects
user_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'sex': fields.String,
    'role_id': fields.String,
    'confirmed': fields.String,
    'disable': fields.String,
    'mobile': fields.String,
    'qq': fields.String,
    'wechat': fields.String,
    'mark': fields.String,
    'gen_date': fields.String
}


# Marshaled field definitions for collections of user objects
user_collection_fields = {
    'items': fields.List(fields.Nested(user_fields)),
    'meta': fields.Nested(meta_fields),
}


class UserResource(Resource):

    decorators = [auth.login_required, ]

    def get(self):
        return {
            'code': 20000,
            'data': {
                'roles': [x.name for x in Role.query.all() if x is not None],
                'role': [
                    Role.query.filter_by(id=g.current_user.role_id).first().name
                ],
                'name': g.current_user.username,
                'avatar': 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif'
            }
        }

    def put(self):
        pass

    def delete(self):
        pass


api.add_resource(UserResource, '/user/info')
