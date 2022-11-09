import os


from flask import Flask
from config import config
from app.extensions import babel, db, executor, mail, migrate, security
from app.parts import parts
from app.core import core
from app.core.models import user_datastore
from app.core.admin_view import admin

app = Flask(__name__)
app.config.from_object(config[os.getenv("FLASK_ENV", "production")])

mail.init_app(app)
babel.init_app(app)
executor.init_app(app)
db.init_app(app)
migrate.init_app(app, db)
security.init_app(app, user_datastore)


app.register_blueprint(parts)
app.register_blueprint(core)
app.register_blueprint(admin)



