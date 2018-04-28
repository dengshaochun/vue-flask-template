# -*- coding: utf-8 -*-
"""Extensions module. Each extension is initialized in the app factory located
in __init__.py
"""

from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth, MultiAuth
basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth(scheme='Bearer')
multi_auth = MultiAuth(basic_auth, token_auth)

from flask_sqlalchemy import SQLAlchemy  # NOQA
db = SQLAlchemy()

from flask_migrate import Migrate  # NOQA
migrate = Migrate()

from flask_cors import CORS  # NOQA
cors = CORS()

from flask_login import LoginManager  # NOQA
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'account.login'
