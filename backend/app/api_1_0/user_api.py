#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/27 19:46
# @Author  : Dengsc
# @Site    :
# @File    : user_api.py
# @Software: PyCharm


from flask import g
from flask_restful import Resource, reqparse
from ..models.account import Role
from authentication import auth


parser = reqparse.RequestParser()
parser.add_argument('username', type=str)
parser.add_argument('password', type=str)
parser.add_argument('token', type=str)


class UserAPI(Resource):

    decorators = [auth.login_required, ]

    def get(self):
        # args = parser.parse_args()
        # user_obj = User.verify_auth_token(args.get('token', ''))
        # if user_obj:
        return {
            "code": 20000,
            "data": {
                "roles": [x.name for x in Role.query.all() if x is not None],
                "role": [
                    Role.query.filter_by(id=g.current_user.role_id).first().name
                ],
                "name": g.current_user.username,
                "avatar": "https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif"
            }
        }
        # else:
            # return unauthorized('user unauthorized!')

    def put(self):
        pass

    def delete(self):
        pass


class LoginAPI(Resource):
    decorators = [auth.login_required, ]

    def get(self):
        pass

    def post(self):
        # args = parser.parse_args()
        # user_obj = User.query.filter_by(email=args.get('username', '')).first()
        # if user_obj and user_obj.verify_password(args.get('password', '')):
        return {
            'code': 20000,
            'data': {
                'token': g.current_user.generate_auth_token(expiration=3600)
                }
        }
        # else:
        #     return unauthorized('user unauthorized!')

    def put(self):
        pass

    def delete(self):
        pass


class LogoutAPI(Resource):

    def get(self):
        pass

    def post(self):
        return {
            "code": 20000,
            "data": "success"
        }

    def put(self):
        pass

    def delete(self):
        pass


class TableAPI(Resource):

    decorators = [auth.login_required, ]

    def get(self):
        # if User.verify_auth_token(parser.parse_args().get('token', '')):
        return {
            "code": 20000,
            "data": {
                "items": [
                    {
                        "id": "360000199306106784",
                        "title": "Mglmg kterc exbr kdpgvt rfuncbga haotykj cjasbxxu jberoy nfurkg ekmgpp qnnv oosqn kpakuaej nbxs shueu ctjnyhbonw pzinlelcr utypmbgt.",
                        "status": "draft",
                        "author": "name",
                        "display_time": "2001-03-17 06:35:08",
                        "pageviews": 4212
                    },
                    {
                      "id": "140000199204050256",
                      "title": "Pwnotb dpy phyfkyq mtqhlhxre qdmktpth rggx byad rnhjph yaye btlrbij hrtdxlf.",
                      "status": "published",
                      "author": "name",
                      "display_time": "1975-05-19 02:19:44",
                      "pageviews": 4319
                    }
                ]
            }
        }

    def post(self):
        pass

    def delete(self):
        pass

    def put(self):
        pass
