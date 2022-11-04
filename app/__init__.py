from flask import Flask
from config import Config
from extensions import babel, db, executor, mail, migrate, security
from app.posts import posts
from app.core import core
from app.core.models import user_datastore


app = Flask(__name__)
app.config.from_object(Config)

mail.init_app(app)
babel.init_app(app)
executor.init_app(app)
db.init_app(app)
migrate.init_app(app, db)
security.init_app(app, user_datastore)


app.register_blueprint(posts)
app.register_blueprint(core)


