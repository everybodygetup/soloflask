from flask import Blueprint, request, render_template, redirect, flash
from app.extensions import db
from app.parts.models import SpareParts
from app.core.forms import KodForm

core = Blueprint('core', __name__, template_folder='templates')


@core.before_app_request
def create_tables():
    db.create_all()
    

@core.route('/index', methods=['GET', 'POST'])
@core.route('/', methods=['GET', 'POST'])
def index():
    form = KodForm()
    if form.validate_on_submit():
        kod_search = SpareParts.query.filter(SpareParts.title.like(f'%{form.find.data}%')).all()
        return render_template('index.j2', kod_search=kod_search, form=form)
    return render_template('index.j2', form=form)


@core.route('/about')
def about():
    return render_template('about.j2')


