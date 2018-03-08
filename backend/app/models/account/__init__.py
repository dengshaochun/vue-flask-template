#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/27 17:46
# @Author  : Dengsc
# @Site    :
# @File    : __init__.py.py
# @Software: PyCharm


from datetime import datetime
from app import db
from app import login_manager
from flask_login import UserMixin, AnonymousUserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, BadSignature
from flask import current_app
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Permission:
    def __init__(self):
        pass
    COMMON = 0x01
    ADMINISTER = 0x80


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permission = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name


class UserLogs(db.Model):
    __tablename__ = 'user_logs'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    log_type = db.Column(db.String(64))
    log_main = db.Column(db.String(200))
    log_context = db.Column(db.String(300))
    log_time = db.Column(db.DateTime, default=datetime.now())

    def to_json(self):
        return {
            'log_type': self.log_type,
            'log_context': self.log_context,
            'log_time': self.log_time.strftime('%Y-%m-%d %H:%M:%S'),
            'log_ip': eval(self.log_main).get('ip'),
            'user_agent': eval(self.log_main).get('agent')
        }

    def __repr__(self):
        return '<UserLogs %r>' % self.id


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(128))
    sex = db.Column(db.Integer, default=-1)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    confirmed = db.Column(db.Boolean, default=False)
    disable = db.Column(db.Boolean, default=False)
    department = db.Column(db.String(128))
    position = db.Column(db.String(128))
    mobile = db.Column(db.String(20))
    qq = db.Column(db.String(20))
    wechat = db.Column(db.String(50))
    mark = db.Column(db.String(200))
    indb_date = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        if self.role is None:
            if self.email == current_app.config['ADMIN']:
                self.role = Role.query.filter_by(permission=0xff).first()
            if self.role is None:
                self.role = Role.query.filter_by(default=True).first()

    def can(self, permissions):
        return self.role is not None and \
               (self.role.permission & permissions) == permissions

    def is_administrator(self):
        return self.can(Permission.ADMINISTER)

    def generate_confirmation_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'confirm': self.id})

    def generate_auth_token(self, expiration):
        s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'id': self.id})

    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        return True

    @property
    def password(self):
        raise AttributeError('password is not readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None  # valid token, but expired
        except BadSignature:
            return None  # invalid token
        user = User.query.get(data['id'])
        return user

    def __repr__(self):
        return '<User %r>' % self.username


class AnonymousUser(AnonymousUserMixin):

    @staticmethod
    def can(**kwargs):
        return False

    @staticmethod
    def is_administrator():
        return False


class Alembic(db.Model):
    __tablename__ = 'alembic_version'
    version_num = db.Column(db.String(32), primary_key=True, nullable=False)

    @staticmethod
    def clear_a():
        for a in Alembic.query.all():
            print a.version_num
            db.session.delete(a)
        db.session.commit()
        print '======== data in Table: Alembic cleared!'

login_manager.anonymous_user = AnonymousUser
