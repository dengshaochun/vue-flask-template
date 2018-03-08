#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/27 17:41
# @Author  : Dengsc
# @Site    :
# @File    : config.py
# @Software: PyCharm


import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:

    def __init__(self):
        pass

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-are-never-guess-dengsc'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ADMIN = 'admin@jiguang.cn'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
    SQLALCHEMY_BINDS = {
        'data': 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
    }


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')
    SQLALCHEMY_BINDS = {
        'data': 'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')
    }


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-prod.sqlite')
    SQLALCHEMY_BINDS = {
        'data': 'sqlite:///' + os.path.join(basedir, 'data-prod.sqlite')
    }


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
