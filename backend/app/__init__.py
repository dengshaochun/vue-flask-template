#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/27 17:36
# @Author  : Dengsc
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm


from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_cors import CORS
from config import config

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
api = Api()
cors = CORS()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'account.login'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    cors.init_app(app, resources={"/api/*": {"origins": "*"}})

    from .api_1_0 import api_1_0 as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1.0')

    from api_1_0.user_api import LoginAPI, UserAPI, TableAPI, LogoutAPI
    api.add_resource(LoginAPI, '/api/user/login')
    api.add_resource(LogoutAPI, '/api/user/logout')
    api.add_resource(UserAPI, '/api/user/info')
    api.add_resource(TableAPI, '/api/table/list')

    api.init_app(app)

    return app
