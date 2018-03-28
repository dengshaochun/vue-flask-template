#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/27 17:36
# @Author  : Dengsc
# @Site    :
# @File    : settings.py
# @Software: PyCharm
import os


class Config(object):
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-are-never-guess-dengsc'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ADMIN = 'admin@jiguang.cn'

    ERROR_404_HELP = False


class ProdConfig(Config):
    """Production configuration."""
    ENV = 'prod'
    DEBUG = False
    # DB URL variable set by heroku
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '')
    SQLALCHEMY_BINDS = {
        'data': os.environ.get('DATABASE_URL', '')
    }


class DevConfig(Config):
    """Development configuration."""
    ENV = 'dev'
    DEBUG = True
    DB_NAME = 'dev.db'
    DB_PATH = os.path.join(Config.PROJECT_ROOT, DB_NAME)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(DB_PATH)


class TestConfig(Config):
    """Test configuration."""
    ENV = 'test'
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
