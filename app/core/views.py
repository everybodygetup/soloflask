from flask import Blueprint,request,render_template,redirect
from app.extensions import db


core = Blueprint('core', __name__, template_folder='templates')

@core.before_app_request
def create_tables():
    db.create_all()
    



@core.route('/')
@core.route('/index')
def index():
    '''Главная страница'''
    return render_template('index.j2')