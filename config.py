import os

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    APP_NAME = "SpareParts"

    BABEL_DEFAULT_LOCALE = "ru"
    LANGUAGES = ["en", "ru"]

    MAIL_ADMINS = ["a9113621595@gmail.com"]

    MAIL_SERVER = os.getenv("MAIL_SERVER")
    MAIL_PORT = int(os.getenv("MAIL_PORT", 465))
    MAIL_USE_SSL = os.getenv("MAIL_USE_SSL", False)
    MAIL_USE_TLS = os.getenv("MAIL_USE_TLS", False)
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    MAIL_BACKEND = os.getenv("MAIL_BACKEND")

    SECURITY_CHANGEABLE = True
    SECURITY_CONFIRMABLE = False
    SECURITY_REGISTERABLE = True
    SECURITY_RECOVERABLE = True
    SECURITY_TRACKABLE = True

    SECURITY_PASSWORD_LENGTH_MIN = 5
    SECURITY_POST_LOGIN_VIEW = "/lk"
    SECURITY_EMAIL_SENDER = os.getenv("MAIL_USERNAME")

    SECURITY_LOGIN_USER_TEMPLATE = "security/login.j2"
    SECURITY_REGISTER_USER_TEMPLATE = "security/register.j2"
    SECURITY_RESET_PASSWORD_TEMPLATE = "security/reset.j2"
    SECURITY_FORGOT_PASSWORD_TEMPLATE = "security/forgot.j2"
    SECURITY_CHANGE_PASSWORD_TEMPLATE = "security/change.j2"
    SECURITY_SEND_CONFIRMATION_TEMPLATE = "security/confirm.j2"

    SECURITY_PASSWORD_SALT = os.getenv("SECURITY_PASSWORD_SALT", "kjasdkjh234df")

    SQLALCHEMY_TRACK_MODIFICATIONS = True

    WTF_CSRF_ENABLED = True
    WTF_CSRF_SECRET_KEY = "b7&dZxm2_xp^jz@ddX$$e=b160k5ru&+d"
    WTF_CSRF_SSL_STRICT = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(BaseConfig):
    basedir = os.path.abspath(os.path.dirname(__file__))

    DEBUG = True
    DEV_SECRET_KEY = "y5gD_xpd+f6ahaF#o&*VCC)V&Adm2qt&"
    SECRET_KEY = os.getenv("SECRET_KEY", DEV_SECRET_KEY)
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'app.db')}"


class TestingConfig(DevelopmentConfig):
    TESTING = True


class ProductionConfig(BaseConfig):
    DEBUG = False
    DB_DRIVER = "mysql"
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "3306")
    DB_NAME = os.getenv("DB_NAME")
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_DATABASE_URI = (
        f"{DB_DRIVER}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_size": 10,
        "pool_recycle": 3600,
        "pool_pre_ping": True,
    }


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
}
