#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/27 17:44
# @Author  : Dengsc
# @Site    :
# @File    : authentication.py
# @Software: PyCharm


from flask import g, request
from app.extensions import auth
from app.models.account import User
from app.api.v1 import api_blueprint
from .errors import unauthorized, forbidden


@auth.verify_password
def verify_password(email_or_token, password):
    # 查看参数是否携带token,否则在header中查找
    email_or_token = email_or_token if email_or_token else request.headers.get(
        'Token', '')
    if email_or_token == '':
        return False
    if password == '':
        g.current_user = User.verify_auth_token(email_or_token)
        g.token_used = True
        return g.current_user is not None
    user = User.query.filter_by(email=email_or_token).first()
    if not user:
        return False
    g.current_user = user
    g.token_used = False
    return user.verify_password(password)


@auth.error_handler
def auth_error():
    return unauthorized('Invalid credentials')


@api_blueprint.before_request
@auth.login_required
def before_request():
    if request.method != 'OPTIONS':
        if not g.current_user.is_anonymous() and \
                not g.current_user.confirmed:
            return forbidden('Unconfirmed account')
