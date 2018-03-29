#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/28 20:29
# @Author  : Dengsc
# @Site    :
# @File    : table.py
# @Software: PyCharm


from flask_restful import Resource
from auth import auth
from app.api.v1 import api


class TableAPI(Resource):

    decorators = [auth.login_required, ]

    def get(self):
        return {
            'code': 20000,
            'data': {
                'items': [
                    {
                        'id': '360000199306106784',
                        'title': 'Mglmg kterc exbr kdpgvt rfuncbga haotykj '
                                 'cjasbxxu jberoy nfurkg ekmgpp qnnv oosqn'
                                 ' kpakuaej nbxs shueu ctjnyhbonw '
                                 'pzinlelcr utypmbgt.',
                        'status': 'draft',
                        'author': 'name',
                        'display_time': '2001-03-17 06:35:08',
                        'pageviews': 4212
                    },
                    {
                        'id': '140000199204050256',
                        'title': 'Pwnotb dpy phyfkyq mtqhlhxre qdmktpth rggx'
                                 ' byad rnhjph yaye btlrbij hrtdxlf.',
                        'status': 'published',
                        'author': 'name',
                        'display_time': '1975-05-19 02:19:44',
                        'pageviews': 4319
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


api.add_resource(TableAPI, '/table/list')
