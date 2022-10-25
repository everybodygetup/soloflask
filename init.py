import os


from extensions import babel, db, executor, mail, migrate, security
from flask import Flask





app = Flask(__name__)

babel.init_app(app)
db.init_app(app)
executor.init_app(app)
mail.init_app(app)
migrate.init_app(app, db)
security.init_app(app)
