from datetime import datetime
from app.extensions import db
from flask_security import SQLAlchemyUserDatastore
from flask_security.models.fsqla_v2 import FsModels, FsRoleMixin, FsUserMixin


roles_users = db.Table('roles_users',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id')))


class User(db.Model, FsUserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean)
    confirmed_at = db.Column(db.DateTime)
    roles = db.relationship(
        'Role', 
        secondary=roles_users, 
        backref=db.backref('users', lazy='dynamic')
    )


class Role(db.Model, FsRoleMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    description = db.Column(db.String(255))


user_datastore = SQLAlchemyUserDatastore(db, User, Role)