#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/27 19:46
# @Author  : Dengsc
# @Site    :
# @File    : user.py
# @Software: PyCharm


from flask import g, abort
from flask_restful import Resource, reqparse, marshal_with, fields
from app.models.account import User
from auth import multi_auth, self_only
from app.api.v1 import api, meta_fields
from app.helpers import paginate


user_parser = reqparse.RequestParser()
user_parser.add_argument('username', type=str)
user_parser.add_argument('password', type=str)


# Marshaled field definitions for user objects
user_fields = {
    'email': fields.String,
    'username': fields.String,
    'role_id': fields.String,
    'confirmed': fields.String,
    'name': fields.String,
    'location': fields.String,
    'about_me': fields.String,
    'member_since': fields.String,
    'last_seen': fields.String,
    'avatar_hash': fields.String
}


# Marshaled field definitions for collections of user objects
user_collection_fields = {
    'items': fields.List(fields.Nested(user_fields)),
    'meta': fields.Nested(meta_fields),
}


@marshal_with(user_fields)
def format_user(user):
    return user


@marshal_with(user_collection_fields)
@paginate()
def format_users(users):
    return users


class UserResource(Resource):

    def get(self, user_id=None, username=None):
        user = None
        if username is not None:
            user = User.get_by_username(username)
        else:
            user = User.get_by_id(user_id)

        if not user:
            abort(404)
        return {
            'code': 20000,
            'data': format_user(user)
        }

    @multi_auth.login_required
    @self_only
    def post(self, user_id=None, username=None):
        g.current_user.update(**user_parser.parse_args())
        return {
            'code': 20000,
            'data': format_user(g.current_user)
        }

    @multi_auth.login_required
    @self_only
    def delete(self, user_id=None, username=None):
        g.current_user.delete()
        return 204


class UserCollectionResource(Resource):

    def get(self):
        users = User.query
        return {
            'code': 20000,
            'data': format_users(users)
        }

    @marshal_with(user_fields)
    def post(self):
        user = User.create(**user_parser.parse_args())
        return {
            'code': 20000,
            'data': format_user(user)
               }, 201


api.add_resource(UserResource, '/users/<int:user_id>/', '/users/<username>/')
api.add_resource(UserCollectionResource, '/users/')
