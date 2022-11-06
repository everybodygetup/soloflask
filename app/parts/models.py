from datetime import datetime

from app.extensions import db
from app.models import ModelMixin




class SpareParts(db.Model,ModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), primary_key=False)
    intro = db.Column(db.String(300), primary_key=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<TnWed %r>' % self.id