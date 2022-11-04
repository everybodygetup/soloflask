import os


basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    
    SECURITY_CHANGEABLE = True
    SECURITY_CONFIRMABLE = True
    SECURITY_REGISTERABLE = True
    SECURITY_RECOVERABLE = True
    SECURITY_TRACKABLE = True

    SECURITY_PASSWORD_LENGTH_MIN = 5
    SECURITY_POST_LOGIN_VIEW = "/lk"
    SECURITY_EMAIL_SENDER = ("Costravel", "mail@costravel.ru")

    SECURITY_LOGIN_USER_TEMPLATE = "security/login.j2"
    SECURITY_REGISTER_USER_TEMPLATE = "security/register.j2"
    SECURITY_RESET_PASSWORD_TEMPLATE = "security/reset.j2"
    SECURITY_FORGOT_PASSWORD_TEMPLATE = "security/forgot.j2"
    SECURITY_CHANGE_PASSWORD_TEMPLATE = "security/change.j2"
    SECURITY_SEND_CONFIRMATION_TEMPLATE = "security/confirm.j2"

    SECURITY_PASSWORD_SALT = os.getenv("SECURITY_PASSWORD_SALT", "kasdasd123")

    SQLALCHEMY_TRACK_MODIFICATIONS = True

    WTF_CSRF_ENABLED = True
    WTF_CSRF_SECRET_KEY = "b4nds434nsdf654756vxv"
    WTF_CSRF_SSL_STRICT = False

    @staticmethod
    def init_app(app):
        pass
 