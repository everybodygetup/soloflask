from datetime import datetime
from extensions import db
from flask_security import SQLAlchemyUserDatastore
from flask_security.models.fsqla_v2 import FsModels, FsRoleMixin, FsUserMixin

FsModels.set_db_info(db)


class Role(db.Model, FsRoleMixin):
    pass


class User(db.Model, FsUserMixin):
    posts = db.relationship("Post", backref="author", lazy="dynamic")
    firstname = db.Column(db.String(255))
    lastname = db.Column(db.String(255))
    phone = db.Column(db.String(20))



class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    text = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __repr__(self):
        return f"<Post {self.title}>"



user_datastore = SQLAlchemyUserDatastore(db, User, Role)