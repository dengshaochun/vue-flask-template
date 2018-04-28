#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/27 17:44
# @Author  : Dengsc
# @Site    :
# @File    : authentication.py
# @Software: PyCharm


import functools
from flask import g, request, abort
from app.extensions import basic_auth, token_auth, multi_auth
from app.models.account import User
from app.api.v1 import api_blueprint
from .errors import unauthorized, forbidden


@basic_auth.verify_password
def verify_password(email_or_token, password):
    # 查看参数是否携带token,否则在header中查找
    if email_or_token == '':
        return False
    if password == '':
        return False
    user = User.query.filter_by(email=email_or_token).first()
    if not user:
        return False
    g.current_user = user
    g.token_used = False
    return user.verify_password(password)


@basic_auth.error_handler
def auth_error():
    return unauthorized('Invalid credentials!')


@token_auth.verify_token
def verify_token(token):
    g.current_user = None
    try:
        g.current_user = User.verify_auth_token(token)
        g.token_used = True
        return g.current_user is not None
    except:
        return False


@token_auth.error_handler
def auth_error():
    return unauthorized('Invalid credentials!')


@api_blueprint.before_request
@multi_auth.login_required
def before_request():
    if request.method != 'OPTIONS':
        if not g.current_user.is_anonymous() and \
                not g.current_user.confirmed:
            return forbidden('Unconfirmed account')


def self_only(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if kwargs.get('username', None):
            if g.current_user.username != kwargs['username']:
                abort(403)
        if kwargs.get('user_id', None):
            if g.current_user.id != kwargs['user_id']:
                abort(403)
        return func(*args, **kwargs)
    return wrapper

