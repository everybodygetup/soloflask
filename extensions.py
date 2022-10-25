from flask_babel import Babel
from flask_executor import Executor
from flask_mailman import Mail
from flask_migrate import Migrate
from flask_security import Security
from flask_sqlalchemy import SQLAlchemy

babel = Babel()
db = SQLAlchemy()
executor = Executor()
mail = Mail()
migrate = Migrate()
security = Security()
