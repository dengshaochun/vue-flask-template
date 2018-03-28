#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/26 14:54
# @Author  : Dengsc
# @Site    : 
# @File    : errors.py
# @Software: PyCharm


from flask import jsonify


def forbidden(message):
    response = jsonify({'error': 'forbidden', 'message': message})
    response.status_code = 403
    return response


def unauthorized(message):
    response = jsonify({'error': 'unauthorized', 'message': message})
    response.status_code = 401
    return response


def bad_request(message):
    response = jsonify({'error': 'bad requset', 'message': message})
    response.status_code = 400
    return response
