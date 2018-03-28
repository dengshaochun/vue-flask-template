#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/27 17:36
# @Author  : Dengsc
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm


"""
The demo module, containing the app factory function.
"""

import os

from flask import Flask

from app.settings import ProdConfig, DevConfig
from app.extensions import (
    db,
    migrate,
    cors,
    login_manager
)
from app.api.v1 import api_blueprint

if os.getenv('FLASK_ENV') == 'prod':
    DefaultConfig = ProdConfig
else:
    DefaultConfig = DevConfig


def create_app(config_object=DefaultConfig):
    """
    An application factory, as explained here:
        http://flask.pocoo.org/docs/patterns/appfactories/

    :param config_object: The configuration object to use.
    :return: 
    """

    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    cors.init_app(app, resources={'/api/*': {'origins': '*'}})


def register_blueprints(app):
    app.register_blueprint(api_blueprint)
