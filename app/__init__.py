from flask import Flask
from config import Config
from app.extensions import db,migrate
from app.posts import posts
from app.core import core

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate.init_app(app, db)

app.register_blueprint(posts)
app.register_blueprint(core)


from app import routes, models